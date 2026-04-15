class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join([c.lower() for c in s if c.isalpha() or c.isnumeric()])

        # if len(ns) == 1:
        #     return False 

        i, j = 0, len(ns)-1

        print(ns)
        while i <= j:
            if ns[i] != ns[j]:
                print(i)
                print(j)
                return False
            
            i += 1
            j -= 1 

        return True