#!/usr/bin/env python
# coding:utf-8
"""
#set:usage,examples,changelog
##################################################################
# USAGE :
#s
from hexor import hexor

# Make options:
# p1=hexor(return_option,'type_of_color')
## return_option:[True,False]
### True for return results
### False for print results
## type_of_color:['hex','rgb']
### hex for hex colors for example : #ffffff, #cccccc
### rgb for rgb colors for example : (255,255,255), (250,12,0)
# default options is : hexor() = hexor(False,'hex')
p1=hexor(<OPTIONS>)

# To change text color only:
p1.c("<TEXT>","<FOREGROUND>")
	
# To change text color and background together:
p1.c("<TEXT>","<FOREGROUND>","<BACKGROUND>")
#e
##################################################################
# EXAMPLES :
#s
from hexor import hexor

# Example:1
p1=hexor(False,"hex")
p1.c("Text is red","#ff0000")
p1.c("Text is red and background is blue","#ff0000","#1a73e8")

# Example:2
p2=hexor(True,"hex")
print(p2.c("Text is red","#ff0000"))
print(p2.c("Text is red and background is blue","#ff0000","#1a73e8"))

# Example:3
p1=hexor(False,"rgb")
p1.c("Text is red","255,0,0")
p1.c("Text is red and background is blue","255,0,0","26,115,232")

# Example:4
p1=hexor(True,"rgb")
print(p1.c("Text is red","255,0,0"))
print(p1.c("Text is red and background is blue","255,0,0","26,115,232"))

# Example:5
hexor().c("Text is red","#ff0000")# hexor().c("Text is red","#ff0000")
hexor(False,"rgb").c("Text is red and background is blue","255,0,0","26,115,232")
#e
##################################################################
"""
# VALUES :
#s
__version__="0.0.6"
__name__="hexor"
__author__="Yasser BDJ (Ro0t96)"
__author_email__="by.root96@gmail.com"
__github_user_name__="byRo0t96"
__title__="hexor texts colors."
__description__="hexor for color the texts in hex or rgb colors."
__author_website__="https://byro0t96.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=['python','hexor','text','color','hex','rgb']
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='Apache Software License'
__license_text__=f'''Copyright (c) 2008->Present, {__author__}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
__copyright__='Copyright 2008 -> Present, '+__author__

__changelog__=("## 0.0.6\n - fix bugs.\n - new build \n\n")
__changelog__=__changelog__+("## 0.0.5\n - Import pakages by pipincluder.\n- Fix bugs.\n\n")
__changelog__=__changelog__+("## 0.0.4\n - Fix bugs.\n\n")
__changelog__=__changelog__+("## 0.0.3\n - Fix bugs.\n\n")
__changelog__=__changelog__+("## 0.0.2\n - Fix bugs.\n- Add RGB type.\n\n")
__changelog__=__changelog__+("## 0.0.1\n - First public release.\n\n")

##################################################################
#e

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