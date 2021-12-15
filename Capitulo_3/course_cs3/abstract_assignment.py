"""Abstract base class that defines the interface of an assignment"""
import abc

class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self,student):
        pass

    @abc.abstractmethod
    def check(self):
        pass

    @classmethod
    def __subclassshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            # puts the properties and methods of candidate class (C) into a set
            # set()  constructor to make a set (collection which is both unordered and unindexed)
            # dir() returns all properties and methods (even built-in properties which are default for all object) of the specified object without the values
            if set(cls.__abstractmethods__) <= attrs:
                # checks if the methods in the abstract class (cls) have been supplied by the candidate class (C)
                return True

        return NotImplemented