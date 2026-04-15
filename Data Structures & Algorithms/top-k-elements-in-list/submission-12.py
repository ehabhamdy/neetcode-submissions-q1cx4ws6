from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        top = [[] for _ in range(len(nums)+1)]

        freq = Counter(nums)
        # {1: 1, 2:2, 3:3}

        for n, f in freq.items():
            top[f].append(n)


        res = []

        for d in top[::-1]:
            for n in d:
                res.append(n)
                if len(res) == k:
                    return res


        
        
