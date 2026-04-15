from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for n, f in freq.items():
            buckets[f].append(n)

        res = []
        for b in buckets[::-1]:
            for n in b:
                if len(res) < k:
                    res.append(n)

        return res