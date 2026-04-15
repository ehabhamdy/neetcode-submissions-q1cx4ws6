from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a dictionary where the key represent 26 chars position 
        # of the english language mapped to an array of the word that matched the key
        #  for example the word 'aaa' will be mapped to the key (3 0 0 0 ....)

        anagrams = defaultdict(list)

        for s in strs:
            # frequencies = [0 for _ in range(26)]
            frequencies = [0] * 26
            for c in s:
                frequencies[ord(c) - ord('a')] += 1
            
            anagrams[tuple(frequencies)].append(s)

        return list(anagrams.values())