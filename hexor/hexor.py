#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
from pipincluder import pipincluder

#import pakages by pipincluder:
exec(pipincluder("import os").modules())

#start hexor class:
class hexor:
    #__init__:
    def __init__(self,return_opt=False,color_type="hex"):
        self.return_opt=return_opt
        self.color_type=color_type
        
    #torgb:
    def torgb(hex):
        hex=hex.lstrip('#')
        lv=len(hex)
        return tuple(int(hex[i:i+lv//3],16) for i in range(0,lv,lv//3))

    #c:
    def c(self,text,foreground,background=False):
        os.system('')
        if self.color_type=="hex":
            f=hexor.torgb(foreground)
        elif self.color_type=="rgb":
            foreground=foreground.replace(" ","")
            f=foreground.split(",")
        if background:
            if self.color_type=="hex":
                b=hexor.torgb(background)
            elif self.color_type=="rgb":
                background=background.replace(" ","")
                b=background.split(",")
            if self.return_opt==True:
                return f"\033[38;2;{f[0]};{f[1]};{f[2]}m\033[48;2;{b[0]};{b[1]};{b[2]}m{text}\033[0m"
            elif self.return_opt==False:
                print(f"\033[38;2;{f[0]};{f[1]};{f[2]}m\033[48;2;{b[0]};{b[1]};{b[2]}m{text}\033[0m")
        else:
            if self.return_opt==True:
                return f"\033[38;2;{f[0]};{f[1]};{f[2]}m{text}\033[0m"
            elif self.return_opt==False:
                print(f"\033[38;2;{f[0]};{f[1]};{f[2]}m{text}\033[0m")
#e