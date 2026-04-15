from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # freq {1: 1, 2:2, 3: 3}
        print(freq)
        buckets = [[] for _ in range(len(nums)+1)]

        for n, f in freq.items():
            buckets[f].append(n)

        res = []
        for bucket in buckets[::-1]:
            print(bucket)
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res

        return res
