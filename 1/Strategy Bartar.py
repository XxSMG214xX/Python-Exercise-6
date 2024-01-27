def isprime(n) :
    if n < 2 :
        return False 
    for i in range(2,int(n**0.5)+1) :
        if n % i == 0 :
            return False
    return True




a, b = [int(a) for a in input().split()]
totall = 0
if a == b :
    if isprime(a):
        print('main order - amount: 1')
        exit()
    else :
        print('main order - amount: 0')
        exit()
if a < b :
    order = True
else :
    order = False
    c = a
    a = b
    b = c
for j in range(a,(b+1)):
    if isprime(j) : totall += 1
if order == True :
    print('main order - amount: ' + str(totall))
else :
    print('reverse order - amount: ' + str(totall))        
    
