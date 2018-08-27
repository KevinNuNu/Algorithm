# -*- coding:utf-8 -*-
class MergeSort:
    def __init__(self, data):
        self.data = data
        self.copy = data.copy()

    def run(self):
        self.mergesort(0, len(self.data) - 1)
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
    # 归并排序
    s = MergeSort([1, 7, 4, 3, 10, 5, 6])
    print(s.run())
