# -*- coding:utf-8 -*-
class BubbleSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.bubblesort2()
        return self.data

    def bubblesort1(self):
        # 基础冒泡排序
        for i in range(len(self.data)):
            for j in range(i, len(self.data)-1)[::-1]:
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def bubblesort2(self):
        # 优化冒泡排序
        # 例如：[2,1,3,4,5]，第一次冒泡就已经排好序了，就不需要继续进行后续的比较了
        # 增加一个tag用于记录是否已经排好序（前一次是否不存在交换）
        tag = True
        for i in range(len(self.data)):
            if not tag:
                break
            else:
                tag = False
            for j in range(i, len(self.data)-1)[::-1]:
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    tag = True


if __name__ == "__main__":
    # 冒泡排序
    s = BubbleSort([2, 1, 3, 4, 5])
    print(s.run())
