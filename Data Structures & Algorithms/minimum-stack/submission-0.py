class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        prevMin = float('inf') if not self.arr else self.arr[-1][1]
        self.arr.append((val, min(prevMin, val)))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
