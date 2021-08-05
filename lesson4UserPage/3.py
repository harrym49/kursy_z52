numbers = [int(i) for i in input().split()]


a = sorted(numbers, key=str, reverse=True)
b = ''
for i in a:
    b += str(i)

print(b)