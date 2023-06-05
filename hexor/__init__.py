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
    def __init__(self, return_opt=False,color_type="hex"):
        self.return_opt = return_opt
        self.color_type=color_type

    @staticmethod
    def hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def check_color_type(color):
        rgb_pattern = r'^rgb\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*\)$'
        hex_pattern = r'^#([A-Fa-f0-9]{3}){1,2}$'

        if re.match(rgb_pattern, color):
            return 'RGB'
        elif re.match(hex_pattern, color):
            return 'Hexadecimal'
        else:
            return 'Unknown'

    @staticmethod
    def convert_to_rgb(string):
        if string.startswith("rgb(") and string.endswith(")"):
            return string  # Already in "rgb(255,0,0)" format
        elif ',' in string:
            r, g, b = map(int, string.split(','))
            return f"rgb({r},{g},{b})"
        else:
            return string  # Not a valid format

    def c(self, text, foreground, background=False):
        if self.check_color_type(foreground) == "Hexadecimal":
            foreground_rgb = self.hex_to_rgb(foreground)
        elif self.check_color_type(foreground) == "RGB":
            foreground_rgb = tuple(map(int, re.findall(r'\d+', foreground)))
        elif self.color_type.lower()=="rgb":
            foreground=foreground.replace(" ","")
            foreground_rgb=foreground.split(",")
        elif ',' in foreground:
            foreground_rgb=tuple(map(int, re.findall(r'\d+', self.convert_to_rgb(foreground))))
        else:
            raise ValueError("Invalid foreground color format")

        if background:
            if self.check_color_type(background) == "Hexadecimal":
                background_rgb = self.hex_to_rgb(background)
            elif self.check_color_type(background) == "RGB":
                background_rgb = tuple(map(int, re.findall(r'\d+', background)))
            elif self.color_type.lower()=="rgb":
                background=background.replace(" ","")
                background_rgb=background.split(",")
            elif ',' in background:
                background_rgb=tuple(map(int, re.findall(r'\d+', self.convert_to_rgb(background))))
            else:
                raise ValueError("Invalid background color format")

            color_code = f"\033[38;2;{foreground_rgb[0]};{foreground_rgb[1]};{foreground_rgb[2]}m" \
                         f"\033[48;2;{background_rgb[0]};{background_rgb[1]};{background_rgb[2]}m{text}\033[0m"
        else:
            color_code = f"\033[38;2;{foreground_rgb[0]};{foreground_rgb[1]};{foreground_rgb[2]}m{text}\033[0m"

        if self.return_opt:
            return color_code
        else:
            print(color_code)
#}END.