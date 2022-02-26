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
