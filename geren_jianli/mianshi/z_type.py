#!/usr/bin/env python
#coding:utf-8

class ccc:
    def aaa(self, s: str, numRows: int) -> str:
        rel = ['']*numRows
        if numRows==1:
            return s
        else:
            for i in range(len(s)):
                k = i%(2*(numRows-1))
                if k<= numRows-1:
                    rel[k] += s[i]
                else:
                    rel[2*(numRows-1)-k] += s[i]
            result = ''.join(rel)
            print(rel)
            return result

print(ccc().aaa("abcdefghijklmn",3))
print(ccc().aaa("LEETCODEISHIRING",3))
