n=int(input())
for i in range(n):
    for j in range(n-2):
        if (i==0 and (j==0 or j==(n-2-1))):
            print(' ',end=' ')
        elif( (j==0 or j==(n-2-1)) or (i==0 or i==(n//2)) ) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  
