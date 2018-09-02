# -*- coding:utf-8 -*-
class QuickSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.quicksort(0, len(self.data)-1)
        return self.data

    def quicksort(self, left, right):
        if left > right:
            return
        i, j = left, right
        key = self.data[left]
        while i != j:
            # 注意此处先指针j移动还是指针i移动是有顺序的
            # 因为我们的目的是将数据划分为：key的左边比key小，key的右边比key大
            # 最后将self.data[left]和self.data[i]互换意味着将小于key的self.data[i]扔到key的左边
            # 所以一定要指针j先动使得最终指针指向的位置停留在一个比key小的位置上
            # 如果指针i先动，则最终指针指向的位置会停留在一个比key大的位置上，从而交换以后不满足左小右大
            while self.data[j] >= key and i < j:
                j -= 1
            while self.data[i] <= key and i < j:
                i += 1
            if i < j:
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[left], self.data[i] = self.data[i], self.data[left]
        self.quicksort(left, i-1)
        self.quicksort(i+1, right)


if __name__ == "__main__":
    # 快速排序
    s = QuickSort([10, 5, 6, 1, 7, 4, 3, 23, 14])
    print(s.run())
