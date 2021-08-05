calendar = ['22.3.2010', '31.6.2012', '04.5.2017']
def date(day : int, month: int, year: int):
    if (str(day)+'.'+str(month)+'.'+str(year)) in calendar:
        print(True)
    else:
        print(False)

date(22, 3, 2010)