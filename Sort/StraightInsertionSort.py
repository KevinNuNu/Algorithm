# -*- coding:utf-8 -*-
class StraightInsertionSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.straightinsertionsort()
        return self.data

    def straightinsertionsort(self):
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[i-1]:
                temp = self.data[i]
                j = i - 1
                while j >= 0 and self.data[j] > temp:
                    self.data[j+1] = self.data[j]
                    j -= 1
                self.data[j+1] = temp


if __name__ == "__main__":
    # 简单选择排序
    s = StraightInsertionSort([2, 1, 3, 4, 5, 9, 8, 7, 6])
    print(s.run())
