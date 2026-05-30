---
title: Using database API
categories:
- Developers/General
- Developers/Tutorials
- Gramplets
- Plugins
- Reports
- Tools
- Views
managed: false
source: wiki-scrape
wiki_revid: 104773
wiki_fetched_at: '2026-05-30T18:18:45Z'
---

Explanation of the basics, underlying Gramps database. **This is not intended to be a reference manual**, but an introductory programmer's guide to using the Gramps database access routines.

Separate [API Reference Documentation for current version of Gramps](https://www.gramps-project.org/docs/) and as well as a simple [UML (svg) diagram for 4.1.x](wiki:Media:API.svg) and [Gramps Data Model](wiki:Gramps_Data_Model) overview are available.

Gramps is written in the [Python](http://www.python.org) language. A basic familiarity with Python is required before the database objects can be effectively used. If you are new to Python, you may wish to check out the [Python 2.x tutorial](https://docs.python.org/2/tutorial/) or [Python 3.x tutorial](https://docs.python.org/3/tutorial/).

## Database API

Access to the database is made through Python classes. Exactly what functionality you have is dependent on the properties of the database. For example, if you are accessing a read-only view, then you will only have access to a subset of the methods available.

At the root of any database interface is either DbReadBase and/or DbWriteBase. These define the methods to read and write to a database, respectively.

The SQLite database engine became an optional addon plugin for Gramps 5.0 and then replaced BSDDB as the default database backend in the 5.1 version. The BSDDB engine is expected to be retired from the standard install for 5.2 release of Gramps.

The full database hierarchy is:

- **DbGeneric** - general read and write implementations
  - **DbWriteBase** - virtual and implementation-independent methods for reading data ([gen/db/base.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db/base.py))
  - **DbReadBase** - virtual and implementation-independent methods for reading data ([gen/db/base.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db//base.py))

<!-- -->

- **DbBsddb** - read and write implementation to BSDDB databases ([gen/db/write.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db/write.py)) (The SQLite database became optional replaced BSDDB as the default database engine in the 5.1 version
  - **DbWriteBase** - virtual and implementation-independent methods for reading data ([gen/db/base.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db//base.py))
  - **DbBsddbRead** - read-only (accessors, getters) implementation to BSDDB databases ([gen/db/read.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db/read.py))
    - **DbReadBase** - virtual and implementation-independent methods for reading data ([gen/db/base.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db/base.py))
    - **Callback** - callback and signal functions ([gen/utils/callback.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/utils/callback.py))
  - **UpdateCallback** - callback functionality ([gen/updatecallback.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/updatecallback.py))
  - **DbTxn** - class for managing Gramps transactions and the undo database ([gen/db/txn.py](http://sourceforge.net/p/gramps/source/ci/master/tree/gramps/gen/db/txn.py))

### DB-API

The DB-API interface uses a generic interface backed with the general Python SQL implementation, called [DB-API](https://www.python.org/dev/peps/pep-0249/). The Gramps' generic interface (gramps.gen.db.generic.DbGeneric) has all of the logic for interacting with the database, except for the specific DB access code. Gramps' DB-API (gramps.plugins.db.dbapi.dbapi) implements the details so as to talk to conforming SQL databases. Other database engines could also implement the DbGeneric details, such as a nosql option.

By default, Gramps DB-API uses sqlite. However, you can also configure DB-API to use mysql, postgresql, and perhaps others.

To be compatible with BSDDB, DB-API stores Gramps data in an identical manner (pickled tuples). However, to allow for fast access, DB-API also stores "flat" data (such as strings and integers) in secondary SQL fields. These are indexed so that data can be selected without having to traverse, unpickle, initialize objects, and compare properties.

### DbBsddb

The DbBsddb interface defines a hierarchical database (non-relational) written in [PyBSDDB](http://www.jcea.es/programacion/pybsddb.htm). There is no such thing as a database schema, and the meaning of the data is defined in the Python classes above. The data is stored as pickled tuples and unserialized into the [primary data types (below)](wiki:Using_database_API#Primary_Objects).

### Using the Database

For most cases, Gramps will have already opened a database for you. This is often embedded in a DbState object. Thus, you might interface the database like:

`>>> dbstate.db.get_person_from_gramps_id("I0001")`

However, to do any database activity, you need to understand the primary objects.

## Primary Objects

Primary objects are the fundamental objects in the Gramps database. These objects are:

- [Person](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.person) - Contains the information specific to an individual person.
- [Family](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.family) - Contains the information specific to relationships between people. This typically contains one or two parents and zero or more children.
- [Event](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.event) - Contains the information related to an event.
- [Place](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.place) - Contains the information related to a specific place.
- [Repository](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.repo) - Contains the information related to a repository.
- [Source](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.src) - Contains the information related to a source of information.
- [Citation](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.citation) - Contains the information related to a citation into a source.
- [Media Object](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.mediaobj) - Contains the information related to a media object. This includes images, documents, or any other type of related files.
- [Note](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.note) - Contains the information related to a note.

Primary objects are treated as tables within the database. Individual components that compose the primary object are stored as individual items in the database.

### 1. Person:

1.  handle
2.  gramps_id
3.  gender
4.  primary_name
5.  alternate_names
6.  death_ref_index
7.  birth_ref_index
8.  event_ref_list
9.  family_list
10. parent_family_list
11. media_list
12. address_list
13. attribute_list
14. urls
15. lds_ord_list
16. citation_list
17. note_list
18. change
19. tag_list
20. private
21. person_ref_list

### 2. Family:

1.  handle
2.  gramps_id
3.  father_handle
4.  mother_handle
5.  child_ref_list
6.  the_type
7.  event_ref_list
8.  media_list
9.  attribute_list
10. lds_seal_list
11. citation_list
12. note_list
13. change
14. tag_list
15. private

### 3. Event:

1.  handle
2.  gramps_id
3.  type
4.  date
5.  description
6.  place
7.  citation_list
8.  note_list
9.  media_list
10. attribute_list
11. change
12. tag_list
13. private

### 4. Place:

1.  handle
2.  gramps_id
3.  title
4.  long (longitude)
5.  lat (latitude)
6.  placeref_list
7.  name
8.  alt_names
9.  place_type
10. code
11. alt_loc (deprecated)
12. media_list
13. citation_list
14. note_list
15. change
16. tag_list
17. private

### 5. Source:

1.  handle
2.  gramps_id
3.  title
4.  author
5.  pubinfo (publication information)
6.  note_list
7.  media_list
8.  abbrev (abbreviation)
9.  change
10. attribute_list
11. reporef_list
12. tag_list
13. private

### 6. Citation:

1.  handle
2.  gramps_id
3.  date
4.  page
5.  confidence
6.  source_handle
7.  note_list
8.  media_list
9.  attribute_list
10. change
11. tag_list
12. private

### 7. Media:

1.  handle
2.  gramps_id
3.  path
4.  mime
5.  desc (description)
6.  checksum
7.  attribute_list
8.  citation_list
9.  note_list
10. change
11. date
12. tag_list
13. private

### 8. Repository

1.  handle
2.  gramps_id
3.  type
4.  name
5.  note_list
6.  address_list
7.  urls
8.  change
9.  tag_list
10. private

### 9. Note

1.  handle
2.  gramps_id
3.  text
4.  format
5.  type
6.  change
7.  tag_list
8.  private

## Secondary Objects

In addition, there are a number of secondary objects. In the DbBsddb implementation, these are stored in the primary objects. Typically, this means that DbBsddb objects are stored in [pickled](https://docs.python.org/3.4/library/pickle.html) format. In the DbDjango implemetation, the secondary objects are additional tables.

The secondary objects include dates, addresses, and source references among other objects.

### 1. Name:

1.  privacy
2.  source_list
3.  note_list
4.  date
5.  first_name
6.  surname
7.  suffix
8.  title
9.  name_type
10. prefix
11. patronymic
12. group_as
13. sort_as
14. display_as
15. call

### 2. Date

### 3. Address

1.  privacy
2.  source_list
3.  note_list
4.  date
5.  location

### 4. LDS Ord

1.  source_list
2.  note_list
3.  date
4.  type
5.  place
6.  famc
7.  temple
8.  status
9.  private

## Handles

Each primary object has a unique handle associated with it. The handle serves as both a unique identifier and as the key into the database. This handle is generated using the current timestamp along with two 32-bit random numbers. The resulting value is converted to a text string to provide a hashable handle.

The handle can always be retrieved from a primary object using the `get_handle` function.

` handle = person.get_handle()`

All relationships between primary objects are in terms of the handle, instead of a reference to an object. This allows objects that are not currently being used to be stored on disk instead of in memory. This adds an additional step of fetching from the database to find related data. For example, to get the Person object marked as the father of a Family, the following must be done:

` # find father from a family`  
` father_handle = family.get_father_handle()`  
` father = database.get_person_from_handle(father_handle)`

For this reason, it is always necessary to have reference to the database that contains the objects with which you are working.

The handle should not be visible to the end user, and should not be included in reports or displayed on screen. Instead, the Gramps ID value should be used for this purpose. The Gramps ID is a user defined value for each object, but is not used internally to the database. This allows the user to change the Gramps ID without affecting the database.

Once created, the handle should never be modified.

#### See also

Discourse forum discussions:

- [Reversing an object handle to its creation date](https://gramps.discourse.group/t/reversing-an-object-handle-to-its-creation-date/2614)
- [Question about the Gramps Handle ID](https://gramps.discourse.group/t/question-about-the-gramps-handle-id/248)
- [Creation timestamp from a handle](https://gramps.discourse.group/t/reversing-an-object-handle-to-its-creation-date/2614/5) SuperTool script

[Line 53 : Creating a Handle](https://github.com/gramps-project/gramps/blob/master/gramps/gen/utils/id.py#L53) gramps/gen/utils/id.py source code

### Object lifetime

Care must be taken when working with primary objects. Each instance that is retrieved from the database is unique, and not connected to other instances. The example below exhibits the issue:

      # get two person objects using the same handle
      person1 = database.get_handle(handle)
      person2 = database.get_handle(handle)

      person1.set_nickname('Fred')

In this case, even though person1 and person2 represent the same person, they are distinct objects. Changing the nickname of person1 does not affect person2. The person2 object will retain the original nickname.

Changes to the object do not become permanent until the object has been committed to the database. If multiple instances exist in memory at the same time, care must be taken to make sure that data is not lost.

## Database Objects

Gramps provides a standard interface for all database objects. The Gramps database object provides the interface to the lower level database. Currently, only one database interface is supported:

- GrampsBSDDB - the default database, providing access to a Berkeley DB database.

### Transactions and Commits

In order to support an UNDO feature, the database has the concept of [Transactions](https://gramps-project.org/docs/gen/gen_db.html#module-gramps.gen.db.txn). Transactions are a group of related database commit operations that need treated as a single unit. If all related commits are not undone as a single unit, the database can be left in a corrupted state. The UNDO operation will undo all the commits in the transaction.

Transactions may be as small as a simple edit of a person or as complex as a GEDCOM import. The developer must decide what the appropriate level of abstraction is for an operation. The developer must also guarantee that the transaction encompasses the entire transaction, so that an undo operation does not leave the database in an inconsistent state.

An example of a transaction is shown below.

       # Create a new family and add the spouses
       # Assume that the father and mother already exist

       # begin transaction
       with DbTxn(_("Set Marker"), self.db, batch=True) as transaction

       # Create new family, add it to the database. The add_family
       # function will assign the handle

       family = Family()
       database.add_family(family,transaction)

       # Add the family to the father and mother
       father.add_family_handle(family.get_handle())
       mother.add_family_handle(family.get_handle())

       # Add parents to the family
       family.set_father_handle(father.get_handle())
       family.set_mother_handle(mother.get_handle())

       # Commit the changes to the father, mother, and family
       database.commit_person(father, transaction)
       database.commit_person(mother, transaction)
       database.commit_family(father, transaction)

### UNDO

Each commit operation associated with a transaction stores the previous value of the object in the database log file. The transaction keeps track to the start and stop commits in this list. Undoing the last transaction is as simple as:

`  database.undo()`

This operation pops the last transaction off the stack, and restores the previous values that were stored in the transaction log file.

### Iterating through the database

Frequently, it is useful to iterate through all the elements of a database. Gramps provides two ways of accomplishing this. The first method involves getting a list of all the handles and looping over the list. This method is the easiest to implement. An example is below:

`  for handle in database.get_person_handles():`  
`     person = database.get_person_from_handle(handle)`

A more efficient method exists, but is more complicated to use. The database can provide a [cursor](https://gramps-project.org/docs/gen/gen_db.html#module-gramps.gen.db.cursor) that will iterate through the database without having to load all handles into memory. The cursor returns a handle, data pair. The data represents the serialized data directly from the database. It is the users responsibility to unserialize the data. An example is below:

`  cursor = database.get_person_cursor()`  
`  pair = cursor.first()`  
`  while pair:`  
`     (handle,data) = pair`  
`     person = Person()`  
`     person.unserialize(data)`  
`     pair = cursor.next()`  
`  cursor.close()`

### Finding references

Primary objects can reference each other in two ways.

A primary object may reference another directly, for instance a Person object may link to a Source object that has information about where some information about the person came from. Finding all of the primary (or forward links) can be done like this:

      # get references directly from the primary object
      references = person.get_referenced_handles()

      # get all references from the primary object and 
      # all secondary objects that are linked to it.
      references = person.get_referenced_handles_recursively()

The second type of reference is an implicit backlink, this is the reverse of the forward-link above. To find all the backlinks for a primary object you have to ask the database to search all the primary objects to see which ones have a reference to the primary object you are looking for. You can do this by using the `find_backlink_handles()` method. e.g.

` for reference in db.find_backlink_handles(person.get_handle()):`  
`   reference_class_name, reference_handle = reference`  
`   if reference_class_name == 'Person':`  
`      person = db.get_person_from_handle(reference_handle)`

### Getting notification of changes to the database

If you have widgets that are displaying the content of the database tables you need to be aware that the database can change. Records may be added, removed or updated by other parts of Gramps and your widget must show these changes. The Gramps database provides a signalling mechanism that can be used to notify your widget of changes to the database. The documentation for the ((GrampsDBCallback)) class provides a description of the signalling mechanism. For most code that uses the Gramps database all that is required is for callback functions to be connected to the correct signals. For example:

`  database.connect('person-add',self.update_view)`  
`  database.connect('person-update',self.update_view)`  
`  database.connect('person-rebuild',self.update_view)`

A full list of the signals that are emitted from the database can be found at the top of the [`GrampsDbBase`](https://gramps-project.org/docs/gen/gen_db.html#module-gramps.gen.db.base) class in the [`gramps/gen/db/base.py`](https://github.com/gramps-project/gramps/blob/master/gramps/gen/db/base.py) module.

[Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category:Developers/General](wiki:Category:Developers/General) [A](wiki:Category:Reports) [A](wiki:Category:Plugins) [A](wiki:Category:Tools) [A](wiki:Category:Gramplets) [A](wiki:Category:Views)
