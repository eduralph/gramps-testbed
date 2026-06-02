Confirmed and fixed.

`ChatWithTreeClass._apply_css_styles` set hardcoded LIGHT pastel
background colours on each chat-bubble CSS class but never set a
foreground colour. The fg fell through to the active GTK theme's default —
black under a light theme (fine), white under a dark theme (light-on-light
text on the pastel bubbles, unreadable).

The pastel backgrounds are intentional message-type colour-coding (green =
user, blue = reply, yellow = tool-call, red = error), so the fix locks the
foreground to `color: black;` on each bubble class so it contrasts against
those specific pastels regardless of which GTK theme is active. The
colour-coding is preserved.

Pure CSS change inside the existing `_apply_css_styles` provider; no
Python logic touched.

Pull request:

https://github.com/gramps-project/addons-source/pull/924

Fixes #14143.
