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

| Distribution     | Version Check | Python Test Version       | Supported | Status    | Everything works |
| :--------------: | :-----------: | :-----------------------: | :-------: | :-------: | :--------------: |
| Ubuntu           | 20.04.4       | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Windwos          | 10.0.20348    | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| MacOS            | 11.6.6        | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Android (termux) | 10            | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |

<h2>Python Package Installation:</h2>

```
# install from pypi:
pip install hexor

# local install:
git clone https://github.com/yasserbdj96/hexor.git
cd hexor
sudo python setup.py install
```

<h2>Run without installation:</h2>

```
git clone https://github.com/yasserbdj96/hexor.git
cd hexor
python3 run.py <TYPE*> <TEXT*> <FC*> <BG>

# TYPE = hex/rgb.
# TEXT = Your text.
# FC   = Front Color.
# BG   = Background Color.
# *    = All inputs must be entered.
```

<h2>Script Usage:</h2>

```python
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
	
# To change text color & background together:
p1.c("<TEXT>","<FOREGROUND>","<BACKGROUND>")
```

<h2>Script Examples:</h2>

```python
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
<p>If you like `hexor` and want to see it improve furthur or want me to create intresting projects , You can buy me a coffee </p>
<div align="center">
    <a href="https://ko-fi.com/yasserbdj96">
        <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="hexor by yasserbdj96">
    </a><br>
    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9<br>
</div>

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