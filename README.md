
<h1>hexor texts colors.</h1>

<p>hexor for color the texts in hex or rgb colors.</p>

<h2>Installation:</h2>

```
pip install hexor==0.0.7
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
	
# To change text color and background together:
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

<h2>Changelog:</h2>

```
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
   
<p align="center">
   <a href="https://www.linkedin.com/in/yasserbdj96" align="center"><img align="center" alt="linkedin" src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white"></a>
   <a href="https://yasserbdj96.github.io" align="center"><img align="center" alt="website" src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white"></a>
   <a href="https://twitter.com/yasserbdj96" align="center"><img align="center" alt="twitter" src="https://img.shields.io/badge/-Twitter-00acee?style=flat-square&logo=Twitter&logoColor=white"></a>
   <a href="https://www.instagram.com/yasserbdj96" align="center"><img align="center" alt="instagram" src="https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white"></a>
   <a href="https://www.facebook.com/yasserbdj96" align="center"><img align="center" alt="facebook" src="https://img.shields.io/badge/-facebook-0088cc?style=flat-square&logo=facebook&logoColor=white"></a>
   <a href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg" align="center"><img align="center" alt="youtube" src="https://img.shields.io/badge/-youtube-ea4335?style=flat-square&logo=youtube&logoColor=white"></a>
   <a href="https://pypi.org/user/yasserbdj96" align="center"><img align="center" alt="pypi" src="https://img.shields.io/badge/-pypi-efeeea?style=flat-square&logo=pypi"></a>
</p>

<p align="center">
    BTC : 16mUJYXdNh9VkjN3MQawA8wvYJqL9F5CKZ

</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>

<div align="center">
    <a href="https://yasserbdj96.github.io"><img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/yasserbdj96/main/images/yasserbdj96.png"></a>
   <br>
    <a href="https://github.com/yasserbdj96/" align="center"><img align="center" alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.hexor"></a>
</div>
