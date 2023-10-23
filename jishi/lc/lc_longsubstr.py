#!/usr/bin/env python
#coding:utf-8


class ccc:
    def aaa(self,s:str)->int:
        n=len(s)
        ret,l,r=0,0,0
        if n==0:
            return 0
        while r<n:
            if s[r] not in s[l:r]:
               r+=1
               ret=max(ret,len(s[l:r]))
               print(s[l:r])
            else:
                while s[r] in s[l:r]:
                    l+=1
        return ret

bbb=ccc()
print(bbb.aaa('cabcabdcbb'))

