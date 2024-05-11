#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
'''
Time Complexity - O(n)
Space Complexity - O(1)

Works on Leetcode
'''
class Solution:
    def cmp_function(self, logs):
        id, log = logs.split(" ", 1) #split the log into identifier and remaining log based on space
        if log[0].isalpha(): #if its a letter log, then this log has higher priority than a digit log and a log starting with lexicographically greater character
            #if lexicographically equal then compare the identifiers of the 2 logs
            return (0, log, id)
        else:
            #if log is digit put it after the letter log and maintain order between digit logs
            return (1, None, None)
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key = self.cmp_function)
        
# @lc code=end

