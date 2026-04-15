from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams should have the same number of chars
        # or anagrams should have the same frequency of the letters in it
        
        anagrams = defaultdict(list)

        # for each s in strs, generate a key which is a array/tube of 26 position holds the frequency of each letter
        # then added it to the anagrams dictionary, that way you collect anagrams under the same key

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1

            anagrams[tuple(key)].append(s)

        return list(anagrams.values())