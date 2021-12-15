class EvenOnly(list):
    """Class that adds items to a list only if they are even numbered integers.
       Extends the list built-in.
       Overrides the append method to check two conditions that ensure the item is an even integer."""

    def append(self, integer):
        """The two exception objects are constructed from the built-in TypeError and ValueError classes"""

        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")

        if integer % 2:
            raise ValueError("Only even numbers can be added")

        super().append(integer)


def funny_division(divider):
    try:
        return 100 / divider

    except ZeroDivisionError:
        return "Zero is not a good idea!"


def funny_division2(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider

    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


def funny_division3(divider):
    """Catching different exceptions and do different things with them"""
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider

    except ZeroDivisionError:
        return "Enter a number other than zero"

    except TypeError:
        return "Enter a numerical value"

    except ValueError:
        print("No, No, not 13!")
        raise #re-raises the ValueError error, so after outputting No, No, not 13!, it will raise the exception again (print the red message with 13 is an unlucky number as the message)



# for val in (0, "hello", 50.0, 13):
#     print("Testing {}:".format(val), end=" ")
#     print(funny_division2(val))


# e = EvenOnly()
# e.append(3)
# e.append("a string")


print(funny_division3(0))
print(funny_division3(50.0))
print(funny_division3("hello"))
print(funny_division3(13))
