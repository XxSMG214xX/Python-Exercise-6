from math import factorial

n = int(input())
for i in range (n) :
    for j in range (i+1) :
        ans = factorial(i)//(factorial(i-j)*factorial(j))
        print(ans,end = ' ')
    print()
    