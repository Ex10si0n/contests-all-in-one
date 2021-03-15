'''
Algorithms Tags: Greedy
Efficiency: High
'''

class Solution:
    '''
    def bruteForce(self, height: List[int]) -> int:
        _max = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                _max = max(_max, (j - i) * min(height[i], height[j]))
        return _max
    '''

    def maxArea(self, height: List[int]) -> int:
        _max = 0
        i = 0
        j = len(height) - 1
        while i != j:
            _max = max(_max, (j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return _max

