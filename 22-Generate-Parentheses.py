'''
Algorithms: DFS
Efficiency: Normal
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, 0, n, "", 0, 0)
        return res

    def dfs(self, res, curlen, n, pattern, l, r):
        if curlen == 2 * n:
            res.append(pattern)
            return
        if l < n:
            self.dfs(res, curlen+1, n, pattern+'(', l+1, r)
        if r < l:
            self.dfs(res, curlen+1, n, pattern+')', l, r+1)
