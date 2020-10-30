import timeit

def SortArray(array):
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


array1 = [-1,-3,-2,3,9,5,-5]
array2 = [9,8,7,6,5,4,3,2,1]

ans = InsertionSort(array2)
#print(execution_time)

if __name__ == "__main__":
    import timeit
    print (timeit.timeit('InsertionSort()',setup = "from __main__ import InsertionSort"))
