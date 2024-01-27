row = []
main_map =[]
n = int(input())


for i in range (n) :
    row.append('.')
for j in range(1000) :
    column = row.copy()
    main_map.append(column)

x=0
y=0
main_map[y][x] = '*'


for i in range(10**10) :
    move = input()
    if move == 'END' :
        break
    elif move == 'L' :
        if x-1 >= 0 :
            x = x - 1
        else :
            x = 0
    elif move == 'R' :
        if x + 1 < n :
            x = x+1
        else :
            x = n -1 
    elif move == 'B' :
        y = y + 1
    main_map[y][x] = '*'



while True:
    if row in main_map :
        main_map.pop(main_map.index(row))
    else:
        break



for i in range(len(main_map)) :
    for j in range(n) :
        print(main_map[i][j] , end= ' ')
    print()

if x != n-1 :
    print("There's no way out!")