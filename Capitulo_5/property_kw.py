class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name) #creates new attribute called name, to replace the direct name attribute (it sets this attribute to be a property)
                                          #property calls the two methods we just created whenever the value is accessed or changed.

# c = Color("#0000ff", "bright red")
# print(c.name)
# c.name = "red"
# print(c.name)
# c.name = "" #it sends an empty property value, and since this behavior is forbidden, it throws an exception


class Silly:

    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a sillyproperty")

s = Silly()
s.silly = "funny"
s.silly
del s.silly