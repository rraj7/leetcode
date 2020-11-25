#Binary search program:: find the middle element in the sorted list and keep comparing. 
#Arr = sorted list , x = element
#low, high --> array size elements


#RECURSIVE METHOD 
def binary_search(arr, low, high, x):
    if high>=low:
        mid = (high+low)//2   #find the middle point
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr, low, mid -1, x)
        else: 
            return binary_search(arr,mid+1,high,x)
    else : 
        return -1;

arr = [10,20,30,40,50];
x = 10;

result = binary_search(arr,0,len(arr)-1,x)

if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 




#ITERATIVE METHOD 
class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0;
        high = len(arr)-1;
        
        while high>low: 
            mid = (high+low)//2;
            if arr[mid] ==target: 
                return mid;
            elif arr[mid]>target:
                high = mid-1;
            elif arr[mid]<target:
                low = mid +1;
            else :
                return mid
        return -1


def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1




'''
def BinarytoDecimal(n):
    if n >1: 
        BinarytoDecimal(n//2)
    print(n%2, end = "")


a = BinarytoDecimal(2309);
print(a)



var1 =1;
var2= 2;
var3 = "car"*2*3;

print (var1,var2,var3);


salary = 8000

def printSalary():
  salary = 12000
  print("Salary:", salary)
  
printSalary()
print("Salary:", salary)



listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)



for i in range(10, 15, 2):
  print( i, end=', ')

var= "James Bond"
print(var[2::-1])

'''

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))



class Node: 
    def __init__(self, value):
        self.val = val
        self.next = None

class myHashSet: 
    def __init__(self):
        self.head = None 
    

    def add(self,key):
        if not self.contains(key):
            node = Node(key)
            node.next = self.head
            self.head = node
    
    def remove(self,key):
        node = self.head

        if node and node.val == key:
            self.head = node.next 
            return None

        while node and node.next: 
            if node.next.val == key:
                node.next = node.next.next
                break 
        
    def contains(self, key):
        node = self.head
        while node: 
            if node.val == key:
                return True
            
            node = node.next
        return False 






nums = [1,0,1,1,1,0,1,1]






xx = 310


def reverse(x):
        
    if x> 0:
        x = str(x)
        ans = x[::-1]
        if ans[0] == 0: 
            ans =  ans[1:]
        
    elif x<0: 
        x = str(x)
        rev = x[1:]
        rev2 = rev[::-1]
        if rev2[0] == 0:
            return rev2[1:]
        
        ans = "-"+rev2
    return ans






arraya = [10,1234,1,12,13]

def findsmallest(arr):
    small = arr[0]
    
    for i in range(0, len(arr)): 
        
        #print(small)
        if small > arr[i]:
            small == arr[i]
    return small


smallest = findsmallest(arraya)
print(smallest)


import sys
array = 1

print(sys.getsizeof(array))


class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
if __name__== '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(123)

    ll.head.next= second;
    second.next = third;

    ll.printList()




array1 = [12,121,5,12,312]

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



answer = BubbleSort(array1)
print(answer)




array1 = [2,2,4,4,6,1]

def Unique(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return nums[i]


answer = Unique(array1)
print(answer)

graphlist = [1,3,4]
print(graphlist*2)