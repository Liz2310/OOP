import abc

class LibraryItems(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def remove_from_inventory(self):
        pass

    @abc.abstractmethod
    def add_to_inventory(self):
        pass

    @abc.abstractmethod
    def register_checkout(self):
        pass

    @abc.abstractmethod
    def register_return(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is LibraryItems:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented

class Inventory:
    books = {}
    dvds = {}

class CheckoutRegistry:
    def __init__(self):
        self.name_and_phone_number = {}

    def update_registry(self, name, phone_number):
        self.name_and_phone_number[name] = phone_number

class Book(LibraryItems):
    def __init__(self, name):
        self.name = name

    def remove_from_inventory(self):
        Inventory.books.pop(self.name)

    def add_to_inventory(self):
        if self.name in Inventory.books:
            Inventory.books[self.name] += 1
        else:
            Inventory.books[self.name] = 1


    def register_checkout(self):
        pass

    def register_return(self):
        pass


book1 = Book("The Little Prince")
book2 = Book("The Alchemist")
book3 = Book("The Little Prince")

book1.add_to_inventory()
book2.add_to_inventory()
book3.add_to_inventory()

print(Inventory.books)


