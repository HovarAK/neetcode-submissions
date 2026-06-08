class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s)
        if length_s != len(t):
            return False

        map_for_s = dict()
        for char in s:
            if char not in map_for_s:
                map_for_s[char] = 1
            else:
                map_for_s[char] += 1

        map_for_t = dict()
        for char in t:
            if char not in map_for_t:
                map_for_t[char] = 1
            else:
                map_for_t[char] += 1

        if map_for_s == map_for_t:
            return True
        return False