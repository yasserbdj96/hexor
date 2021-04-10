#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
import os

#start hexor class:
class hexor:
    #torgb:
    def torgb(hex):
        hex=hex.lstrip('#')
        lv=len(hex)
        return tuple(int(hex[i:i+lv//3],16) for i in range(0,lv,lv//3))

    #c:
    def c(text,foreground,background=False):
        f=hexor.torgb(foreground)
        if background:
            b=hexor.torgb(background)
            m="echo \033[38;2;{};{};{}m\033[48;2;{};{};{}m{}\033[0m".format(f[0],f[1],f[2],b[0],b[1],b[2],text)
        else:
            m="echo \033[38;2;{};{};{}m{}\033[0m".format(f[0],f[1],f[2],text)
        os.system(m)
#e