## Root cause
`ChatWithTreeClass._apply_css_styles` (`ChatWithTree/ChatWithTree.py:169-198`)
sets hardcoded LIGHT background colours on each chat-bubble CSS class
(`.message-box`, `.user-message-box`, `.tree-reply-box`, `.error-reply-box`,
`.tree-toolcall-box`) plus `#chat-listbox { background-color: white; }`. No
foreground colour was set, so the fg fell through to the active GTK theme's
default — black under a light theme (fine) but white under a dark theme,
producing light-on-light text on the pastel bubbles. Unreadable.

## Fix
Add `color: black;` to each bubble class (and `#chat-listbox`). Pure CSS
change inside the existing CSS provider; no Python logic touched. An inline
comment explains why the foreground is locked rather than pulled from the
theme: the bubbles' pastel backgrounds are intentional message-type
colour-coding chosen against a white parent, so the safe fix is to lock the
fg to contrast against those specific pastels regardless of theme.

## Verified against
- `ChatWithTree/ChatWithTree.py:169-198` (`maintenance/gramps60`) — the
  only CSS provider in the addon; no other style entry-point depends on
  theme-derived colours.
- No prior contrast / dark-mode work in `git log upstream/maintenance/gramps60 -- ChatWithTree/`
  since the addon's introduction (`706a78fa3` Merge ChatWithTree gramplet
  addition #762).

## Test
No automated test. Contrast is a visual property; a regex-on-CSS-string
test would lock in the implementation and add no behavioural coverage
beyond `git diff`. **Manual visual verification required**: open Chat
With Tree under a dark GTK theme (e.g. Adwaita Dark) and confirm the
chat-bubble text is readable on each bubble class (default / user / reply /
error / tool-call) while the colour-coding remains distinguishable.

Fixes #14143.
