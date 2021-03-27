array = [1,2,3,4,5]
N = 2

def ArrayRotation(A,N):
  sol = []
  temp1 = A[:-2]
  temp2 = A[-2:]
  for i in temp2:
    sol.append(i)
  for i in temp1: 
    sol.append(i)
  return sol

ans = ArrayRotation(array,N)
print(ans)