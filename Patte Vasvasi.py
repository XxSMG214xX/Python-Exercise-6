import re

inp = input()

inp.strip()

inp = re.sub(r' +',' ' , inp)
inp = re.sub(r"\\n",'\n' , inp)

password = ''
inp = list(inp)
check = 0
final_pass = []

for i in inp :
    if i =='@' :
        final_pass.append('@')
        check +=1
    elif i == '#' and check > 0 :
        check -=1
    
    else :
        final_pass.append(i)

for item in final_pass :
    password += item


print('Formatted Text: ' + password)