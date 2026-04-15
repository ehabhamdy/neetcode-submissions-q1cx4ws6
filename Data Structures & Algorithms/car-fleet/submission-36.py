class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for p, s in sorted(zip(position, speed), reverse=True):
            ttd = (target-p) / s
            if stack and stack[-1] >= ttd:
                continue
            
            stack.append(ttd)

        return len(stack)