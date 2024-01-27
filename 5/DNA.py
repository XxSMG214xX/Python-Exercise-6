class AghayeKharchang :
    def __init__(self,dna) :
        self.dna = dna
    def dna_mod(self) :
        self.dna = self.dna.replace('tt','o')
        return self.dna
class Octapus :
    def __init__(self,dna) :
        self.dna = dna
    def r_triplets(self) :
        new_dna = ""
        counter = 0
        j = 0
        i = 0        
        while i < len(self.dna):
            if self.dna[i] == 'x' and counter == 0 :
                counter += 1
                j = i
            while (i + 3 < len(self.dna)) and (self.dna[i] == self.dna[i + 1]) and (self.dna[i]==self.dna[i+2]):
                new_dna += "(0_0)"
                i+= 3
            else :
                new_dna += self.dna[i]
                i += 1
        if j != 0 :
            new_dna += str(j)
        return new_dna
class Bob_Esfanji :
    def __init__(self,dna) :
        self.dna = dna
    def merge_sort(self,arr) :
        if len(arr) > 1 :
            mid = len(arr)//2
            sub_array_r = arr[:mid]
            sub_array_l = arr[mid:]
            self.merge_sort(sub_array_l)
            self.merge_sort(sub_array_r)
            i = 0
            j = 0
            k = 0
            while i < len(sub_array_r) and j < len(sub_array_l) :
                if sub_array_r[i] < sub_array_l[j] :
                    arr[k] = sub_array_r[i]
                    i += 1
                else :
                    arr[k] = sub_array_l[j]
                    j += 1
                k += 1
            while i < len(sub_array_r) :
                arr[k] = sub_array_r[i]
                i += 1
                k += 1
            while j < len(sub_array_l) :
                arr[k] = sub_array_l[j]
                j += 1
                k += 1
        n = 100
        for kn in range(len(arr)) :
            n += int(arr[kn]) * (10**(len(arr) - kn -1))
        return n
    def sort_dna(self) :
        sorted_dna = self.merge_sort(self.dna)
        return sorted_dna

def main() :
    inp = input().strip()
    if inp.startswith("m") :
        aghaye_kharchang = AghayeKharchang(inp[1:] + inp[:10])
        print('m' + aghaye_kharchang.dna_mod())
    elif inp.startswith("sb") :
        bob_esfanji = Bob_Esfanji(list(str(len(inp))))
        print(bob_esfanji.sort_dna())
    elif inp.startswith("s") and not inp.startswith("sb") :
        octapus = Octapus(inp[0:])
        print(octapus.r_triplets())
    elif inp[len(inp) - 1] == 'm' :
        inp = inp[::-1]
        aghaye_kharchang = AghayeKharchang(inp[1:]+inp[:10])
        print('m' + aghaye_kharchang.dna_mod())
    elif(inp[len(inp)-1] == 's') and (inp[len(inp) - 2] == 'b') :
        inp = inp[::-1]
        bob_esfanji = Bob_Esfanji(list(str(len(inp))))
        print(bob_esfanji.sort_dna())
    elif(inp[len(inp)-1] == 's') and (inp[len(inp) - 2] != 'b'):
        inp = inp[::-1]
        octapus = Octapus(inp[0:])
        print(octapus.r_triplets())
    else :
        print('invalid input')
if __name__ == "__main__":
    main()
