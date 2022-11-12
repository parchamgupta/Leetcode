import bisect
class MedianFinder:

    def __init__(self):
        self.lst = []
        self.size = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.lst, num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            n1 = self.lst[(self.size // 2) - 1]
            n2 = self.lst[self.size // 2]
            return (n1 + n2) / 2
        else:
            return self.lst[self.size // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()