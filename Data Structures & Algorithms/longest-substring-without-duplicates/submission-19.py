class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        unique = set()

        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            
            unique.add(s[r])
            longest = max(longest, r-l+1)
        
        return longest