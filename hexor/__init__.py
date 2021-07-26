#!/usr/bin/env python
# coding:utf-8
"""
#set:usage.py,examples.py,changelog.txt
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
# CHANGELOG :
#s
## 0.0.7
- Fix Bugs.

## 0.0.6
 - fix bugs.
 - new build.
 
## 0.0.5
 - Import pakages by pipincluder.
 - Fix bugs.
 
## 0.0.4
 - Fix bugs.
 
## 0.0.3
 - Fix bugs.
 
## 0.0.2
 - Fix bugs.
 - Add RGB type.
 
## 0.0.1
 - First public release.
#e
##################################################################
"""
# VALUES :
__version__="0.0.7"
__name__="hexor"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="hexor texts colors."
__description__="hexor for color the texts in hex or rgb colors."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
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