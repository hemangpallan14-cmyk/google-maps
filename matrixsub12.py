matrix1=[[1,2],[2,3]]
matrix2=[[2,4],[5,6]]
r1=2,c1=2
r2,c2=2,2
if r1==r2 and c1==c2:
    print("sub posiible")
result=[]
for i in range (r1):
    row=[]
    for j in range (c1):
        row.append(abs(matrix1[i][j]-matrix2[i][j]))
        result.append(row)


