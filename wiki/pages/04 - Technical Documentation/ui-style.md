---
title: UI style
categories:
- Developers/Design
- Developers/General
managed: false
source: wiki-scrape
wiki_revid: 118068
wiki_fetched_at: '2026-05-30T18:18:43Z'
---

For developers working on the [UI](https://wikipedia.org/wiki/User_interface#User_interfaces_in_computing) (User interface), it is important to follow this guidelines to maintain consistency.

- Adhere to the [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/index.html) as much as possible. If you feel you have a need to deviate from these, make sure you can justify it. Include the justification with the proposed design and get buy in from the rest of the developers.
- Avoid using color to distinguish text. If you can, use a different mechanism. There are two issues:

1.  GTK allows the users to change their themes. You may be happy with your dark blue text that you've defined, but what about the person whose theme has a dark blue background? So far, the only widget that seems safe to use color is the [GtkTreeView](https://docs.gtk.org/gtk3/class.TreeView.html)
2.  Many users (particularly males) are color blind. What you can distinguish, others may not be able recognize.

- Gramps is designed to be usable (even if it may not look best) on 800x600 resolution displays. (This policy was last reviewed in [2016](https://sourceforge.net/p/gramps/mailman/message/35551768/))
- Go for consistency. If a concept is used elsewhere in the program to represent what you want to do, use that mechanism. As an example, if someone's birth date does not exist, and you want to use a christening date instead, put the date in italics. This is what the Person View does. Be consistent with that. The more consistent we are, the less confused the user gets.
- Don't go button crazy. Buttons should be reserved for functions routinely used by all users (like Add, Delete, Edit). More obscure and less frequently used items should be in menus (such as a right context menu). Think of Firefox - The "Go to home page" function is used all the time, so it is a button. The "Send Link" function is not frequently used, so it appears in the menus.
- Data editors (like the Edit Person or Edit Family dialogs) should be just that - Data Editors. They are for data entry, not for displaying interesting information. If you want to display related data that is not part of the entry, use a Quick Report in the right context menu.
- Help the user. If a button is not valid in the current context, set it insensitive. That way the user doesn't click on it and wonder why nothing happens.
- Data should be edited in one place, and one place only. Otherwise, we cannot keep consistency. If two dialogs are editing the same data, one will stomp on the other's data.
- Too many options confuse users and make the program more work to maintain. Consider alternatives before adding a new option. Adding options should be the last resort, not the first.
- In the UI, display actual data, not derived data. If people see derived data in the UI, they will expect to be able to edit it. Derived data should only be shown in reports.
- Remember that the majority of the users are probably novices without a lot of computer experience. Design things so that your Aunt Martha could use it. Advanced functions can be deferred to the right context menu.

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Design](wiki:Category:Developers/Design)
