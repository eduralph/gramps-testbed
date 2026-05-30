---
title: Signals and Callbacks
categories:
- Developers/General
- Developers/Tutorials
- GEPS
managed: false
source: wiki-scrape
wiki_revid: 109998
wiki_fetched_at: '2026-05-30T18:18:34Z'
---

The Gramps signaling system is used to pass changes in the db, GUI, or other sources to various elements (usually, the GUI) that need to be updated when changes occur.

Signals are emitted by the source, processed by the callback system and managers and result in callbacks to the GUI (or other) elements that have done a 'connect' to the callback manager for the signal of interest.

Signals from the db can indicate the types of db changes, such as an add, update or delete of one of the primary objects. Examples of these signals are 'person-add', 'media-update', 'citation-delete', 'note-rebuild'. This type of signal is emitted with a list of handles of the primary objects affected as arguments.

The GUI also emits signals when some user action changes the state; on a given view the 'active-changed' signal indicates that the selected object has changed. In addition, Gtk provides a rich set of signals for their widgets that use the separate (but similar) Gtk signal system.

## Callback

For the db and most of the GUI, the [callback.py](https://github.com/gramps-project/gramps/blob/master/gramps/gen/utils/callback.py) module with its Callback class provides much of the functionality. The Callback class is usually a base class for modules that emit and allow connection to callbacks, so its methods become part of the main class. An example is the class DbBsddbRead, or the displaystate.py History class. When emitting or connecting to a callback it is important to use the correct object in calling the method. If your code needs to see a 'databased-changed' and 'person-update' signals, for instance, you might use:

`       self.dbstate.connect('database-changed', self.db_changed)`  
`       self.db.connect('person-update', self.update)`

This presumes that your db could be located in self.db of course. If you wanted an 'active-changed' signal from the GUI, you would use the following:

`       history = self.uistate.get_history(nav_type, self.nav_group) # get history for current view`  
`       history.connect("active-changed", method)`

### Callback methods

`   emit(signal_name, args=tuple())`

which takes the 'signal-name' (type str) and emits it with the attached tuple of arguments. The args must be a tuple of arguments that match the types declared for the method that will be called during callback.

`   key = connect(signal_name, callback)`

which takes the 'signal-name' (type str) and the 'callback' (a method to execute)

Connect a callable to a signal_name. The callable will be called with the signal is emitted. The callable must accept the argument types declared in the signals callable method. The `connect` returns a unique 'key' that can be passed to the `disconnect` method.

`   disconnect(key)`

which takes the 'key' that was returned from the connect method, and uses it to disconnect the signal. It is important to disconnect from the signal when closing a GUI (or other) element.

There are additional methods in this module (read the code) to enable or disable logging of signals and a few lesser used functions.

### Callback example

An example usage of the Callback methods is to get an update of a person object, the db code will at some point do:

`       self.emit('person-update', ['987654321', '76ab38490', '548def987'])`

and in your code:

`       # in the initialization code`  
`       sel.key = self.db.connect('person-update', self.update)`  
  
`def update(self, handle_list):`  
`    for handle in handle_list:`  
`        # do something useful with the three handles`  
  
`# in close or cleanup code make sure to disconnect from db`  
`       self.db.disconnect(self.key)`

## Callman

There is also the callman.py which implements the CallbackManager class. This class serves to assist a signal user (typically a GUI element) in registering for callbacks on primary objects (Person, Place etc.) from the db. The CallbackManager acts as a filter, in that it will only pass on a signal to the GUI element if the element has registered for one or more handles it is interested in. This reduces the overhead of signals when there are a lot of GUI elements 'listening', they don't all have to update on every signal. It also assists in keeping track of callbacks so the cleanup process is a bit easier.

### Instantiating the CallbackManager

The Callback class is unique to a db and some GUI element. When instantiating the class, the current db is passed in:

`       self.callman = CallbackManager(database)`

When a db is changed, one should destroy the CallbackManager and set up a new one (or delete the GUI element as it shows info from a previous db).

### Registering callbacks with the CallbackManager

The CallbackManager allows the programmer to 'register' several callbacks at once:

`    callbackdict = {'person-delete': self.delete, 'media': self.rebuild}`  
`    register_callbacks(callbackdict)`

This function can be called several times, adding to and if needed overwriting, existing callbacks. No db connects are done at this point. If a signal already is connected to the db, it is removed from the connect list of the db. The callbackdict is a dictionary with key: value that is one of two types. The value is a function to be called when signal is raised.

If the key is a full signal name ('person-add', 'media-rebuild' etc.) the function is directly registered for that signal.

If the key is only one of the primary object types ('person', 'family', 'tag' etc.), then the function is registered for all of the available db transaction types ('add', 'delete', 'update', 'rebuild').

### Making connections with the CallbackManager

The CallbackManager actually makes the connections to the db when the following is executed, so this MUST follow the `register_callbacks` method in your code. The handles can be registered later on if desired.

`   connect_all(keys)`

This connects all database signals related to the primary objects given in 'keys' to the already registered callbacks. Note that only those callbacks registered with `register_callbacks` will effectively result in an action, so it is safe to connect to all keys even if not all keys have a registered callback. The parameter 'keys' is a list of keys of primary objects for which to connect the signals, with the default that no connects are done. One can enable signal activity to needed objects by passing a list, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr> `keys=['source', 'place]`, or to all with `keys=callman.KEYS` (which is a list of all the keys)

### Removing connections with the CallbackManager

`   disconnect_all()`

This disconnects the GUI element from all signals from the database. This method should always be called before the callback methods become invalid, that is, before closing the GUI element.

### Registering handles for callbacks

The CallbackManager allows the programmer to 'register' handles to be monitored in mass, according to the basic object class of each handle.

`   ahandledict = {'person': ['987654321', '76ab38490', '548def987'], 'media': ['357fed954']}`  
`   register_handles(ahandledict)`

This function registers handles that need to be tracked by the manager. This function can be called several times, adding to existing registered handles. The handledict parameter is a dictionary with key:value where the key is one of the primary object types ('person', 'family', 'tag' etc.), and the value is a list of handles to track.

The manager saves the registered handles in internal lists for each of the primary object types. When the underlying db signal is emitted, the handle is compared against the list to see if the actual callback to the GUI code needs to be done.

The following allows the programmer to register the handles found in a primary object:

`   register_obj(baseobj, directonly=False)`

When directonly is True, this method, will register all directly primary objects (their handles) connected to baseobj with the CallbackManager. So a person objects media, notes, attributes etc. will have their handles returned. If directonly is False, a recursive search is done through the primary objects that have references, and all other referenced handles will also be registered. Note that the handle for baseobj is not registered itself. Also note that objects that go through a reference object (like Event through EventRef) are not registered.

### Unregister handles with the CallbackManager

The following allows the programmer to stop monitoring handles. It uses the same ahandledict as `register_handles`:

`   unregister_handles(ahandledict)  # remove specific handles from registration.`  
`   unregister_all()  # allows removing all the registered handles from registration.`

### Connecting directly to db with the CallbackManager

`   add_db_signal(signal_name, callback)`

This does a custom db connect signal outside of the primary object ones managed automatically. It has the same arguments and function as the `Callback.connect` method. Its purpose in the CallbackManager is to allow the `disconnect_all` method manage this callback, so the user doesn't have to store a key and disconnect it individually.

## Db signals

The most commonly used signals from the db indicate the types of db changes, such as an add, update or delete of one of the primary objects. Currently, the primary objects are 'person', 'family', 'event', 'place', 'media', 'source', 'citation', 'repository', 'note', and 'tag'. The types of db signal that apply to these are 'add', 'delete', and 'update'. The signals are formed by appending the signal type to the primary object type with a '-' as in 'person-add'. Examples of these signals are 'person-add', 'media-update', 'note-delete'. This type of signal is emitted with a list of handles of the primary objects affected as arguments.

These signals are emitted when one or more commits occur at the end of a transaction. The signals are delayed until the end of the transaction so that they are not emitted if the transaction fails. Because the signals are delayed until after the all the transaction commits are actually complete, it is important for programmers to understand possible side effects.

For example, if a UI element made connections to both 'family-delete', and 'person-delete' and was trying to maintain a display of family related information, and further tried to be too smart about what it updated, it could 'see' apparent problems with the db. In the case of a family merge, it is possible that both the merged-in family and parents are deleted. If, when the 'person-delete' arrived, the UI element decided to update its family display, it might get an exception when it tried to access the family again. This was a real bug we had to correct.

To minimize likely side-effects, it was found that signals should be emitted by the db in a particular order; first are deletes, then adds, and finally updates. Within each type of commit, the various object types are also emitted in order according to the object keys (persons, families, sources, events, media, places, repositories, notes, tags and citations). By doing this we maintain consistent ordering of signals, regardless of commit order, db type or other circumstances. This emit order is maintained during undo and redo as well.

In the family merge example above, it would be much better for the UI element to make connection to 'family-delete', 'family-update', and 'person-update'. If a parent (or child) was removed, the 'family-update' signal would allow a correct update. If either was changed, the 'person-update' signal would allow a correct update.

One other class of db signals are object rebuilds; 'person-rebuild', 'place-rebuild', etc. These are emitted without parameters when a significant change has occurred to the db state, typically after a batch operation like an import, db repair, or other mass modification of the db. Usually, only views need to connect to these, [Gramplets](wiki:Gramplets_development) and editors will get 'active-changed' from the view code. The `self.db.request_rebuild()` call can be used by tools which make mass changes to update the UI.

There are a few other signal from the db;

- 'home-person-changed', with no parameters
- 'person-groupname-rebuild', with the name and group as parameters

and some db related signals from **dbstate**

- 'no-database'
- 'database-changed' (with the new db)

For example `self.dbstate.connect('database-changed', self.db_changed)`

## Other sources of signals

The Config manager can emit changes to the config settings; it emits the config setting as the signal name. It has its own 'connect', 'disconnect' and 'emit' methods.

### uistate

The user interface **uistate** has the following signals available:

- 'nameformat-changed'
- 'grampletbar-close-changed'
- 'filter-name-changed'
- 'filters-changed' with class of objects as a parameter
- 'update-available' with addon_update_list as a parameter

### displaystate

The **displaystate** passes the following signals:

- 'mru-changed' with new mru when the user selects a new line in a view
- 'active-changed' with new handle when the user selects a new line in a view

### Plugin manager

The Plugin manager passes the following signals:

- 'plugins-reloaded'

### Gtk

The Gtk system has its own callback and signal system with very similar underlying concepts. Please see the <https://developer.gnome.org/gnome-devel-demos/stable/signals-callbacks.py.html.en> for more information.

### See also

- Gramps developer docs (Sphinx)
  - [gramps/gen/utils/callback](https://gramps-project.org/docs/gen/gen_utils.html#module-gramps.gen.utils.callback)
  - [Connect](https://gramps-project.org/docs/_modules/gramps/gen/utils/configmanager.html#ConfigManager.connect)
  - [Disconnect](https://gramps-project.org/docs/_modules/gramps/gen/utils/configmanager.html#ConfigManager.disconnect)
  - [Emit](https://gramps-project.org/docs/_modules/gramps/gen/utils/configmanager.html#ConfigManager.emit)

[Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category:Developers/General](wiki:Category:Developers/General) [Category:GEPS](wiki:Category:GEPS)
