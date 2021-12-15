"""Automated grading system for programming assignments,
similar to that employed at Dataquest or Coursera.

Provides a simple class-based interface for course writers to
create their assignments and should give a useful error message
if it does not fulfill that interface."""

import abc

class Assignment(metaclass=abc.ABCMeta):
    """Abstract base class that defines the interface of an assignment"""

    @abc.abstractmethod
    def lesson(self,student):
        pass

    @abc.abstractmethod
    def check(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            # puts the properties and methods of candidate class (C) into a set
            # set()  constructor to make a set (collection which is both unordered and unindexed)
            # dir() returns all properties and methods (even built-in properties which are default for all object) of the specified object without the values

            if set(cls.__abstractmethods__) <= attrs:
                # checks if the methods in the abstract class (cls) have been supplied by the candidate class (C)

                return True

        return NotImplemented

class IntroToPython():
    # when using issubclass(IntroToPython, Assignment) it returns True because Intro provides all the methods (there's no need to explicitly extend the ABC)

    def lesson(self):
        return f"""
            Hello {self.student}. define two variables,
            an integer named a with value 1
            and a string named b with value 'hello'
        """

    def check(self, code):
        return code == "a = 1\nb = 'hello'"

class Statistics(Assignment):
    def lesson(self):
        return (
            "Good work so far, "
            + self.student
            + ". Now calculate the average of the numbers "
            + " 1, 5, 18, -3 and assign it to a variable named 'avg'"
        )

    def check(self, code):
        import statistics

        code = "import statistics\n" + code

        local_vars = {}
        global_vars = {}
        exec(code, global_vars, local_vars)
        # exec() executes the dynamically created program, which is either a string or a code object.

        return local_vars.get("avg") == statistics.mean([1, 5, 18, -3])

class AssignmentGrader:
    """Manages how many attempts the student has made
    at a given assignment.

    Uses composition instead of inheritance, to avoid
    having to explicitly extending the ABC (the ABC could
    inherit from AssignmentGrader)"""

    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1

        return result

    def lesson(self):
        return self.assignment.lesson()

if __name__ == "__main__":
    print(issubclass(IntroToPython,Assignment))
    print(issubclass(Statistics,Assignment))