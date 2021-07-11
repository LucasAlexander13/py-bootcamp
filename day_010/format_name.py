def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f'{f_name} {l_name}'

print(format_name(input('Enter a name: '), input('Enter a last name: ')))
