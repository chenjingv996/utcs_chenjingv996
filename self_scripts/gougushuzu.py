#!/usr/bin/env python
#coding:utf-8
print("*"*60)
class Gougushu():
    def gougu_tuple(self,m,n):
        lst=[]
        flag=0
        for j in range(m,n+1):
            for k in range(j+1,k+1):
                for x in range(k+1,n+1):
                    if self.exist_divisors(j,k,x)==0 and j**2+k**2==x**2:
                        print("(%d,%d,%d)是勾股数元祖"%(j,k,x))
                        lst.append((j,k,x))
                        flag=1
        if flag==0:
            print("NA")
            return "NA"
        else:
            print(lst)
            return lst
    def exist_divisor(self,num1,num2):
        flag=0
        for i in range(2,min(num1,num2)+1):
            if num1%i==0 and num2%i==0:
                flag=1
                print("%d和%d的公约数为%d"%(num1,num2,i))
                break
        print(flag)
        return flag
    def exist_divisors(self,num1,num2,num3):
        flag=0
        if self.exist_divisor(num1,num2)==1 or self.exist_divisor(num1,num3)==1 or self.exist_divisor(num3,num2)==1:
            flag=1
        print(flag)
        return flag
if __name__=="__main__":
    Gougushu().gougu_tuple(1,20)
        

