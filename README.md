<h1>hexor</h1>

<p>Coloring texts and their backgrounds in command line interface (cli), with rgb or hex types.</p>

[![Python package](https://github.com/yasserbdj96/hexor/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/yasserbdj96/hexor/actions/workflows/python-app.yml)  [![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/hexor/badge)](https://www.codefactor.io/repository/github/yasserbdj96/hexor)

<h2>Languages:</h2>
* python3

<h2>Supported Distributions:</h2>

| Distribution | Version Check     | Python Test Version | Supported | Status  | Everything works |
| :----------: | :---------------: | :-----------------: | :-------: | :----:  | :--------------: |
| Ubuntu       | 20.04.3           | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |
| Windwos      | 11.6.4            | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |
| MacOS        | 10.0.20348        | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |

<h2>Installation:</h2>

```
pip install hexor
```

<h2>Usage:</h2>

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

<h2>Examples:</h2>

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
    <a href="https://raw.githubusercontent.com/yasserbdj96/hexor/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/hexor/main/screenshot/screenshot_1.png">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.0.10 [26-02-2022]
 - Fix bugs.
 
## 0.0.8 [26-02-2022]
 - Delete pipincluder pakage.
 - Fix bugs.

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
```

<h1></h1> 

<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information</a>
    <br>
    <a href="https://github.com/yasserbdj96/hexor" align="center">
        <img align="center"  alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.hexor">
    </a>
</div>
