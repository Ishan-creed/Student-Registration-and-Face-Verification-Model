def DigitsSum(n):
    L=[int(i) for i in str(n)]
    return sum(L)

def IsHarshad(L):
    for x in L:
        for y in x:
            if (y% DigitsSum(y)!=0):
                return False
    return True

m=int(input("Enter the value: "))
L=[]
for i in range(m):
    L1=[int(i) for i in input().split(",")]
    L.append(L1)
n=len(L[0])
flag=False
for i in range(m-1):
    for j in range(n-1):
        R=[]
        R1=L[i][j:j+2]
        R2=L[i+1][j:j+2]
        R.extend([R1,R2])
        if (IsHarshad(R)==True):
            flag=True
            print(*R[0],sep=",")
            print(*R[1],sep=",")

if (flag==False):
    print(-1)