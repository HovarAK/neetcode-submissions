class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for s in strs:
            chars = [c for c in s]
            chars.sort()
            chars = tuple(chars)
            anagram[chars] = anagram.get(chars, []) + [s]

        return list(anagram.values())