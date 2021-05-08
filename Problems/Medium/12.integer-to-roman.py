#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        if p := (num // 1000):
            s += ['', 'M', 'MM', 'MMM'][p]
        num %= 1000
        if p := (num // 100):
            s += ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'][p]
        num %= 100
        if p := (num // 10):
            s += ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'][p]
        num %= 10
        if p := num:
            s += ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][p]
        return s

# @lc code=end

