# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("jfrolich@calpoly.edu")
print(message)


def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # For which calls below is this statement evaluated? n > m
   else:
      return m


first = smallest(3, 2)  # What is the value of first? 2
second = smallest(2, 2)  # The value is 2 but it is not reasonable because 2 = 2
print()