# -*- coding:utf-8 -*-
class SimpleSelectionSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.simpleselectionsort()
        return self.data

    def simpleselectionsort(self):
        for i in range(len(self.data)):
            minidx = i
            minval = self.data[i]
            for index, item in enumerate(self.data[i+1:]):
                if item < minval:
                    minval, minidx = item, index+i+1
            if i != minidx:
                self.data[i], self.data[minidx] = self.data[minidx], self.data[i]


if __name__ == "__main__":
    # 简单选择排序
    s = SimpleSelectionSort([2, 1, 3, 4, 5, 9, 8, 7, 6])
    print(s.run())
