class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        def getKey(word):
            chars = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                chars[index] += 1

            return tuple(chars)

        for word in strs:
            key = getKey(word)

            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]


        return hashmap.values()