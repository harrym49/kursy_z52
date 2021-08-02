
while True:
    number = input("Введите число ")
    try:
        float(number) / 1 == float(number)
        print("Число корректно. Начинаю проверку")
        break
    except ValueError:
        print("Вы ввели что-то другое. Введите число. Не хитрите!")
#
number = list(number)

dict_of_numbers = {"четных цифр": 0, "нечетных цифр": 0}

for i in number:
    try:
        if int(i)%2 == 0 and int(i) != 0:
            dict_of_numbers["четных цифр"] += 1
        elif int(i)%2 != 0 and int(i) != 0:
            dict_of_numbers["нечетных цифр"] += 1
        elif int(i) == 0:
            continue
    except ValueError:
        continue

print(dict_of_numbers)