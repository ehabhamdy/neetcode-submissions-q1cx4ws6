from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for n in counter:
            freq[counter[n]].append(n)

        print(freq)
        # freq [0, [1,2], [4,5]]

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res