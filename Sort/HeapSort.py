# -*- coding:utf-8 -*-
class HeapSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.heapsort()
        return self.data

    def heapsort(self):
        def heapadjust(lst, start, end):
            """最大堆调整"""
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and lst[child] < lst[child+1]:
                    child += 1
                if lst[root] < lst[child]:
                    lst[root], lst[child] = lst[child], lst[root]
                    root = child
                else:
                    break
        n = len(self.data)
        # 创建最大堆
        for start in range((n - 2) // 2, -1, -1):
            heapadjust(self.data, start, n-1)

        # 堆排序
        for end in range(n - 1, 0, -1):
            self.data[0], self.data[end] = self.data[end], self.data[0]
            heapadjust(self.data, 0, end - 1)


if __name__ == "__main__":
    # 堆排序
    s = HeapSort([50, 10, 90, 30, 70, 40, 80, 60, 20])
    print(s.run())
