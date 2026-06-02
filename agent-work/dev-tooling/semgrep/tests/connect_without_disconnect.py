# Semgrep test fixtures for gramps-connect-without-disconnect.
# Semgrep convention: lines that SHOULD match are marked with a ruleid comment;
# lines that should NOT match are marked todoruleid / left clean.
# Run:  semgrep --config gramps-connect-without-disconnect.yml tests/
#       semgrep --test tests/   (if using the ruleid/ok annotations)

# --- POSITIVE: connects, no disconnect in cleanup (the 13091/12031 shape) ---
class EditCitationLike:                      # mirrors a DbGUIElement subclass
    def __init__(self, dbstate):
        self.callman = dbstate
        # ruleid: gramps-connect-without-disconnect
        self.handler = self.callman.connect("citation-update", self._on_update)

    def _on_update(self, *args):
        return self.callman.database        # 13091: callman None post-disposal

    def _cleanup_callbacks(self):
        self.callman = None                 # nulls state but never disconnected handler

# --- NEGATIVE: connects AND disconnects in cleanup (the 13326 post-fix shape) ---
class GalleryTabFixed:
    def __init__(self, dbstate):
        self.dbstate = dbstate
        # ok: gramps-connect-without-disconnect
        self.hid = self.dbstate.connect("database-changed", self._cb)

    def _cb(self, *args):
        pass

    def _cleanup_callbacks(self):
        if self.dbstate.handler_is_connected(self.hid):
            self.dbstate.disconnect(self.hid)   # guarded disconnect — correct

# --- OUT OF SCOPE: mid-init access, no connect (14177) — rule MUST NOT flag (no connect) ---
class EditPrimaryLike:
    def __init__(self):
        raise ValueError("init fails before show() sets self.opened")
    # close_item reads self.opened which was never set — flow bug, not a connect bug.
