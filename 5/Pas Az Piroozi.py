def similar(n , s ,word) :
    words = s.split()
    s_w = []
    for i in words :
        word_1 = i
        
        first_word = word
        
        if len(word) > len(i) :
            word_1 += "_" * (len(word) - len(i))
        elif len(word) < len(i) :
            first_word += "_" * (len(i) - len(word) )
        
        d = sum (d1 != d2 for d1,d2 in zip(word_1 , first_word))
        if d <= n :
            s_w.append(i)
    return s_w

n = int(input())
s = input()
s = s.replace(':' , '')
s = s.replace('.' , '')
s = s.replace('،', '')
word = input()
res = similar(n,s,word)
for k in range (len(res)) :
    print(res[k])
        