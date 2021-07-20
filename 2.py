my_dict = {'a': 400, 'b': 58700, 'c': -560, 'd': 'one', 'e': 20000, 'f': 2000, 'g': 400, 'i': 3.14}
new_list = []
k = ''
for i in my_dict.values():
    k = i
    try:
        if int(k)/1 == int(k):
            new_list.append(i)
    except ValueError:
        continue

new_list.sort(reverse=True)
print(new_list[:3])