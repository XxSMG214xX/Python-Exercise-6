class Person :
    def __init__(self,name,health , score) :
        self.health = health
        self.score = score
        self.name = name

class Card :
    def __init__(self ,damage):
        self.damage = damage

"""""
FOR FILE INPUTS


file_path = 'file_path.txt' 
data = []
with open(file_path, 'r') as file:
    for line in file:
        data.append(line)
try :
    line1 = data[0]
    line2 = data[1]
    line3 = data[2]
    line4 = data[3]
    line5 = data[4]
    line6 = data[5]
except :
    error = True
    print("Invalid Command.")
    exit()

error = False
n = line1
nparts = n.split()
if len(nparts) != 2 :
    error = True
    print("Invalid Command.")
    exit()
n1,n2 = n.split()
health = line2
healthparts = health.split()
try :
    h1 = int(healthparts[0])
    h2 = int(healthparts[1])
except :
    error = True
    print("Invalid Command.")
    exit()


d = line3
dparts= d.split()
td1 = dparts[0]
td2 = dparts[1]
td3 = dparts[2]
try :
    d1 = int(dparts[0])
    d2 = int(dparts[1])
    d3 = int(dparts[2])
except :
    error = True

round1 = line4
r1p1 , r1p2 = round1.split()
round2 = line5
r2p1 , r2p2  = round2.split()
round3 = line6
r3p1 , r3p2 = round3.split()
s1 = 0
s2 = 0

if error :
    print("Invalid Command.")
    exit()

    
FOR PANDAS INPUTS :


import pandas as pd

your_dataframe = pd.read_csv('file_path.txt', header=None, names=['line'])

try:
    line1 = your_dataframe.iloc[0, 0]
    line2 = your_dataframe.iloc[1, 0]
    line3 = your_dataframe.iloc[2, 0]
    line4 = your_dataframe.iloc[3, 0]
    line5 = your_dataframe.iloc[4, 0]
    line6 = your_dataframe.iloc[5, 0]
except IndexError:
    print("Invalid Command.")
    exit()

error = False
n = line1
nparts = n.split()
if len(nparts) != 2:
    error = True
    print("Invalid Command.")
    exit()
n1, n2 = nparts

health = line2
healthparts = health.split()
try:
    h1 = int(healthparts[0])
    h2 = int(healthparts[1])
except ValueError:
    error = True
    print("Invalid Command.")
    exit()

d = line3
dparts = d.split()
td1, td2, td3 = dparts
try:
    d1 = int(td1)
    d2 = int(td2)
    d3 = int(td3)
except ValueError:
    error = True

round1 = line4
r1p1, r1p2 = round1.split()
round2 = line5
r2p1, r2p2 = round2.split()
round3 = line6
r3p1, r3p2 = round3.split()
s1 = 0
s2 = 0

if error:
    print("Invalid Command.")
    exit()


"""

error = False
n = input()
nparts = n.split()
if len(nparts) != 2 :
    error = True
    print("Invalid Command.")
    exit()
n1,n2 = n.split()
health = input()
healthparts = health.split()
try :
    h1 = int(healthparts[0])
    h2 = int(healthparts[1])
except :
    error = True
    print("Invalid Command.")
    exit()


d = input()
dparts= d.split()
td1 = dparts[0]
td2 = dparts[1]
td3 = dparts[2]
try :
    d1 = int(dparts[0])
    d2 = int(dparts[1])
    d3 = int(dparts[2])
except :
    error = True

round1 = input()
r1p1 , r1p2 = round1.split()
round2 = input()
r2p1 , r2p2  = round2.split()
round3 = input()
r3p1 , r3p2 = round3.split()
s1 = 0
s2 = 0

if error :
    print("Invalid Command.")
    exit()

    
A = Card(d1)
B = Card(d2)
C = Card(d3)


    

if r1p1 == "A" :
    r1p1 = A
if r1p1 == "B" :
    r1p1 = B
if r1p1 == "C" :
    r1p1 = C 


if r1p2 == "A" :
    r1p2 = A
if r1p2 == "B" :
    r1p2 = B
if r1p2 == "C" :
    r1p2 = C 


if r2p1 == "A" :
    r2p1 = A
if r2p1 == "B" :
    r2p1 = B
if r2p1 == "C" :
    r2p1 = C 


if r2p2 == "A" :
    r2p2 = A
if r2p2 == "B" :
    r2p2 = B
if r2p2 == "C" :
    r2p2 = C 


if r3p1 == "A" :
    r3p1 = A
if r3p1 == "B" :
    r3p1 = B
if r3p1 == "C" :
    r3p1 = C


if r3p2 == "A" :
    r3p2 = A
if r3p2 == "B" :
    r3p2 = B
if r3p2 == "C" :
    r3p2 = C  

p1 = Person(n1,h1,s1)
p2 = Person(n2,h2,s2)

p1.health -= r1p2.damage
p2.health -= r1p1.damage
if r1p1.damage > r1p2.damage :
    p1.score += 1
if r1p1.damage < r1p2.damage :
    p2.score += 1


p1.health -= r2p2.damage
p2.health -= r2p1.damage
if r2p1.damage > r2p2.damage :
    p1.score += 1
if r2p1.damage < r2p2.damage :
    p2.score += 1

p1.health -= r3p2.damage
p2.health -= r3p1.damage
if r3p1.damage > r3p2.damage :
    p1.score += 1
if r3p1.damage < r3p2.damage :
    p2.score += 1

print(f'{p1.name} -> Score: {p1.score}, Health: {p1.health}')
print(f'{p2.name} -> Score: {p2.score}, Health: {p2.health}')

"""
WRITING OUTPUT IN A FILE:


output_file_path = 'result.txt'
with open(output_file_path, 'a') as file:
    file.write(f'{p1.name} -> Score: {p1.score}, Health: {p1.health}\n')
    file.write(f'{p2.name} -> Score: {p2.score}, Health: {p2.health}\n')
"""

"""
DRAWING THE PLOT:

import matplotlib.pyplot as plt
x = [p1.name , p2.name]
y = [p1.score , p2.score]
plt.xlabel("Player Name")
plt.ylabel("Player Score")
plt.title('Resault Plot')
bar_colors = ['red' , 'blue']
plt.bar(x,y, color = bar_colors)
plt.show()
"""