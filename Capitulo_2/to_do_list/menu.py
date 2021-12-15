import sys
from list import List

class Menu:
    def __init__(self):
        """Dictionary with numbers as keys (the numbers represent the user's inout) and
           with functions names as values (functions that are to be invoked later on)"""

        self.toDoList = List()
        self.choices = {
            "1" : self.show_to_dos,
            "2" : self.add_to_do,
            "3" : self.remove_to_do,
            "4" : self.search,
            "5" : self.modify_text,
            "6" : self.modify_due_date,
            "7" : self.quit
        }

    def display_menu(self):
        """Displays message for the user to know what to input for desired action"""

        print(
            """
        To-Do List Menu
    
        1. Show all To-Dos
        2. Add To-Do
        3. Remove To-Do
        4. Search List
        5. Modify To-Do 
        6. Modify To-Do due date
        7. Quit
            """
        )

    def run(self):
        """Main program loop.

           Displays the menu.

           Takes the user's input, looks in the dictionary for the key-value pair,
           once found it invokes the function by parenthesizing.

           It finds the function as the value of the key, which is the number input of the user"""

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_to_dos(self):
        """Invokes the dictionary in the List class and displays its key-value pairs"""

        items = self.toDoList.to_do_items
        print("\nTo-Dos:")
        for k,v in items.items():
            print(f"{k} due for: {v}")


    def add_to_do(self):
        """Asks user to input To-Do details and invokes the function from List class
           that adds a key-value pair to dictionary of all To-Dos"""

        new_to_do = input("Enter new To-Do: ")
        new_due_date = input("Enter a due date (optional): ")
        self.toDoList.addNewItem(new_to_do,new_due_date)
        print("To-Do has been added!")

        # MIGHT BE NICE TO PLACE IN LOOP IN CASE THE USER WANTS TO KEEP ADDING TO-DOS W/O HAVING TO GO BACK TO MENU


    def remove_to_do(self):
        """Asks user to input the To-Do to delete (be it its text or its due date) and invokes the function from List class
           that deletes a key-value pair to dictionary of all To-Dos.

           Stays in a loop in case nothing was found to be deleted and gives the user the chance to keep trying"""

        toDo_to_delete = input("Enter the To-Do you wish to delete by text or by due date ")
        while self.toDoList.deleteToDo(toDo_to_delete) == False:
            ans = input("Want to keep searching? Y or N: ").upper()
            if ans == "Y":
                toDo_to_delete = input("Enter the To-Do you wish to delete by text or by due date ")
            elif ans == "N":
                break
            else:
                print("Not a valid input")

        # MIGHT BE NICE TO PLACE IN LOOP IN CASE THE USER WANTS TO KEEP DELETING TO-DOS W/O HAVING TO GO BACK TO MENU

    def search(self):
        """Asks the user for To-Do or due date (be it the whole thing or a keyword) and invokes
           the function from the List class that searches through all key-value pairs in dictionary.

           Stays in a loop in case nothing is found."""

        search = input("Enter a keyword or letter to search To-Do or enter a due date: ")
        while self.toDoList.searchList(search) == False:
            ans = input("Want to keep searching? Y or N: ").upper()
            if ans == "Y":
                search = input("Enter a keyword or letter to search To-Do or enter a due date: ")
            elif ans == "N":
                break
            else:
                print("Not a valid input")

    def modify_text(self):
        """Invokes the function from the List class that modifies a To-Do's text"""

        self.toDoList.modify_text()

    def modify_due_date(self):
        """Invokes the function from the List class that modifies a To-Do's due-date"""

        self.toDoList.modify_dueDate()

    def quit(self):
        """Exits the program"""

        print("GoodBye Bishhhhh")
        sys.exit()

if __name__ == "__main__":
    Menu().run()
