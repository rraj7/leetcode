# Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Input: nums = [2,7,11,15], target = 9 ;Output: [0,1]
#
#

# First approach - Brute force TimeComp - O(n**2) Space : O(1)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+ nums[j] ==target):
                    ans = [i,j];
        
        return ans

#Second Approach - Hash Map Time = O(n) Spce O(n)
class Solution(object):
     def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, j in enumerate(nums):
            compliment = target - j
            if compliment in hash_table :
                return [hash_table[compliment],i]
            hash_table[j] = i
    
        return []
            
