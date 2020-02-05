import csv
print("Enter Name of FILE")
a = input()
f = open(a)
csv_f = csv.reader(f)
c1 = 0
for row in csv_f:
    c1 = c1+1
index = 0
arr = [[] for i in range(0,c1)]
f.seek(0)
for roww in csv_f:   
    for i in range(0,len(roww)):
        arr[index].append(roww[i])
    index = index + 1

while c1>0:
    for i in range(0,len(arr[0])):
        element = arr[0][i]
