n=5
mat=[[0 for _ in range(n)] for _  in range(n)]
count=1
top=0
bottom=n-1
right=n-1
left=0
while top<=bottom and left<=right:
    for i in range(left,right+1):#top
        mat[top][i]=count
        count +=1
    top += 1
    for i in range(top,bottom+1):#right
        mat[i][right]=count
        count+=1
    right-=1
    for i in range(right,left-1,-1):#bottom
        mat[bottom][i]=count
        count+=1
    bottom-=1
    for i in range(bottom,top-1,-1):#left
        mat[i][left]=count
        count+=1
    left+=1
for r in mat:
    print(" ".join(str(x) for x in r))
