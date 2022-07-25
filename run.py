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

try:
    import os
    import sys
    #
    TYPE = os.environ['T'] if "T" in os.environ else sys.argv[1]
    TEXT = os.environ['TEXT'] if "TEXT" in os.environ else sys.argv[2]
    FC = os.environ['FC'] if "FC" in os.environ else sys.argv[3]
    
    try:
        BG = os.environ['BG'] if "BG" in os.environ else sys.argv[4]
    except:
        BG=""
except Exception as e:
    print(f"USAGE : python3 {sys.argv[0]} <TYPE*> <TEXT*> <FC*> <BG>")
    help="""    
        TYPE = hex/rgb.
        TEXT = Your text.
        FC   = Front Color.
        BG   = Background Color.
        *    = All inputs must be entered."""
    print(help)
    exit()
    #pass

# :
p1=hexor(False,TYPE)
if BG!="":
    p1.c(TEXT,FC,BG)
else:
    p1.c(TEXT,FC)
#}END.
