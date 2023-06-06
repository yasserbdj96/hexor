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
import re
import os

class hexor:
    def __init__(self, return_opt=False,color_type=""):
        self.return_opt = return_opt
        self.color_type=color_type

    @staticmethod
    def check_and_modify_color(input_color):
        hex_pattern = r'^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
        rgb_pattern = r'^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$'
        rgb2_pattern = r'^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*'

        if re.match(hex_pattern, input_color):
            # Input is a valid hex color
            if not input_color.startswith('#'):
                input_color = '#' + input_color
            #print("Modified hex color:", input_color)
            hex_code = input_color.lstrip('#')
            return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        elif re.match(rgb_pattern, input_color):
            # Input is a valid RGB color
            match = re.match(rgb_pattern, input_color)
            r, g, b = match.groups()
            modified_color = f'rgb({r},{g},{b})'
            #print("Modified RGB color:", modified_color)
            return tuple(map(int, re.findall(r'\d+', modified_color)))
        elif re.match(rgb2_pattern, input_color):
            # Input is a valid RGB color
            match = re.match(rgb2_pattern, input_color)
            r, g, b = match.groups()
            modified_color = f'rgb({r},{g},{b})'
            #print("Modified RGB color:", modified_color)
            return tuple(map(int, re.findall(r'\d+', modified_color)))
        else:
            raise ValueError("Invalid color format")
            #print("Invalid color")
            #exit()

    def c(self, text, foreground, background=False):
        foreground_rgb=self.check_and_modify_color(foreground)
        
        if background:
            background_rgb=self.check_and_modify_color(background)
            color_code = f"\033[38;2;{foreground_rgb[0]};{foreground_rgb[1]};{foreground_rgb[2]}m" \
                         f"\033[48;2;{background_rgb[0]};{background_rgb[1]};{background_rgb[2]}m{text}\033[0m"
        else:
            color_code = f"\033[38;2;{foreground_rgb[0]};{foreground_rgb[1]};{foreground_rgb[2]}m{text}\033[0m"

        if self.return_opt:
            return color_code
        else:
            print(color_code)
#}END.