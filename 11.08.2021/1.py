import random
import re

words = [str(i) for i in input().split()]
random.shuffle(words)
pattern = r"[A-Za-z]"

for i in words:
    if re.match(pattern, i):
        print(i)

