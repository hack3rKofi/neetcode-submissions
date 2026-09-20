class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            r = l

            while s[r] != "#":
                r += 1
            
            sub_str = int(s[l:r])
            l = r + 1
            r = l + sub_str
            res.append(s[l:r])
            l = r
        
        return res