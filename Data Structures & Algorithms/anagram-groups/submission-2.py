class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        def getKey(string):
            chars = [0] * 26

            for char in string:
                index = ord(char) - ord('a')
                chars[index] += 1
            return tuple(chars)


        for word in strs:
            key = getKey(word)

            if key in hashmap:
                hashmap[key].append(word)
                

            else: hashmap[key]=[word]
        
        return hashmap.values()