# YMLDB
A file based, NoSQL database with atomic change rollbacks.

This library allows fast access to YML files to store structured data.

- Fast Search Functionality
- Schema Definition
- Type Validation
- Optionally uses `git` to store history.


## Object Locations

The location of object `d` stored in `a/b/c/d.yml` is referred to as `a.b.c.d`.

In the above example, `a.b.c` can also be an object, but the data is stored in `a/b/c/meta.yml`. Thus `meta` is a reserved object name.

## Fast finding

"Static Global" properties should be stored in the filename of the object. Then we can use a `glob` to quickly search for them.

- "Static" - This property is immutable.
- "Global" - All objects in the database should have this attribute.

## Schema

The database schema is stored in `.ymldb/schema/` and is also held in version control.
