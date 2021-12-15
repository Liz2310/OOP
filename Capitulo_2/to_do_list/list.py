
class ListItem:
    def __init__(self, text, due_date=None):
        """Set the text of To-Do item and its due date,
           if no due date is provided set to No due date"""

        self.text = text
        if due_date == "" or due_date == None:
            self.due_date = "No due date"
        else:
            self.due_date = due_date

class List:
    def __init__(self):
        """Dictionary to store To-Dos as keys and due dates as values"""
        self.to_do_items = {}

    def addNewItem(self, item, due_date=None):
        """Add To-Do and its due date to dictionary of all To-Dos"""

        new_item = ListItem(item, due_date)
        self.to_do_items[new_item.text] = new_item.due_date

    def deleteToDo(self, item):
        """Loop through key-value pairs in dictionary, if the item provided (item to delete) is
           the same as a key or value, delete from dictionary"""

        for k, v in self.to_do_items.items():
            if item == k:
                del self.to_do_items[item]
                print("To-Do deleted")
                return True
            elif item == v:
                del self.to_do_items[k]
                print("To-Do deleted")
                return True
            else:
                print("No such item in to-do list")
                return False

    def searchList(self, search):
        """Loop through key-value pairs in dictionary, if the search term is in key or
           its in value, print the key and value pair.

           If no matches were found, print No items found"""

        print("\nSearch Results: ")
        for k, v in self.to_do_items.items():
            if search in k:
                print(f"{k} for: {self.to_do_items[k]}")
                return True
            elif search in v:
                print(f"{k} for: {self.to_do_items[k]}")
                return True
            else:
                print("No items found")
                return False

    def modify_text(self):
        """Loop through key-value pairs in dictionary searching for the To-Do to delete.
           If found, change only the key and leave same value, then delete old key-value pair"""

        keyword = input("Enter To-Do you want to modify: ")
        for k,v in self.to_do_items.items():
            if k == keyword:
                change = input("Enter modification: ")
                self.to_do_items[change] = v
                del self.to_do_items[k]
                print("Change made")
                break


    def modify_dueDate(self):
        """Loop through key-value pairs in dictionary searching for the To-Do that
           belongs to the due date given. If found modify the value only, leave the key the same"""

        keyword = input("Enter To-Do that you want to modify its due-date: ")
        for k,v in self.to_do_items.items():
            if k == keyword:
                print(f"To-Do: {k} \nDue date: {v}")
                change = input("Enter new due-date: ")
                self.to_do_items[k] = change
                print("Change made")

    # IN THE MODIFY FUNCS FIGURE OUT HOW TO DISPLAY MULTIPLE TO-DOs AND HAVE USER CHOOSE WHICH ONE TO CHANGE
    # IN THE DELETE FUNC FIGURE OUT HOW TO SEARCH BY KEYWORD, DISPLAY ALL TO-DOs FOUND, HAVE THE USER CHOOSE WHICH ONE(S) TO DELETE

if __name__ == "__main__":
    x = ListItem("lol","feb 24")



