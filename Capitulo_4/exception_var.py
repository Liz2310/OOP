# try:
#     raise ValueError("This is an argument")
# except ValueError as e:
#     print("The exception arguments were", e.args)


import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error") #raises an exception, with "An error" as argument

except ValueError:
    print("Caught a ValueError")

except TypeError:
    print("Caught a TypeError")

except Exception as e:
    print("Caught some other error: %s" % ( e.__class__.__name__)) #accesing the exception's name attribute
    #print("The exception arguments were",e.args)

else:
    print("This code called if there is no exception")

finally:
    print("This cleanup code is always called")