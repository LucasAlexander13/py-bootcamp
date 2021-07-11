def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap(year):
        month_days[1] = 29
    
    month = month_days[month - 1]
    return month

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))

print(days_in_month(year, month))