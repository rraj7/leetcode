#Binary Search - Iterative T.C = O(n) S.C = O(1)
def BinarySearch (array, x):

    l = 0 
    r = len(array)-1

    while l<=r: 
        mid = (l+r)//2

        if array[mid] == x: 
            return mid
        elif array[mid] <x: 
            l = mid+1
        else: 
            r = mid-1
    return -1

arr = [20,30,40,53,56]
print(BinarySearch(arr,53))


#Binary Search - Recursive T.C = O(nlogn) S.C = O(1)

def Binary(array,l,r,x):
    l = 0 
    r = len(array)-1

    while l<=r: 
        mid = (l+r)//2 
    
        if array[mid] == x: 
            return mid
        elif array[mid] >x: 
            Binary(array,l,mid-1,x)
        else: 
            Binary(array,mid+1,r,x)
    return -1
        
n = len(arr)
#print(Binary(arr,1,len(arr)-1,53))



#Linear Search O(N) S.C = O(1)

def LinearSearch(array, x): 
    for i in range(1,len(array)):
        if array[i] == x:
            return i 


print(LinearSearch(arr,56))


#Interpolation Search T.C = O(N)
def InterpolationSearch(array, l, h, x):
    if (l<=h and x>=array[0] and x <=array[h] ):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))

        if array[pos] ==x: 
            return pos
        elif array[pos]> x:
            return InterpolationSearch(array,pos+1,hi,x)
        else: 
            return InterpolationSearch(array,l, pos-1,x)
    return -1


