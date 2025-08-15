def sum(a):
    res = 0
    for i in range(len(a)):
        res+= a[i]
    return res

x = int(input())
y = int(input())
z = int(input())
n = int(input())
posisble_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
res_list = []
# print(posisble_list)
for i in range(len(posisble_list)):
    res = sum(posisble_list[i])
    if(res != n):
        res_list.append(posisble_list[i])

print(res_list)