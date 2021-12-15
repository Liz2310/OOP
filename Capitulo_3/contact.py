class ContactList(list):
    """Class that extends the built-in list data type"""

    def search(self, name):
        """Return all contacts that contain the search value
        in their name."""

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    """The Contact class is responsible for maintaining a list of all contacts in a class variable, and
       for initializing the name and address for an individual contact."""


    all_contacts = ContactList()
    """The all_contacts list, because it is part of the class definition, is shared by all instances of this class. 
       This means that there is only one Contact.all_contacts list. Example of class variables (notice the lack of 'self.')"""

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    """Acts like our Contact class, but has an additional order method.
       This way we can contact suppliers only to order, not accidentally contact customers or any other type of costumer.

       Can do everything a contact can do (including adding itself to the list of all_contacts) and all
       the special things it needs to handle as a supplier."""

    def order(self, order):
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )

class MailSender:
    """Adds functionality to our Contact class that allows sending an email to self.email.
       Sending email is a common task that we might want to use on many other classes.
       So, we can write a simple mixin class to do the emailing.

       Doesn't do anything special but it does allow to define a new class that describes
       both a Contact and a MailSender, using multiple inheritance"""


    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    """Class that inherits from two classes (Multiple inheritance).
       The Contact initializer still adds the new contact to the all_contacts list.
       And the mixin is able to send mail to self.email"""

    pass

class AddressHolder:
    """since a friend can have an Address class, we can argue that a Friend class is an AddressHolder class"""
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    """Invokes attributes (in the initializer) of parent class Contact and adds one of its own.

       The tricky part is that we now have two parent __init__ methods, both of which need to be initialized.
       And they need to be initialized with different arguments. That is where super() comes in, but
       how can we manage different sets of arguments when using super? """

    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


#c = Contact("Some Body", "somebody@example.net")
#s = Supplier("Sup Plier", "supplier@example.net")
# print(c.name, c.email, s.name, s.email)
# c.order("I need pliers") gives error cuz Contact has no order method
# s.order("I need pliers") doesn't give error cuz Supplier has order method
# print(c.all_contacts)

#c1 = Contact("John A", "johna@example.net")
#c2 = Contact("John B", "johnb@example.net")
#c3 = Contact("Jenna C", "jennac@example.net")
#print([c.name for c in Contact.all_contacts.search('John')])

#testing the mixin
# e = EmailableContact("John Smith", "jsmith@example.net")
# print(Contact.all_contacts)
# print(e.send_mail("Hello, test e-mail here"))