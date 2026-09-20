class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""

        for s in strs:
            mystr += str(len(s))+"#"+s
        
        return mystr

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0

        while l < len(s):
            r = l

            while s[r] != "#":
                r += 1
            
            sub_str = int(s[l:r])
            l = r + 1
            r = sub_str + l
            result.append(s[l:r])
            l = r
        
        return result