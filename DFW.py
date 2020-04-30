file  = open("nxdfwords.txt" ,"r+")
data = file.readlines()
fname = input("File Name?")
tfile = open(f'{fname}.txt' , 'r+')
lines = tfile.readlines();
a = []
for i in lines:
    thisline = i.split(" ");
    a.append(thisline)
c = []
for i in range(len(a)):
    for j in range(len(a[i])):
        c.append(a[i][j].rstrip())
d = []
for i in data:
    thisline = i.split(" ");
    d.append(thisline[0])
e = [x for x in d if x in c]
inds = []
for i in range(len(e)):
    inds.append(d.index(e[i]))

for i in range(len(inds)):
    print(data[inds[i]])

k = input()
file.close()
tfile.close()
