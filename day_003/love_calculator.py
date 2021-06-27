print('Welcome to the True Love calculator.')
name1 = input('Enter the first name: ').lower()
name2 = input('Enter the second nuame: ').lower()
true = 0; love = 0
name = name1 + name2

for letter in name:
    if letter in ['t', 'r', 'u', 'e']:
        true += 1
for letter in name:
    if letter in ['l', 'o', 'v', 'e']:
        love += 1

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score > 40 and score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
