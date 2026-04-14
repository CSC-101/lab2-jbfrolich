# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("jfrolich@calpoly.edu")
print(message)


from typing import Optional             # gain access to the Optional[X] type hint


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # For which call below is this statement evaluated? First
   elif len(L) > 1:  # and what are the values being added? 4 + 2 + 3
      result = len(L[0]) + len(L[1])  # For which call below is this statement evaluated? Third
   elif len(L) > 0:  # and what are the values being added? 7 + 4
      result = len(L[0])  # For which call below is this statement evaluated? None
   else:  # and what are the values being added? None
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()