"""Compare Detailed Descendant Book Report's index Ref tuples
between dubperson=True and dubperson=False over example.gramps.

Loads example.gramps in-process, constructs the report twice, and
compares self.index_of_places / self.index_of_dates contents.
"""

import os
import sys

sys.path.insert(0, "/home/eddie/workspace/gramps")
sys.path.insert(0, "/home/eddie/workspace/addons-source/DescendantBooks")

from gramps.cli.user import User
from gramps.gen.db.utils import import_as_dict
from gramps.gen.plug.docgen import TextDoc


# --- minimal stand-ins ---------------------------------------------------

class FakeDoc(TextDoc):
    """Captures nothing — we only care about index dicts."""
    def init(self): pass
    def open(self, filename): pass
    def close(self): pass
    def page_break(self): pass
    def start_bold(self): pass
    def end_bold(self): pass
    def start_superscript(self): pass
    def end_superscript(self): pass
    def start_paragraph(self, style_name, leader=None): pass
    def end_paragraph(self): pass
    def start_table(self, name, style_name): pass
    def end_table(self): pass
    def start_row(self): pass
    def end_row(self): pass
    def start_cell(self, style_name, span=1): pass
    def end_cell(self): pass
    def write_text(self, text, mark=None, links=False): pass
    def write_markup(self, text, s_tags, mark=None): pass
    def write_styled_note(self, styledtext, format, style_name,
                          contains_html=False, links=False): pass
    def add_media(self, name, pos, x_cm, y_cm,
                  alt='', style_name=None, crop=None): pass
    def write_endnotes_ref(self, text, style_name): pass


def build_options(database, person, dubperson, omit_indexes_too=False):
    """Construct DetailedDescendantBookOptions filled in for our run."""
    import DetailedDescendantBookReport as ddbr
    opts = ddbr.DetailedDescendantBookOptions("dbb_test", database)
    opts.load_previous_values()
    # Inflate the menu with default values, then override what we care about
    menu = opts.menu
    menu.get_option_by_name("pid").set_value(person.get_gramps_id())
    menu.get_option_by_name("omitda").set_value(dubperson)
    menu.get_option_by_name("incindexdates").set_value(
        not omit_indexes_too
    )
    menu.get_option_by_name("incindexplaces").set_value(
        not omit_indexes_too
    )
    menu.get_option_by_name("incindexnames").set_value(
        not omit_indexes_too
    )
    return opts


def run_once(database, person, dubperson):
    import DetailedDescendantBookReport as ddbr
    user = User()
    opts = build_options(database, person, dubperson)
    report = ddbr.DetailedDescendantBookReport(database, opts, user)
    report.doc = FakeDoc()
    report.write_report()
    return {
        "index_of_dates": dict(report.index_of_dates),
        "index_of_places": dict(report.index_of_places),
        "ascendants_n": len(report.ascendants),
    }


def main():
    # Bootstrap the bits of Gramps' headless plumbing we need
    from gramps.gen.config import config
    config.init()
    from gramps.gen.filters import CustomFilters, reload_custom_filters
    reload_custom_filters()

    user = User()
    db = import_as_dict(
        "/home/eddie/workspace/gramps/example/gramps/example.gramps", user
    )
    db.db_name = "example"
    db.get_dbname = lambda: "example"

    # Pick a center person whose ascendant tree has multiple roots so
    # the multi-report scenario is exercised. Garner, Anne Therese
    # (I00016) is the example tree's typical center person.
    center = db.get_person_from_gramps_id("I00016")
    assert center is not None, "Could not find I00016 in example.gramps"

    print("=== dubperson=True (omit-duplicates on) ===")
    on = run_once(db, center, True)
    print("ascendants_n:", on["ascendants_n"])
    print("places count:", len(on["index_of_places"]))
    print("dates count:", len(on["index_of_dates"]))

    print("=== dubperson=False (omit-duplicates off) ===")
    off = run_once(db, center, False)
    print("ascendants_n:", off["ascendants_n"])
    print("places count:", len(off["index_of_places"]))
    print("dates count:", len(off["index_of_dates"]))

    # Compare: for places present in both, extract the "Ref: r g p" prefix
    # of any common date and check it matches.
    import re
    ref_re = re.compile(r"Ref:\s*(\S+)\s+(\S+)\s+(\S+)")
    common_places = set(on["index_of_places"]) & set(off["index_of_places"])
    print(f"\n{len(common_places)} places appear in BOTH index outputs")

    mismatches = []
    matches = 0
    samples = []
    for place in sorted(common_places):
        on_dates = on["index_of_places"][place]
        off_dates = off["index_of_places"][place]
        common_dates = set(on_dates) & set(off_dates)
        for date in common_dates:
            m_on = ref_re.search(on_dates[date])
            m_off = ref_re.search(off_dates[date])
            if not (m_on and m_off):
                continue
            if m_on.groups() == m_off.groups():
                matches += 1
                if len(samples) < 5:
                    samples.append((place, date, m_on.groups(), "MATCH"))
            else:
                mismatches.append(
                    (place, date, m_on.groups(), m_off.groups())
                )

    print(f"\nRef tuples comparison over common (place, date):")
    print(f"  matches:    {matches}")
    print(f"  mismatches: {len(mismatches)}")
    for place, date, on_t, off_t in samples:
        print(f"  ok  {place} / {date}: {on_t}")
    for place, date, on_t, off_t in mismatches[:8]:
        print(f"  MISMATCH {place} / {date}: on={on_t}  off={off_t}")
    if len(mismatches) > 8:
        print(f"  ... +{len(mismatches) - 8} more mismatches")


if __name__ == "__main__":
    main()
