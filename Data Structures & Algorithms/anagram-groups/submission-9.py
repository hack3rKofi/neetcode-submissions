class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        gp_anagram = {}

        for s in strs:

            key = ''.join(sorted(s))

            if key in gp_anagram: gp_anagram[key].append(s)

            else:
                gp_anagram[key] = [s]


        return gp_anagram.values()