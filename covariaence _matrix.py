data=[[1,2],[2,3],[4,5],[6,7]]
rows= len(data)
colums=len(data[0])
mean_a=0
mean_b=0

for i in range(rows):
    mean_a=mean_a+data[i][0]
    mean_b=mean_b+data[i][1]
mean_a=(mean_a)/rows    
mean_b=(mean_b)/rows
center=[]
for i in range (rows):
    a=data[i][0]-mean_a
    b=data[i][1]-mean_b
    center.append([a,b])
aa=0
bb=0    
ab=0
for i in range (rows):
    aa=aa+center[i][0]*center[i][0]
    bb=bb+center[i][1]*center[i][1]
    ab=ab+center[i][0]*center[i][1]
a1=(aa)/rows-1
b1=(bb)/rows-1
c1=(ab)/rows-1
covar_matrix=[[a,c1],[c1,b1]]
print(covar_matrix)