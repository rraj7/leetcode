# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(s):
        ans = 0 
        sub = ''
        for i in s: 
            if i not in sub: 
                sub += i 
                ans = max(ans, len(sub))
            else: 
                l = sub.index(i)
                sub = sub[l+1:] + i
        return (ans, sub)

string = "pwwkeeeewwwdsdsfhhytyituyndcgnfyhjdgjfjnhfw"
ans = Solution 
print(ans.lengthOfLongestSubstring(string))