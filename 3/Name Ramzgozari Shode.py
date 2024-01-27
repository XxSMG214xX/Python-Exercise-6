inp = input()
data = inp.split()
data_list = {}
for i in range(len(data)) :
    data_list[int(data[i][1:])] = data[i][0]
for key in sorted(data_list.keys()) :
    print(data_list[key], end='')