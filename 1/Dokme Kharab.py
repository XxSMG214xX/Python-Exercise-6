def jaam(a,b):
    while b != 0:
        carryover = a & b
        a = a ^ b
        b = carryover << 1
    return a  
n = int(input())
m = int(input())
k = int(input())
jaam_n_m = jaam(n,m)
print(jaam_n_m)
if jaam_n_m == k :
    print('YES')
else :
    print('NO')
