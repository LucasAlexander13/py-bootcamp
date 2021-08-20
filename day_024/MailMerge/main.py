with open('./Input/Names/invited_names.txt', 'r') as file:
    name_list = []
    for name in file.readlines():
        name_list.append(name[:(len(name)-1)])
    file.close()    

with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()
    for name in name_list:
        invited = letter.replace('[name]', name)
        with open(f'./Output/ReadyToSend/letter_to_{name}.txt', 'w') as done:
            done.write(invited)
            done.close()
    file.close()
