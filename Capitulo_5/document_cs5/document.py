from cursor import Cursor
from character import Character

class Document:
    """Since strings aren't mutable we can't insert a character into
    it or remove one without creating a brand new string object.

    So instead we'll use a list of characters which we can modify at
    will. In addition, we'll need to know the current cursor position
    within the list, and should probably also store a filename for
    the document."""

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    @property
    def string(self):
        """to concatenate the characters so we can see the
        actual document contents"""
        return "".join((str(c) for c in self.characters))

    def insert(self, character):
        """check whether the character being passed in is
        a Character or a str. If it is a string, it is
        wrapped in a Character class so all objects in the
        list are Character objects.

        It is possible that someone using our code would want
        to use a class that is neither a Character nor a string,
        using duck typing. If the object has a character attribute,
        we assume it is a Character-like object. But if it does
        not, we assume it is a str-like object and wrap it in Character.
        This helps the program take advantage of duck typing as well
        as polymorphism; as long as an object has a character attribute,
        it can be used in the Document class."""

        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position,character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join(self.characters))


if __name__ == "__main__":
    doc = Document()
    doc.filename = "test_document"
    doc.insert('h')
    doc.insert('e')
    doc.insert('l')
    doc.insert('l')
    doc.insert('o')
    doc.insert('\n')
    doc.insert('w')
    doc.insert('o')
    doc.insert('r')
    doc.insert('l')
    doc.insert('d')
    doc.cursor.home()
    doc.insert("*")
    #print("".join(doc.characters))
    #print(doc.cursor.position)
    doc.cursor.home()
    #print(doc.cursor.position)
    #print(doc.string)
    #doc.save()

    d = Document()
    d.insert('h')
    d.insert('e')
    d.insert(Character('l', bold=True))
    d.insert(Character('l', bold=True))
    d.insert('o')
    d.insert('\n')
    d.insert(Character('w', italic=True))
    d.insert(Character('o', italic=True))
    d.insert(Character('r', underline=True))
    d.insert('l')
    d.insert('d')
    print(d.string)
    d.cursor.home()
    print(d.cursor.position)
    d.delete()
    d.insert('W')
    print(d.string)


