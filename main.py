# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("jfrolich@calpoly.edu")
print(message)


def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # when a is the largest
   elif b > c:
      return b + c  # when b>c and a is not the largest
   else:
      return 2 * c  # when c is greater than or equal to c and a is not the largest


answer1 = function2(3, 2, 1)  # What is the value of answer1? 1
answer2 = function2(2, 3, 1)  # What is the value of answer2? 4
answer3 = function2(2, 1, 3)  # What is the value of answer3? 6
print()