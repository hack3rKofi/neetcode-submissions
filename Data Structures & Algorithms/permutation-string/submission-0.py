class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = [0] * 26
        window_count = [0] * 26

        #build s1 count
        for char in s1:
            s1_count[ord(char)- ord('a')] += 1
        
        #initialize first window
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
        
        #Check if the first window is a match
        if s1_count == window_count:
            return True
        
        #Slide the window and check remaining positions
        for i in range(len(s1), len(s2)):

            #Add new characters to the window
            window_count[ord(s2[i]) - ord('a')] += 1

            #Remove character from the windows leftEnd
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_count == window_count:
                return True
        
        return False
        
