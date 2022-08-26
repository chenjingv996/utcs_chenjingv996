#!/usr/bin/env python
#coding:utf-8



class ccc():
    def aaa(self,nums:int)->bool:
        #str1=str(nums)
        #lst1=list(nums)
        #lst2=lst1.reverse()
        #str2=str(lst2)

        if str(nums)==str(nums)[::-1]:
            return True
        else:
            return False


print(ccc().aaa(12321))
print(ccc().aaa(1232342))

