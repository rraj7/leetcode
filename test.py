def Solution(a,b,target):
    ans = a*b
    if (ans>target):
        return ans
    else: 
        sol = f'The value will be {a}'
        return sol


test = Solution(5,2,23)
print(test)