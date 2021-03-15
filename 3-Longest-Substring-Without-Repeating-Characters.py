'''
Algorithms Tags: Simulation, Brute Force
Effeciency: Normal

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lgst = 0
        curr = 0
        buff = []
        for c in s:
            
            if c not in buff:
                buff.append(c)
                curr += 1
            else:
                lgst = max(lgst, curr)
                for i in range(len(buff)):
                    if buff[i] == c:
                        buff = buff[i+1:]
                        buff.append(c)
                        curr = len(buff)
                        break
        lgst = max(curr, lgst)
                    
        return lgst
