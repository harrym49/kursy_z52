def is_year_leap(year):
    if (year %4 ==0) and (year %100 != 0) or (year % 400 == 0):
        print('leap year')
    else:
        print('regular year')

year = int(input('input year'))
is_year_leap(year)
