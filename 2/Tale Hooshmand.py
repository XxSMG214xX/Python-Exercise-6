def change_base(num,b) :
    number = ''
    while num :
        x = int(num % b)
        num = num // b
        number = str(x) + number
    return number



final_sum = 0
invalid = False

for i in range (10**10) :

    input_str = input()
    inputs = input_str.split()
    sum_devisor = 0
    n = int(inputs[0])
    b = int(inputs[1])
    if n == -1 and b == -1 :
        break
    if b < 2 or b > 9 :
        invalid = True
    for i in range (1,n+1) :
        if n % i == 0 :
            sum_devisor += i
    
    final_sum += int(change_base(sum_devisor,b))

if invalid == True : 
    print('invalid base!')
else :
    print(final_sum)
    

    
    


