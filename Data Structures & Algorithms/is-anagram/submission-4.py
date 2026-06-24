class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        anagrams = {}

        for c1, c2 in zip(s,t):
            anagrams[c1] = anagrams.get(c1,0) + 1
            anagrams[c2] = anagrams.get(c2,0) - 1

        for b in anagrams.values():
            if b != 0:
                return False

        return True