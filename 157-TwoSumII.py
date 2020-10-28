#167. Two Sum II - Input array is sorted

""" Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Input: numbers = [2,3,4], target = 6
Output: [1,3]

"""
#Solution 1: brute force
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+ nums[j] ==target):
                    ans = [i+1,j+1];
        return ans

    
#Solution 2: Two Pointers

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        low = 0
        high = len(nums)-1
        
        while low<high:
            summation = nums[low]+nums[high]
            if summation == target: 
                return low+1,high+1
            elif summation > target: 
                high -=1
            else: 
                low +=1
                    

#Solution 3: Hash Map
        seen={}
        
        for i in range(len(numbers)):
            find = target-numbers[i]
            if numbers[i] not in seen:
                seen[numbers[i]]= i
            
            if find in seen and seen[find] !=i:
                return (seen[find]+1, i+1)