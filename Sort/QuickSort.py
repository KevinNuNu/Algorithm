# -*- coding:utf-8 -*-
class QuickSort:
    def __init__(self, data):
        self.data = data
        self.max_length_insert_sort = 7

    def run(self):
        self.quicksort3(0, len(self.data)-1)
        return self.data

    def quicksort1(self, left, right):
        # 这种快排的思路是：
        # 取序列第一个值作为key
        # 找到序列里“左边比key大，右边比key小”的值互换
        # 最后两个指针交汇的值(一定比key小)与key互换
        if left > right:
            return
        i, j = left, right
        key = self.data[left]
        while i < j:
            # 注意此处先指针j移动还是指针i移动是有顺序的(归根结底是因为key的选择是序列左数第一个)
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
        self.quicksort1(left, i-1)
        self.quicksort1(i+1, right)

    def quicksort2(self, left, right):
        # Hoare版本快排
        # 核心思想，不再是最后换key，而是每次都是和key交换
        # 找到右边比key小的，直接和key换，接着找到左边比key大的，再和key换
        # 直到指针i和指针j指向同一位置，此时key也换到了最佳的位置，左边都比key小，右边都比key大
        if left > right:
            return
        i, j = left, right
        key = self.data[left]
        while i < j:
            while self.data[j] >= key and i < j:
                j -= 1
            self.data[j], self.data[i] = self.data[i], self.data[j]
            while self.data[i] <= key and i < j:
                i += 1
            self.data[i], self.data[j] = self.data[j], self.data[i]
        self.quicksort2(left, i-1)
        self.quicksort2(i+1, right)

    def quicksort3(self, left, right):
        # Hoare版本快排（优化版）
        # 1.优化小数组时的排序方案：排序序列长度小于阈值（此处设为7）时采用直接插入排序
        if right - left + 1 > self.max_length_insert_sort:
            while left < right:
                i, j = left, right
                key = self.data[left]
                # 2.优化不必要的交换：改交换为赋值，最后再把key值赋给“指针i=指针j”的位置
                while i < j:
                    while self.data[j] >= key and i < j:
                        j -= 1
                    self.data[i] = self.data[j]
                    while self.data[i] <= key and i < j:
                        i += 1
                    self.data[j] = self.data[i]
                self.data[i] = key
                # 3.优化递归操作：改尾部两个递归为尾递归
                self.quicksort3(left, i - 1)
                left = i + 1
        else:
            self.data[left:right + 1] = straightinsertionsort(self.data[left:right + 1])


# 直接插入排序
def straightinsertionsort(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            temp = data[i]
            j = i - 1
            while j >= 0:
                if data[j] > temp:
                    data[j+1] = data[j]
                    j -= 1
                else:
                    break
            data[j+1] = temp
    return data


if __name__ == "__main__":
    # 快速排序
    s = QuickSort([7, 8, 9, 10, 6, 5, 1, 3, 4, 2])
    print(s.run())
