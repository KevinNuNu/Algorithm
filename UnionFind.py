class UnionFind:
    def __init__(self, n):
        self.n = n
        # 初始化节点i的直接父节点parent[i]为自身i
        self.parent = list(range(n))
        # 初始化节点i作为根节点的树的高度为1
        self.rank = [1] * n

    def find(self, x):
        # 查询节点x的根节点
        r = x
        while r != self.parent[r]:
            r = self.parent[r]

        # 进行路径压缩
        i = x
        while self.parent[i] != r:
            self.parent[i], i = r, self.parent[i]

        return r

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        # 将高度较小的树连接到高度较大的树上
        if i_root != j_root:
            if self.rank[i_root] == self.rank[j_root]:
                self.parent[i_root] = j_root
                self.rank[j_root] += 1
            elif self.rank[i_root] > self.rank[j_root]:
                self.parent[j_root] = i_root
            else:
                self.parent[i_root] = j_root

    def unionfind(self):
        for i in range(1, self.n):
            arr = list(map(int, input().split(' ')))
            for j in range(len(arr)):
                if arr[j] == 0:
                    break
                else:
                    self.union(i, arr[j])
            print(self.parent)

        # for i in range(1, self.n):
        #     self.find(i)
        # print(self.parent)


if __name__ == "__main__":
    # 并查集
    N = int(input())
    # 由于题目需要下标需要从1开始，所以此处加了1，不同情况不同分析
    u = UnionFind(N+1)
    u.unionfind()
"""
10
0
5 3 0
8 4 0
9 0
9 0
3 0
0
7 9 0
0
9 7 0
"""
