# -*- coding:utf-8 -*-
class RadixSort:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.radixsort()
        return self.data

    def radixsort(self, radix=10):
        K = int(math.ceil(math.log(max(self.data) + 1, radix)))  # 用K位数可表示任意整数
        for i in range(1, K + 1):  # K次循环
            bucket = [[] for i in range(radix)]  # 不能用 [[]]*radix，否则相当于开了radix个完全相同的list对象
            for val in self.data:
                bucket[val % (radix ** i) // (radix ** (i - 1))].append(val)  # 获取整数第K位數字（从低到高）
            del self.data[:]
            for each in bucket:
                self.data.extend(each)  # 桶合并


if __name__ == "__main__":
    import math
    # 基数排序
    s = RadixSort([2, 1, 3, 4, 5, 9, 8, 7, 6, 10, 21])
    print(s.run())
