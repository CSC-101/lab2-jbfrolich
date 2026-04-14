# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("jfrolich@calpoly.edu")
print(message)


from typing import Optional             # gain access to the Optional[X] type hint


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# What is the value of words at this point? ["this", "is", "confusing", "code." "Avoid", "such."]
# What are the values of first and second at this point? Both are ["this", "is", "confusing", "code." "Avoid", "such."]
# What happened? Changes original list using append and both calls use same list
print()