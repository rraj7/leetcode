def Sortarrayay(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index],array[i]
    return array

    

def BubbleSort(array):
    for i in range(0,len(array)):
        for j in range(0,(len(array)-i-1)):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def InsertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j -=1
        array[j+1]= key
    return array

#Quick Sort
def partition(array, low, high):
    i = (low-1)
    
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i = i+1
            array[i],array[j] = array[j],array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def QuickSort(array,low, high):
    if low < high:
        array = partition(array, low, high)

        QuickSort(array,low, array-1)
        QuickSort(array,array+1,high)
    return array



def MergeSort(array):
    if len(array) > 1: 
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        left = MergeSort(left)
        right = MergeSort(right)

        array = []

        while len(left)>0 and len(right) >0:
            if left[0] <right[0]:
                array.append(left[0])
                right.pop(0)

            else: 
                array.append(right[0])
                right.pop(0)
            
        for i in left:
            array.append(i)
        for i in right:
            array.append(i)
    return array

        
#HEAP SORT



arrayay1 = [-1,-3,-2,3,9,5,-5]
arrayay2 = [9,8,7,6,5,4,3,2,1]

ans = MergeSort(arrayay)
print(ans)
