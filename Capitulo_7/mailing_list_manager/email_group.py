"""We'll need an object that somehow matches email addresses
with the groups they are in. """

from collections import defaultdict
from send_email import send_email

class MailingList:
    """Manage groups of e-mail addresses for sending e-mails.

    Since the values in our dictionary will always be collections
    of unique email addresses, we can store them in a set container.
    We can use defaultdict to ensure that there is always a set
    container available for each key"""

    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        """Allows us to collect all the email addresses in one or more
        groups. This can be done by converting the list of groups to
        a set"""

        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            """This method, of course, returns a tuple of key-value 
            pairs for each item in the dictionary. The values are 
            sets of strings representing the groups. We split these 
            into two variables named e and g, short for email and 
            groups. We add the email address to the set of return 
            values only if the passed-in groups intersect with the 
            email address groups. The g&groups syntax is a shortcut 
            for g.intersection(groups); the set class does this by 
            implementing the special __and__ method to call intersection."""
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        """Method to our MailingList class that sends messages to
        specific groups.

        This function relies on variable argument lists. As input,
        it takes a list of groups as variable arguments. It gets
        the list of emails for the specified groups and passes those
        as variable arguments into send_email, along with other
        arguments that were passed into this method."""

        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)


if __name__ == "__main__":
    m = MailingList()
    m.add_to_group("friend1@example.com", "friends")
    m.add_to_group("friend2@example.com", "friends")
    m.add_to_group("family1@example.com", "family")
    m.add_to_group("pro1@example.com", "professional")
    m.send_mailing("A Party", "Friends and family only: a party", "me@example.com", "friends",
                   "family", headers={"Reply-To": "me2@example.com"})


