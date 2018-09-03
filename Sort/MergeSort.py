# -*- coding:utf-8 -*-
class MergeSort:
    def __init__(self, data):
        self.data = data
        self.copy = data.copy()

    def run(self):
        # self.mergesort1(0, len(self.data) - 1)
        self.mergesort2(len(self.data))
        return self.data

    def mergesort1(self, start, end):
        # 递归方法
        if start == end:
            return 0

        half = (end - start) // 2
        self.mergesort1(start, start+half)
        self.mergesort1(start+half+1, end)

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

    def mergesort2(self, n):
        # 迭代方法
        k = 1
        while k < n:
            self.mergepass(self.data, self.copy, k, n)
            k *= 2
            self.mergepass(self.copy, self.data, k, n)
            k *= 2

    def mergepass(self, data1, data2, k, n):
        i = 0
        # i + 2*k <= n ====> i <= n - 2*k
        while i <= n-2*k:
            self.merge(i, k, i+2*k-1)
            i += 2*k
        if i < n - k:
            self.merge(i, k, n-1)
        else:
            data2[i:] = data1[i:]

    def merge(self, start, stride, end):
        # start:第一条归并序列开始的下标;
        # stride:第一条归并序列的长度；
        # end:第二条归并序列结束的下标（两条不一定等长）；
        p = start + stride - 1
        q = end
        copy_index = end
        while p >= start and q >= start + stride:
            if self.data[p] > self.data[q]:
                self.copy[copy_index] = self.data[p]
                p -= 1
            else:
                self.copy[copy_index] = self.data[q]
                q -= 1
            copy_index -= 1
        if p >= start:
            self.copy[start:copy_index + 1] = self.data[start:p + 1]
        if q >= start + stride:
            self.copy[start:copy_index + 1] = self.data[start + stride:q + 1]
        self.data[start:end + 1] = self.copy[start:end + 1]


if __name__ == "__main__":
    # 归并排序
    s = MergeSort([50, 10, 90, 30, 70, 40, 80, 60, 20])
    print(s.run())
