#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sz = len(intervals)
        ans = []
        left, right = -1, -1
        p = 0
        while p < sz:
            tmp = intervals[p]
            if left < 0:
                if newInterval[0] < tmp[0]:
                    left = newInterval[0]
                elif tmp[0] <= newInterval[0] <= tmp[1]:
                    left = tmp[0]
                # tmp[1] < newInterval[0]
                else:
                    ans.append(tmp)
                    p += 1
                    continue
            elif right < 0:
                if newInterval[1] < tmp[0]:
                    ans.append([left, newInterval[1]])
                    right = newInterval[1]
                    break
                elif tmp[0] <= newInterval[1] <= tmp[1]:
                    ans.append([left, tmp[1]])
                    right = tmp[1]
                    p += 1
                    break
                # tmp[1] < newInterval[1]
                else:
                    p += 1
                    continue
        if left < 0:
            ans.append(newInterval)
        elif right < 0:
            ans.append([left, newInterval[1]])
        else:
            ans += intervals[p:]
        return ans

# @lc code=end

