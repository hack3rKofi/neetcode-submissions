class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Returns True if s2 contains a permutation of s1.
        Time Complexity: 0(n) where n is the length of s2.
        Space Complexity: 0(1) because the frequency array size is constant(26).
        """

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # Standardize our counts using the alphabet size
        s1_counts = [0] * 26
        window_counts = [0] * 26

        # Pre-calculate the ASCII value of 'a' for cleaner indexing
        base = ord('a')

        for i in range(n1):
            s1_counts[ord(s1[i]) - base] += 1
            window_counts[ord(s2[i]) - base] += 1
        
        # 2. Start the sliding window from the first possible move.
        # We check for a match *before* we slide and *after* every shift.

        for i in range(n1, n2):
            if s1_counts == window_counts:
                return True
            
            # Slide: And the character at index i, remove the character at the index i - n1
            window_counts[ord(s2[i]) - base] += 1
            window_counts[ord(s2[i-n1]) - base] -= 1
        
        # Final check for the last window position
        return s1_counts == window_counts