import re

n = int(input())
domain = []
duplicate = {}
for i in range(n) :
    email = str(input())
    if '@' in email :
        demo  = re.findall('[@][A-Za-z0-9.]+', email)
        if demo[0] not in duplicate :
            main = demo[0][1:]
            duplicate[main] = True
for j in sorted(duplicate) :
        print(j)
