class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            anagram[sortedS] = anagram.get(sortedS, []) + [s]

        return list(anagram.values())