from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]

        freq = Counter(nums)

        for n, f in freq.items():
            buckets[f].append(n)
        
        res = []
        for bucket in buckets[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res