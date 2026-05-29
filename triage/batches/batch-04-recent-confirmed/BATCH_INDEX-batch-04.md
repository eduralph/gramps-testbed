# Batch: batch-04-recent-confirmed

> Source: 20260523-Mantis_Export.csv, filtered to Product Version >= 5.2.0
> (the "recent" pool — 43 candidates; batch-03's 12 already excluded).
> Character: FIX-ORIENTED. Current-era confirmed bugs likely to reproduce on the
> gramps60/gramps61 tree, so expected yield is real patches, not long-tail closes.
>
> Selection: 43 recent − 5 non-defects (12757 help-menu wording, 13354 typo,
> 13404 dead .deb link, 13470 obsolete PO strings, 13839 source-comment typo)
> = 38 issues, all placed below.
>
> Branch rule (per 04-bug-batch-triage-playbook.md): addons-source →
> maintenance/gramps60; gramps core → maintenance/gramps61. "3rd Party Addons"
> is the SYMPTOM location — resolve addon-vs-core BY REPRODUCING.
>
> Every item has a Mantis entry → every item gets results/issue_<id>/mantis-comment.md.
> Platform-specific items (macOS/Windows) cannot be confirmed on Linux → they get
> a MANUAL-VERIFICATION.md instead of an outright close (playbook rule).
>
> STEP 0 for the batch: scrape the Mantis comment threads for these 38 (notes →
> per-issue .md) BEFORE writing verdicts. CSV Description/Steps is the starting
> signal; the threads are where root cause usually lives.

## A — Core defects, Linux-confirmable (likely real fixes -> gramps61)
| ID | Ver | Summary | Disposition |
|---|---|---|---|
| 13819 | 6.0.1 | Family Edit window changes order of parent families (MAJOR) | core fix, gramps61 — highest severity in batch |
| 14033 | 6.0.5 | Frequent spurious "Place cycle detected" errors | core fix, gramps61 |
| 13747 | 6.0.0 | Saving an unmodified DB changes the DB on disk | core fix, gramps61 — data integrity |
| 13744 | 6.0.0 | Empty dates saved in a format that doesn't round-trip | core fix, gramps61 — data integrity |
| 13864 | 6.0.1 | Dashboard crashes & locks family tree | core fix, gramps61 |
| 13865 | 6.0.1 | Dashboard: Number of Columns 20 / added gramplet issue | core fix, gramps61 |
| 13876 | 6.0.1 | Citation Tree view mode fails to delete citations | core fix, gramps61 |
| 13716 | 5.2.2 | Filter gramplets don't update the Type popup | core fix, gramps61 |
| 13205 | 5.2.0 | Merging citations triggers gramps.gen.errors exception | core fix, gramps61 |
| 13418 | 5.2.2 | Exception generating a LaTeX report | core fix, gramps61 |
| 13413 | 5.2.2 | Fan Chart Report font size inconsistent | core fix, gramps61 |
| 13268 | 5.2.2 | Notes editor: Undo scrambles content | core fix, gramps61 |

## B — Addon defects, Linux-confirmable (likely real fixes -> gramps60)
| ID | Ver | Summary | Disposition |
|---|---|---|---|
| 13920 | 6.0.3 | [FTV] TypeError: Pango.extents_to_pixels() | addon fix, gramps60 — rich desc |
| 13326 | 5.2.2 | Forms addon AttributeError | addon fix, gramps60 — same teardown family as 13966/13059 |
| 13966 | 6.0.4 | Closing family tree -> Prerequisites Check error | RESOLVE addon-vs-core by repro; may be core |
| 13888 | 6.0.3 | [GenealogyTree] LaTeX report images referred wrong | addon fix, gramps60 |
| 13830 | 6.0.1 | [Graph View] "Show path to home person" broken | addon fix, gramps60 |
| 13589 | 6.0.5 | [Family sheet] extra page | addon fix, gramps60 |
| 14051 | 6.0.3 | DetailedDescendantBookReport AttributeError | RESOLVE addon-vs-core; report code may be core |
| 13979 | 6.0.5 | PostgreSQL Enhanced addon load error | addon fix, gramps60 |
| 13707 | 6.0.0-rc2 | Lib WebConnect install inconsistency | addon fix, gramps60 |
| 13694 | 6.0.0-rc1 | make.py lists addon with include_in_listing=False | addon/tooling fix, gramps60 |

## C — Addon-manager / isotammi cluster (verify shared root cause)
| ID | Ver | Summary | Disposition |
|---|---|---|---|
| 13906 | 6.0.3 | [Addon manager] Fails to update isotammi addons | cluster w/ 13174 — verify shared cause before treating as one |
| 13174 | 5.2.0-rc1 | [Addon manager] Fails to update isotammi addons | cluster w/ 13906 — likely same root |

## D — Other, lower confidence (repro-or-close -> gramps61 unless addon)
| ID | Ver | Summary | Disposition |
|---|---|---|---|
| 14014 | 6.0.5 | [Gramps web] date ranges error on import | repro-or-close; Gramps-Web interaction |
| 13832 | 6.0.1 | People created in Gramps-Web 6.0.1 not viewable | repro-or-close; Gramps-Web interaction |
| 13984 | 6.0.5 | Dashboard label wrong language after install | repro-or-close; localization/install-state |
| 13518 | 5.2.3 | [RCS Archive] Tree Manager can't rename archive | repro-or-close, gramps61 |
| 13406 | 5.2.3 | [Top Surnames Gramplet] quick view lastnames | repro-or-close, gramps61 |
| 13387 | 5.2.2 | 'Estimated' in Age Calculator contaminated | repro-or-close, gramps61 |
| 13270 | 5.2.1 | Tooltip on chart for living person | repro-or-close, gramps61 |

## E — Platform-specific -> MANUAL-VERIFICATION.md (cannot confirm on Linux)
| ID | Ver | Platform | Summary | Disposition |
|---|---|---|---|---|
| 14230 | 6.0.8 | macOS | Hosting Media on S3 / boto3 | MANUAL-VERIFICATION (macOS) |
| 13983 | 6.0.1 | macOS | No further editing after loading | MANUAL-VERIFICATION (macOS) |
| 13774 | 6.0.0 | macOS | Life Line Ancestor Chart addon install crash | MANUAL-VERIFICATION (macOS) |
| 13223 | 5.2.0 | macOS | Cannot install addon — failing prerequisite | MANUAL-VERIFICATION (macOS) |
| 13409 | 5.2.3 | Windows | AIO installer issue Win11 | MANUAL-VERIFICATION (Windows) |
| 13667 | 6.0.0-beta2 | Windows | AIO Addon Manager module install | MANUAL-VERIFICATION (Windows) — confirm still applies to 6.0.x release first (beta2 is old) |
| 13260 | 5.2.2 | Linux Mint | Can't load database backend | repro-or-close on Linux (this one IS Linux, not manual) |

## Triage checklist (do before launching Claude Code)
- [ ] STEP 0: scrape Mantis comment threads for all 38 (notes -> per-issue .md)
- [ ] Every issue has a filled TRIAGE VERDICT
- [ ] EXTERNAL/UPSTREAM issues removed or flagged
- [ ] addon-vs-core resolved (esp. 13966, 14051) by reproducing
- [ ] Each issue repros on example.gramps (no private data)
- [ ] Branch target confirmed per item (addons->gramps60, core->gramps61)
- [ ] Cluster hypothesis verified for 13906/13174 before treating as one fix

## Count
A: 12 core · B: 10 addon · C: 2 cluster · D: 7 repro-or-close · E: 7 platform/Linux-edge
= 38 issues

## Scrape list (38 IDs)
13819 14033 13747 13744 13864 13865 13876 13716 13205 13418 13413 13268
13920 13326 13966 13888 13830 13589 14051 13979 13707 13694
13906 13174
14014 13832 13984 13518 13406 13387 13270
14230 13983 13774 13223 13409 13667 13260
