class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Track the number of times a number occures within nums
        occurances = {}

        # Iterates through the list
        for n in nums:
            occurances[n] = occurances.get(n,0)+1

        # Sort the keys based on the values in the dictionary
        occurances = sorted(occurances.keys(),
                                key=lambda x: occurances[x],
                                reverse=True)
        
        return occurances[:k]