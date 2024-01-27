def binary(n) :
    number = ''
    while n > 1 :
        b = int(n%2)
        n = n / 2
        number = str(b) + number
    for i in range(32-len(number)):
        number = '0' + number
    return number
num1 = int(input())
num2 = int(input())
part1 = ''
part2 = ''
n = int(input())
bit1 = str(binary(num1))
bit2 = str(binary(num2))
guest_list = bit2 + bit1
guest = []
for j in range(n) :
    guest.append( int(input()))
for i in range(n) :
    if guest_list[63-guest[i]] == '1' :
        print('yes')
    else :
        print('no')
