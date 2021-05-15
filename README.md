
<h1>hexor texts colors.</h1>

<p>hexor for color the texts in hex or rgb colors.</p>
<p align="center">
    <img align="center" src="https://travis-ci.com/byRo0t96/hexor.svg?branch=main">
    <img align="center" src="https://img.shields.io/github/issues/byRo0t96/hexor">
    <img align="center" src="https://img.shields.io/github/forks/byRo0t96/hexor">
    <img align="center" src="https://img.shields.io/github/stars/byRo0t96/hexor">
    <img align="center" src="https://img.shields.io/badge/license-Apache--2.0-green.svg">
    <img align="center" src="https://img.shields.io/badge/python-3.x.x-blue">
</p>
<h2>Installation:</h2>

```
pip install hexor==0.0.6
```

<h2>Usage:</h2>

```python
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

```

<h2>Examples:</h2>

```python
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

```

<h2>Changelog:</h2>

```
## 0.0.6
 - fix bugs.
 - new build 

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
<br>
<br>
<p align="center">
    <a align="center" href="https://byro0t96.github.io/">
        <img alt="byRo0t96" height="100" align="center" src="https://raw.githubusercontent.com/byRo0t96/byRo0t96/main/images/Ro0t-96_v.3.1.png">
    </a>
</p>

<p align="center">
    <a align="center" href="https://www.facebook.com/yasser.bdj.31">
        <img alt="facebook" align="center" src="https://img.shields.io/badge/Facebook-%2Fyasser.bdj.31-blue">
    </a>
	
   <a align="center" href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg">
        <img align="center"  alt="youtube" src="https://img.shields.io/badge/-YouTube-red">
    </a>
	
   <a href="https://www.linkedin.com/in/boudjada-yasser-a53543196" align="center" >
        <img align="center" alt="LinkedIn" src="https://img.shields.io/badge/-linkedin-blue">
    </a> 
    
   <a href="https://www.instagram.com/bdj.yasser/" align="center" >
        <img align="center" alt="instagram" src="https://img.shields.io/badge/instagram-%2Fbdj.yasser-orange">
    </a> 
        
   <a href="https://github.com/byRo0t96/" align="center" >
        <img align="center" alt="visitor-badge" src="https://visitor-badge.laobi.icu/badge?page_id=byRo0t96.byRo0t96">
    </a>
</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>