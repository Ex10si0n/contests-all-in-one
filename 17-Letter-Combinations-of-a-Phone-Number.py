'''
Algorithms: DFS
Efficiency: Optimized
'''
class Solution:

    def __init__(self):
        self._map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self._len = None
        self.digits = None
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        self._len = len(digits)
        if self._len == 0:
            return []
        self.digits = digits
        self.dfs(0, '')
        return self.res

    def dfs(self, depth, pattern):
        if depth == self._len:
            self.res.append(pattern)
            return
        for c in self._map[int(self.digits[depth])]:
            self.dfs(depth+1, pattern+c)

