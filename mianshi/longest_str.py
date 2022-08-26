#!/usr/bin/env python
#coding:utf-8

print("#"*80)



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1
        length = len(s)
        res, freq = 0, []
        while l < length:
            if r + 1 < length and s[r + 1] not in freq:
                r += 1
                freq.append(s[r])
            else:
                freq.pop(0)
                l += 1
            res = max(res, r - l + 1)
        return res


print(Solution().lengthOfLongestSubstring(abcbaddfd))
