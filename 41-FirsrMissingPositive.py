def MissingPositive(num):
    a = nums.sort()
    for i in range(len(a)):
        if a[i] >=0 and a[i] != 1:
            return 1 
        