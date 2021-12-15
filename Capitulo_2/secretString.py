class SecretString:
    """A not-at-all secure way to store a secret string."""

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only show the string if the pass_phrase is correct."""

        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""

secret_string = SecretString("ACME: Top Secret", "antwerp")
another_secret_string = SecretString("Lmao", "Lol")

#print(secret_string.decrypt("antwerp"))
#print(another_secret_string.decrypt("Lol"))

#print(secret_string.__plain_string) #cant acces the plain_string attribute withtout the passphrase
print(secret_string._SecretString__plain_string)#this way the string CAN be accesed

"""When we use a double underscore, the property is prefixed with _<classname>.
   When methods in the class internally access the variable, they are automatically unmangled. 
   When external classes wish to access it, they have to do the name mangling themselves. 
   So, name mangling does not guarantee privacy; it only strongly recommends it."""