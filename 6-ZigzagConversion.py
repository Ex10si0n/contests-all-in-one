class Solution(object):
    def convert(self, s, numRows):
        """
        line 1 gap: (2n-2 0)
        line 2 gap: (2n-4 2)
        line 3 gap: (2n-6 4)
        ...
        line n gap: (0 2n-2)
        """
        res = ''
        if numRows == 1:
            return s
        for i in range(numRows):
            j = i
            while j < len(s):
                gap1 = 2 * numRows - 2 * (i + 1)
                if gap1 != 0 and j < len(s):
                    res += s[j]
                    j += gap1

                gap2 = 2 * numRows - 2 - gap1
                if gap2 != 0 and j < len(s):
                    res += s[j]
                    j += gap2
        return res


if __name__ == '__main__':
    s = 'A'
    numRows = 1
    solution = Solution()
    print(solution.convert(s, numRows))
