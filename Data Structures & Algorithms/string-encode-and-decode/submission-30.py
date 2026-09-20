class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for word in strs:
            mystr += str(len(word)) + "#" + word
        
        return mystr

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0

        while l < len(s):
            r = l

            while s[r] != "#":
                r += 1
            
            substr = int(s[l:r])
            l = r + 1
            r = substr + l
            result.append(s[l:r])
            l = r
        
        return result