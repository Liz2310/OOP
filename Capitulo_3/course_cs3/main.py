from grader import Grader
from lessons import  IntroToPython, Statistics

grader = Grader()
itp_id = grader.register(IntroToPython) # Given the IntroToPython class, we register it without instantiating it
stat_id = grader.register(Statistics)

grader.start_assignment("Liz", itp_id)

print("Liz's Lesson:", grader.get_lesson("Liz"))

print("Liz's check:", grader.check_assignment("Liz", "a = 1 ; b = 'hello'"))
# print("Liz's check:", grader.check_assignment("Liz", "a = 1 ; b = 'lmao'"))
print("Liz's other check:", grader.check_assignment("Liz", "a = 1\nb = 'hello'"))
# print("Liz's other check:", grader.check_assignment("Liz", "a = 1\nb = 'hello'"))

print(grader.assignment_summary("Liz"))

#######################################################################################
#
# grader.start_assignment("Liz", stat_id)
#
# print("Liz's Lesson:", grader.get_lesson("Liz"))
# print("Liz's check:", grader.check_assignment("Liz", "avg=5.25"))
# print("Liz's other check:", grader.check_assignment("Liz", "avg = statistics.mean([1, 5, 18, -3])"))
#
# print(grader.assignment_summary("Liz"))
