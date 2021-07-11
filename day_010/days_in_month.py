def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
        }
    
    if is_leap(year):
        month_days['February'] = 29
    
    month = month_days[month]
    return month

year = int(input('Enter a year: '))
month = input('Enter a month: ').title()

print(days_in_month(year, month))
