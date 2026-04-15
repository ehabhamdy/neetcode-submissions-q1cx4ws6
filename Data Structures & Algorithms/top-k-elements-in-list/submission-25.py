from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # {1: 1, 2: 2, 3: 3}

        buckets = [[] for i in range(len(nums)+1)]
        
        res = []
        for n,f in counter.items():
            buckets[f].append(n)

        print(buckets)
        for bucket in buckets[::-1]:
            for n in bucket:
                print(n)
                res.append(n)
                if len(res) == k:
                    return res
            print(res)

