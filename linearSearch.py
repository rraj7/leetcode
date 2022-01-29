#create a program for a linear search 
# Linear Search is the only searching algo can be performed in an Unsorted List 

arr = [12,4,2,5,6,8,1]
target = 1

def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i] == target: 
            return i 
             
        else:
            return "Not found"

linearSearch(arr, target)