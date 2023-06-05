<h1>hexor</h1>

<p>Coloring texts and their backgrounds in command line interface (cli), with rgb or hex types.</p>

[![Test on Ubuntu latest](https://github.com/yasserbdj96/hexor/actions/workflows/python-app-on-linux.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/python-app-on-linux.yml)
[![Test on Windows latest](https://github.com/yasserbdj96/hexor/actions/workflows/python-app-on-win.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/python-app-on-win.yml)
[![Test on MacOS latest](https://github.com/yasserbdj96/hexor/actions/workflows/python-app-on-mac.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/python-app-on-mac.yml)
[![pypi-setup](https://github.com/yasserbdj96/hexor/actions/workflows/pypi-setup.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/pypi-setup.yml)
[![Upload to PYPI](https://github.com/yasserbdj96/hexor/actions/workflows/pipup.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/pipup.yml)
[![Deploy static content to Pages](https://github.com/yasserbdj96/hexor/actions/workflows/pages.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/pages.yml)
[![CodeQL](https://github.com/yasserbdj96/hexor/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/yasserbdj96/hexor/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/hexor/badge)](https://www.codefactor.io/repository/github/yasserbdj96/hexor)
[![Supported Versions](https://img.shields.io/pypi/pyversions/hexor.svg)](https://pypi.org/project/hexor) 
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.hexor&format=true)](https://github.com/yasserbdj96/hexor)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red)](https://github.com/yasserbdj96/hexor)
[![Stars](https://img.shields.io/github/stars/yasserbdj96/hexor?color=red)](https://github.com/yasserbdj96/hexor)
[![Forks](https://img.shields.io/github/forks/yasserbdj96/hexor?color=red)](https://github.com/yasserbdj96/hexor)
[![Watching](https://img.shields.io/github/watchers/yasserbdj96/hexor?label=Watchers&color=red&style=flat-square)](https://github.com/yasserbdj96/hexor)
![GitHub contributors](https://img.shields.io/github/contributors/yasserbdj96/hexor)
![GitHub closed issues](https://img.shields.io/github/issues-closed/yasserbdj96/hexor)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/yasserbdj96/hexor)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/yasserbdj96/hexor)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/yasserbdj96/hexor)
![GitHub last commit](https://img.shields.io/github/last-commit/yasserbdj96/hexor)
[![GitHub license](https://img.shields.io/github/license/yasserbdj96/hexor)](https://github.com/yasserbdj96/hexor)
[![Join the chat at https://gitter.im/yasserbdj96/hexor](https://badges.gitter.im/yasserbdj96/hexor.svg)](https://gitter.im/yasserbdj96/hexor?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<h2>Languages:</h2>
* python3

<h2>Supported Distributions:</h2>

| Distribution   | Version Check | Python Version | Supported | Status    | Everything works |
| :------------: | :-----------: | :------------: | :-------: | :-------: | :--------------: |
| Ubuntu         | Last version  | 3.7 --> 3.11   | ✓         |  ✓       | ✓                |
| Windwos        | Last version  | 3.7 --> 3.11   | ✓         |  ✓       | ✓                |
| MacOS          | Last version  | 3.7 --> 3.11   | ✓         |  ✓       | ✓                |
| Android-termux | Last version  | 3.7 --> 3.11   | ✓         |  ✓       | ✓                |
| Nethunter      | Last version  | 3.7 --> 3.11   | ✓         |  ✓       | ✓                |



<h2>Python Package Installation:</h2>

```
# install from pypi:
❯ pip install hexor

# local install:
❯ git clone https://github.com/yasserbdj96/hexor.git
❯ cd hexor
❯ pip install .
```

<h2>Script Usage:</h2>

```python
from hexor import hexor

# Usage example:
# p1 = hexor(return_option, color_format)

## return_option: [True, False]
### True to return results
### False to print results

## color_format: ['hex', 'rgb']
### 'hex' for hex colors (e.g., #ffffff, #cccccc)
### 'rgb' for rgb colors (e.g., (255, 255, 255), (250, 12, 0))

# The default options are: hexor() = hexor(False, 'hex')
p1 = hexor(<return_option>, <color_format>)

# To change text color only:
p1.c("<TEXT>", "<FOREGROUND>")

# To change text color and background together:
p1.c("<TEXT>", "<FOREGROUND>", "<BACKGROUND>")
```

<h2>Script Examples:</h2>

```python
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
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/hexor/main/screenshot/screenshot.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/hexor/main/screenshot/screenshot.png">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hexor/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/hexor/main/screenshot/screenshot_1.png">
    </a>
</div>

<br>
<h2>Changelog History:</h2>
<a href="https://raw.githubusercontent.com/yasserbdj96/hexor/main/CHANGELOG">Click to See changelog History</a>

<br>
<h2>Development By:</h2>

Developer / Author: [yasserbdj96](https://github.com/yasserbdj96)

<br>
<h2>License:</h2>
<p>The content of this repository is bound by the following <a href="https://raw.githubusercontent.com/yasserbdj96/hexor/main/LICENSE">LICENSE</a>.</p>

<br>
<h2>Support:</h2>
<p>If you enjoy this project and would like to see it continue to improve, or if you would like me to create more interesting projects, please consider <a href="https://github.com/sponsors/yasserbdj96">sponsoring me</a>.</p>
<br>
<br>

<br><br>

<p align="center">
  <samp>
    <a href="https://yasserbdj96.github.io/">website</a> .
    <a href="https://github.com/yasserbdj96">github</a> .
    <a href="https://gitlab.com/yasserbdj96">gitlab</a> .
    <a href="https://www.linkedin.com/in/yasserbdj96">linkedin</a> .
    <a href="https://twitter.com/yasserbdj96">twitter</a> .
    <a href="https://instagram.com/yasserbdj96">instagram</a> .
    <a href="https://www.facebook.com/yasserbdj96">facebook</a> .
    <a href="https://www.youtube.com/@yasserbdj96">youtube</a> .
    <a href="https://pypi.org/user/yasserbdj96">pypi</a> .
    <a href="https://hub.docker.com/u/yasserbdj96">docker</a> .
    <a href="https://t.me/yasserbdj96">telegram</a> .
    <a href="https://gitter.im/yasserbdj96/yasserbdj96">gitter</a> .
    <a href="mailto:yasser.bdj96@gmail.com">e-mail</a> .
    <a href="https://ko-fi.com/yasserbdj96">sponsor</a>
  </samp>
</p>