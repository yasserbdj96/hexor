hexor texts color
==========================
hexor for color the texts in hex or rgb colors.

.. image:: https://travis-ci.com/byRo0t96/hexor.svg?branch=main

Installation
============

.. code::

    pip install hexor

Usage
=====
.. code:: python

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

.. begin changelog

Example
=====
.. code:: python

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
    p1=hexor(False,"rgb")
    print(p1.c("Text is red","255,0,0"))
    print(p1.c("Text is red and background is blue","255,0,0","26,115,232"))
	
	# Example:5
    hexor(False,"hex").c("Text is red","#ff0000")# hexor().c("Text is red","#ff0000")
    hexor(False,"rgb").c("Text is red and background is blue","255,0,0","26,115,232")
	
.. begin changelog

Changelog
=========

0.0.2
-----
- Fix bugs.
- Add RGB type.

0.0.1
-----
- First public release.

.. end changelog
