############DEBUGGING#####################

# Describe Problem
def my_function():
  for number in range(1, 21):
    if number == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
face = ["1", "2", "3", "4", "5", "6"]
number = randint(1, 6)
print(face[number - 1])

# Play Computer
year = int(input("What's your year of birth?: "))
if year > 1980 and year <= 1995:
  print("You are a millenial.")
elif year > 1996:
  print("You are a Gen Z.")
else:
  print("You are a Gen X.")

# Fix the Errors
age = int(input("How old are you?: "))
if age > 18:
  print(f"You can drive at age {age}.")

#Print is Your Friend
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(pages * word_per_page)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  return (b_list)

print(mutate([1,2,3,5,8,13]))
