from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        top = [[] for _ in range(len(nums)+1)]

        freq = Counter(nums)
        # {1: 1, 2:2, 3:3}

        for n, f in freq.items():
            top[f].append(n)


        res = []

        for i in range(len(top)-1, -1, -1):
            d = top[i]
            for n in d:
                res.append(n)
                if len(res) == k:
                    return res


        
        
