# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

array = [1,2,3,4,5,6,7]
k = 2

def ArrayRotation(array,k):
  sol = []
  temp1 = array[:-2]
  temp2 = array[-2:]
  for i in temp2:
    sol.append(i)
  for i in temp1: 
    sol.append(i)
  return sol

ans = ArrayRotation(array,k)
print(ans)