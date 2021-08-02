import re
string = "abc83 cde7 1 b 24"

a = re.sub(r'[a-z]', '', string)

buffer = ''

for i in a:
    if i != ' ':
        buffer += i
    else:
        buffer +=','
c = [i for i in buffer.split(',')]

print(list(filter(None, c)))

