class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
        
        count = [0]*26
        window = [0]*26

        base = ord('a')

        for i in range(n1):
            count[ord(s1[i]) - base] += 1
            window[ord(s2[i]) - base] += 1
        
        for i in range(n1, n2):
            if count == window:
                return True
            
            window[ord(s2[i]) - base] += 1
            window[ord(s2[i -n1]) - base] -= 1
        
        return count == window