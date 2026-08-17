matrix=[[1,2],[2,3],[3,4]]
row=len(matrix)
col=len(matrix[0])
trans_matrix=[]
for i in range(col):
    trans_row=[]
    for j in range(row):
        trans_row.append(matrix[i][j])
    trans_matrix.append(trans_row)        