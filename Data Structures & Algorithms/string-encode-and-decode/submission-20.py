class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for stri in strs:
            res += str(len(stri))+'#'+stri
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            sub_len = int(s[i:j])
            i = j + 1
            j = sub_len + i
            res.append(s[i:j])
            i = j
        
        return res