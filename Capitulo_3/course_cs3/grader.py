from lessons import Assignment, AssignmentGrader
import uuid


class Grader:
    """Manages which assignments are available and which one
    each student is currently working on."""

    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        #assignment_class is an actual class, not an instance of a class.
        #for example, the IntroToPython class is registered without instantiating it

        if not issubclass(assignment_class, Assignment):
            #check whether that class is a subclass of the ABC Assignment
            #since a __subclasshook__ method was used, this includes classes that don't explicitly extend the ABC

            raise RuntimeError("Your class does not have the right methods")
            # RuntimeError: Raised when an error is detected that doesn’t fall in any of the other categories.

        id = uuid.uuid4()
        # generate random identifier to represent that specific assignment
        # uuid returns a string called a universally unique identifier (extremely large number that is almost impossible to conflict with another similarly generated identifier)

        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        """Allows a student to start working on an assignment given the ID of
        said assignment.

        Constructs and instance of AssignmentGrader and put it in a dictionary
        stored on Grader"""

        self.student_graders[student] = AssignmentGrader(student, self.assignment_classes[id])

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        return assignment.lesson()

    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        """Gives summary of a student's current assignment progress.

        Looks up the assignment object and created a formatted string with all
        the info about that student."""

        grader = self.student_graders[student]

        return f"""
{student}'s attempts at {grader.assignment.__class__.__name__}:
        
attempts: {grader.attempts}
correct: {grader.correct_attempts}
passed: {grader.correct_attempts > 0}
        
"""

if __name__ == "__main__":
    grader = Grader()