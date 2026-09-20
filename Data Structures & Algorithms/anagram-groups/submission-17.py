class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for w in strs:
            key = "".join(sorted(w))

            if key in hashmap:
                hashmap[key].append(w)
            else:
                hashmap[key]=[w]
        
        return list(hashmap.values())