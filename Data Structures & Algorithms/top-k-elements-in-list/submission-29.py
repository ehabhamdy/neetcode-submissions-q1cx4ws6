from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums)+1)]

        for n, f in counter.items():
            buckets[f].append(n)

        for bucket in buckets[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res
