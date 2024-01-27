inp = str(input())
inp_list = inp.split()
n = int(input())
dict_inp ={}
ans = []
for i in range(len(inp_list)) : 
    if str(n- int(inp_list[i])) in dict_inp :
        ans.append(i + dict_inp[str((n-int(inp_list[i])))])
    dict_inp[inp_list[i]] = i
ans.sort()
if len(ans) == 0 :
    print('Not Found!')
else :
    for item in ans :
        print(item)



