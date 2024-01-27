def binary(n) :
    return "{0:b}".format(int(n))
a=int(input())
b=int(input())
dif = 0
fin1 = ''
fin2 = ''
bin1 = str(binary(a))
bin2 = str(binary(b))
for i in range((1000)-len(bin1)) :
    fin1 = fin1 + '0'
fin1 = fin1 + bin1
for i in range((1000)-len(bin2)):
    fin2 = fin2 + '0'
fin2 = fin2 + bin2
for i in range(1000) :
    if fin1[i] != fin2[i] :
        dif = dif + 1
print(dif)

