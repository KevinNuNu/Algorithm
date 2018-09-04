# -*- coding:utf-8 -*-
class ShellSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.shellsort()
        return self.data

    def shellsort(self):
        n = len(self.data)
        # 初始步长
        gap = n // 2
        while gap > 0:
            # 简单插入排序
            for i in range(gap, n):
                temp = self.data[i]
                j = i
                while j >= gap and self.data[j-gap] > temp:
                    self.data[j] = self.data[j-gap]
                    j -= gap
                self.data[j] = temp
            gap = gap // 2


if __name__ == "__main__":
    # 希尔排序
    s = ShellSort([2, 1, 3, 4, 5, 9, 8, 7, 6])
    print(s.run())
