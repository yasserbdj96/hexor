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