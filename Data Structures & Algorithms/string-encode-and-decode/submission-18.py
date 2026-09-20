class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for c in strs:
            res += str(len(c))+"#"+c
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            sub_length = int(s[i:j])
            i = j + 1
            j = sub_length + i
            res.append(s[i:j])
            i = j
        
        return res