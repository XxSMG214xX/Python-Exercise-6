import math



def sum_n(list):
    sum_t=0
    for elm in list :
        sum_t+= int(elm)
    return sum_t

def average(list):
    sum_t = 0
    n = 0
    for elm in list :
        sum_t += float(elm)
        n +=1
    avg = (sum_t) / (n)
    rounded_avg = round(avg, 2)
    return rounded_avg

def gcd_two (a,b):
    while b!= 0:
        a, b = int(b), int(a)% int(b)
    return a



def gcd(list):
    result = list[0]
    
    for num in list[1:]:
        result = gcd_two(result, abs(int(num)))

    return result


def lcd(list) :

    resault = abs(int(list[0]))

    for num in list[1:] :
        resault = (resault * abs(int(num)) ) // (gcd_two(resault,abs(int(num))))
    
    return resault

func = input()
if func != 'sum' and func != 'average' and func != 'gcd' and func != 'lcd' and func != 'min' and func != 'max' :
    print('Invalid command')
    exit()

numbers = []
for i in range (10**10) :
    inp = input()
    if inp == 'end' :
        break

    elif inp.isdigit :
        numbers.append(float(inp))
    else :
        numbers.append(inp)

if func == 'sum' :
    print(sum_n(numbers))
    
elif func == 'average' :
    print(average(numbers))
elif func == 'gcd' :
    print(gcd(numbers))
elif func == 'lcd' : 
    print(lcd(numbers))
elif func == 'min' :
    print(int(min(numbers)))
elif func == 'max' :
    print(int(max(numbers)))