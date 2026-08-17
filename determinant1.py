def determinant(a):
    n=len(a)
    if n==1:
        return a[0][0]
    if n==2:
        return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    ans=0
    for col in range(n):
        minor=[]
        for row in range(1,n):
            minor_row=[]
            for j in range(n):
                if j!=col:
                    minor_row.append(a[row][j])
            minor.append(minor_row)
            val=a[0][col]*determinant(minor)
            if col%2==0:
                ans=ans+val
            else:
                ans=ans-val


