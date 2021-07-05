from art_variables import banana

name = input('Enter your full name: ').split()

first_name = name[0]
last_name = name[-1]

name = (first_name + ' Banana ' + last_name).title()

print(banana)
print(f'Welcome {name}!')
