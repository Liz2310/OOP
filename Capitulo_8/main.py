import pickle

"""In each case, we open the file using a with statement so 
that it is automatically closed. The file is first opened 
for writing and then a second time for reading, depending 
on whether we are storing or loading data."""

some_data = ["a list", "containing", 5, "values including another list",["inner", "list"]]

with open("pickled_list", 'wb') as file:
    """The dumps and loads functions behave much like their 
    file-like counterparts, except they return or accept 
    bytes instead of file-like objects. The dumps function 
    requires only one argument, the object to be stored, and 
    it returns a serialized bytes object. """

    pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
    """The loads function requires a bytes object and returns 
    the restored object. The 's' character in the method names 
    is short for string; it's a legacy name from ancient 
    versions of Python, where str objects were used instead of bytes."""

    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data
"""The assert statement at the end would raise an error if the 
newly loaded object was not equal to the original object. 
Equality does not imply that they are the same object. Indeed, 
if we print the id() of both objects, we would discover they 
are different. However, because they are both lists whose 
contents are equal, the two lists are also considered equal."""
