import hashlib

class User:
    def __init__(self, username, password):
        """Create a new user object. The password
        will be encrypted before storing."""

        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""

        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""

        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""

        self.users = {}

    def add_user(self, username, password):
        """Check the two conditions (password length and previously existing users)
        before creating a new User instance and adding it to the dictionary"""

        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        """Raises the InvalidUsername and InvalidPassword exceptions if necessary.
        If not, it flags the user as logged in"""

        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

class Authorizor:
    """Maps permissions to users. Should not permit user access to a permission
    if they are not logged in, so they'll need a reference to a specific authenticator."""

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission that users
        can be added to (like test or change program).
        Allows us to create a new permission,
        unless it already exists, in which case an
        exception is raised."""

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set() # We use set instead of list for usernames, so that even if you grant a user permission more than once, the nature of sets means the user is only in the set once.
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user.
        Allows us to add a username to a permission, unless either
        the permission or the username doesn't yet exist."""

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """Checks whether a user has a specific permission or not. In order for them
        to be granted access, they have to be both logged into the authenticator and
        in the set of people who have been granted access to that privilege. If either
        of these conditions is unsatisfied, an exception is raised"""

        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

class AuthException(Exception):
    """Requires a username and has an optional user parameter.
    This second parameter should be an instance of the User class associated with that username."""

    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class PermissionError(Exception):
    """This new error doesn't require a username,
    so we'll make it extend Exception directly,
    instead of our custom AuthException"""

    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass


authenticator = Authenticator() #default authenticator instance to our module so that the client code can access it easily using auth.authenticator
authorizor = Authorizor(authenticator) #default authorizor to go with our default authenticator