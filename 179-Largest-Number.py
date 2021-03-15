'''
Algorithms: Sort
Efficiency: High

Note: this is a Python2 version because Python3 sort does not have cmp param.
'''

class Solution:
    def largestNumber(self, nums):
        _str = []
        count_zeros = 0
        for elem in nums:
            if elem == 0:
                count_zeros += 1
            _str.append(str(elem))
        if count_zeros == len(nums):
            return "0"
        _str.sort(reverse=True, cmp=lambda a,b:1 if a+b>b+a else -1)
        result = ''
        for s in _str:
            result += s
        return result
