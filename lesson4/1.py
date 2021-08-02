numbers = [1,23,1,2,4,5,6,6,7]
dict_of_numbers = {}
for i in numbers:
    if i not in dict_of_numbers:
        dict_of_numbers[i] = 1
    else:
        dict_of_numbers[i] += 1
for key, value in dict_of_numbers.items():
    if value == 1:
        print(f"{key} -- уникальное число")
    else:
        print(f"{key} -- не уникалено. Число встречается {value} раз(a).")

# print(dict_of_numbers)