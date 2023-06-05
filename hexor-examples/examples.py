#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
from hexor import *

# Example:1
p1=hexor(False,"hex")
p1.c("Text is red","#ff0000")
p1.c("Text is red and background is blue","#ff0000","#1a73e8")

# Example:2
p1=hexor()
p1.c("Text is red","#ff0000")
p1.c("Text is red and background is blue","#ff0000","#1a73e8")

# Example:3
p2=hexor(True,"hex")
print(p2.c("Text is red","#ff0000"))
print(p2.c("Text is red and background is blue","#ff0000","#1a73e8"))

# Example:4
p2=hexor(True)
print(p2.c("Text is red","#ff0000"))
print(p2.c("Text is red and background is blue","#ff0000","#1a73e8"))

# Example:5
p1=hexor(False,"rgb")
p1.c("Text is red","255,0,0")
p1.c("Text is red and background is blue","255,0,0","26,115,232")

# Example:6
p1=hexor()
p1.c("Text is red","255,0,0")
p1.c("Text is red and background is blue","255,0,0","26,115,232")

# Example:7
p1=hexor()
p1.c("Text is red","rgb(255,0,0)")
p1.c("Text is red and background is blue","rgb(255,0,0)","rgb(26,115,232)")

# Example:8
p1=hexor(True,"rgb")
print(p1.c("Text is red","255,0,0"))
print(p1.c("Text is red and background is blue","255,0,0","26,115,232"))

# Example:9
p1=hexor(True)
print(p1.c("Text is red","255,0,0"))
print(p1.c("Text is red and background is blue","255,0,0","26,115,232"))

# Example:10
p1=hexor(True,"rgb")
print(p1.c("Text is red","rgb(255,0,0)"))
print(p1.c("Text is red and background is blue","rgb(255,0,0)","rgb(26,115,232)"))

# Example:11
p1=hexor()
p1.c("Text is red and background is blue","rgb(255,0,0)","26,115,232")
p1.c("Text is red and background is blue","255,0,0","rgb(26,115,232)")
p1.c("Text is red and background is blue","rgb(255,0,0)","#1a73e8")
p1.c("Text is red and background is blue","255,0,0","#1a73e8")

# Example:12
hexor().c("Text is red","#ff0000")# hexor().c("Text is red","#ff0000")
hexor(False,"rgb").c("Text is red and background is blue","255,0,0","26,115,232")
#}END.
