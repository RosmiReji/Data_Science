x = [[1,2,3],
     [3,4,5],
     [4,5,6]]
y = [[3,5,6],
    [3,5,2],
    [1,4,1]]
result =[[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range (len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j] +y[i][j]
for r in result:
    print(r)


