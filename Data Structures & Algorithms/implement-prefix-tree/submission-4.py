class TrieNode:
    def __init__(self, children=None, end=0):
        self.children = children if children else {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        parent = self.root

        for i, c in enumerate(word):
            if c not in parent.children:
                parent.children[c] = TrieNode()
                
            parent = parent.children[c]
        
        parent.end += 1

    def search(self, word: str) -> bool:
        current = self.root

        for c in word.lower():
            if c not in current.children:
                return False
            current = current.children[c]
    
        return current.end > 0

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix.lower():
            if c not in current.children:
                return False            
            current = current.children[c]

        return True

        
        