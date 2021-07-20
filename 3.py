b = []
c = []
d = {}
e = []
with open('lorem.txt') as a:
    k = ''
    for i in a:
        for j in i:
            if j != ' ' and j != '.' and j != ',' and j != '' and j != '\n' and j != '-':
                k+=j
            else:
                b.append(k)
                k = ''
                continue

for i in b:
    if i == '':
        continue
    else:
        c.append(i)

b.clear()

b.append(c[0])

for i in c:
    if len(i) > len(b[0]):
         b[0] = i
    else:
        continue

for i in c:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key, value in d.items():
    e.append(value)
for key, value in d.items():
    if value == max(e):
        print(key)
    else:
        continue

print(b)