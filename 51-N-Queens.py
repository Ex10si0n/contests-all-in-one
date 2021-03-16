'''
Algotithms: Backtracking
Efficiency: Nearly Optimized
'''
class Solution:
    def __init__(self):
        self.column = None
        self.position = None
        self.left = None
        self.right = None
        self.n = 0
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.column = [False for i in range(n * 2)]
        self.position = [-1 for i in range(n * 2)]
        self.left = [False for i in range(n * 2)]
        self.right = [False for i in range(n * 2)]
        self.result = []
        self.dfs(0)
        return self.result

    def parsePosition(self, pos):
        res = []
        for i in range(self.n):
            res.append("." * (pos[i]) + 'Q' + '.' * (self.n - pos[i] - 1))
        return res



    def dfs(self, depth):
        # print("col:", self.column)
        # print("l  :", self.left)
        # print("r  :", self.right)
        if depth == self.n:
            self.result.append(self.parsePosition(self.position))
            return
        for i in range(self.n):
            if (not self.column[i]) and \
            (not self.left[depth + i]) and \
            (not self.right[depth + self.n - i]):
                self.column[i] = True
                self.left[depth + i] = True
                self.right[depth + self.n - i] = True
                self.position[depth] = i
                self.dfs(depth + 1)
                self.position[depth] = -1
                self.column[i] = False
                self.left[depth + i] = False
                self.right[depth + self.n - i] = False

