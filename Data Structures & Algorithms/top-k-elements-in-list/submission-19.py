from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        print(counter)
        for n, c in counter.items():
            print(c)
            freq[c].append(n)
        
        res = []
        for bucket in freq[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res


