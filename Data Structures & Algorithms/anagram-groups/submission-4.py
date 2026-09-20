class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashset = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in hashset:
                hashset[key].append(word)
            
            else:
                hashset[key] = [word]
        
        return hashset.values()