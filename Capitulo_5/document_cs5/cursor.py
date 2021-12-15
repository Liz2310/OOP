class Cursor:
    """In charge of search forward or backward for newline
    characters in the string and jump to them,
    and every possible movement action like
    move by words, move by sentences, Page Up, Page Down,
    end of line, beginning of white space, and others."""

    def __init__(self, document):
        """This class takes the document as an
        initialization parameter so the methods
        have access to the content of the document's
        character list.
        
        It then provides simple methods for moving 
        backward and forward, as before, and for 
        moving to the home and end positions.""" # que son las home y end positions?

        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        while (self.position < len(self.document.characters) and self.document.characters[self.position].character != "\n"):
            self.position += 1
