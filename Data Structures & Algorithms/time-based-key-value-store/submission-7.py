from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.memory = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memory[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        elementsForKey = self.memory[key]
        for e in elementsForKey:
            if e[1] == timestamp:
                return e[0]
        # res = elementsForKey[-1][0]
        for e in elementsForKey[::-1]:
            print(e)
            if e[1] <= timestamp:
                return e[0]
        return ""
