n = 5
a = []
b = []
est = [['Harry',37.21], 
       ['Berry',37.21], 
       ['Tina',37.2], 
       ['Akriti',41], 
       ['Harsh',39]]


#print([[a, b] for k in int(est) for a, b in [zip(*k)]])

for i in range(n):
    a.append(est[i][0])
    b.append(est[i][1])
    
m = min(b)
print(a)
print(b)
print(min(b))

#name = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
name = input(str())
#score = [37.21, 37.21, 37.2, 41, 39]
score = input(int())
dic = {}
s  = list()
if score in dic:
    dic[score].append(name)
else:
    dic[score]=[name]

if score not in s:
    s.append(score)

m = min(s)
s.remove(m)
m1=min(s)
dic[m1].sort()
print(dic[m1])






       

    










