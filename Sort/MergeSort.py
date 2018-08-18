# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = None
        self.copy = None

    def InversePairs(self, data):
        # write code here
        self.data = data
        self.copy = data.copy()
        self.mergesort(0, len(data)-1)
        return self.data

    def mergesort(self, start, end):
        if start == end:
            return 0

        half = (end - start) // 2
        self.mergesort(start, start+half)
        self.mergesort(start+half+1, end)

        p = start+half
        q = end
        copy_index = end
        while p >= start and q >= start+half+1:
            if self.data[p] > self.data[q]:
                self.copy[copy_index] = self.data[p]
                p -= 1
            else:
                self.copy[copy_index] = self.data[q]
                q -= 1
            copy_index -= 1
        if p >= start:
            self.copy[start:copy_index+1] = self.data[start:p+1]
        if q >= start+half+1:
            self.copy[start:copy_index+1] = self.data[start+half+1:q+1]
        self.data[start:end+1] = self.copy[start:end+1]


if __name__ == "__main__":
    s = Solution()
    print(s.InversePairs([7,4,5,6]))