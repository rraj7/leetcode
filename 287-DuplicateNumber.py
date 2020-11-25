""" 287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Input: nums = [1,3,4,2,2]
Output: 2


Input: nums = [3,1,3,4,2]
Output: 3 """

#Solution 1 : Brute Force T--> O(n**2) S --> O(1) 

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] == nums[j]:
                    return nums[i]

#Solution 2: Sort T--> O(nlogn) S --> O(n) 

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        for i in range(0, len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]


#Solution 3: Set T--> O(n) S --> O(n)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = set ()
        
        for i in nums:
            if i in val:
                return i
            val.add(i)
        
        
