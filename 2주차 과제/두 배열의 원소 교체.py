n,k = map(int,input().split())
A = [int(x) for x in input().strip().split()]
B = [int(x) for x in input().strip().split()]
A.sort(reverse=True);    B.sort(reverse=True)
for i in range(1,k+1):
    A[-i] = B[i-1]
print(sum(A))