class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for word in strs:
            res += str(len(word))+'#'+word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        l = 0

        while l < len(s):
            r = l

            while s[r] != '#':
                r += 1
            
            sub_str = int(s[l:r])
            l = r + 1
            r = sub_str + l
            res.append(s[l:r])
            l = r
        
        return res