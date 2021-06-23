bill = float(input('How much cost the bill: '))
tip = int(input('How much tip will be paid: '))
people = float(input('How many people will pay the bill: '))

payment = (bill * (1 + tip / 100)) / people

print(f'Each one will pay ${payment:.2f}')
