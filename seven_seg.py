#!/usr/bin/python

from numbersdef import *

"""
Subject of the contest is to code the shortest possible python module that
converts decimal numbers to the seven-segment display format. To support
leading zeroes the decimal number is given as a string.

A string containing "23" will result in:

	 _  _
	 _| _|
	|_  _|
Or more precisely in the string:

" _  _ \n _| _|\n|_  _|\n"
The module has to be named seven_seg and has to define the function seven_seg.
The function seven_seg takes a string as parameter and returns a string.
         _      _      _     _
  |      _|    |_       |   |_|
  |      _|     _|      |    _|

 _              _      _     _
 _|     |_|    |_     |_|   | |
|_        |    |_|    |_|   |_|
"""

import sys

def printNums(numList):
	if not isinstance(numList, list):
		numList = [numList]
	for row in range(3):
		for numIter in range(len(numList)):
			print ''.join(numList[numIter][row]),
		print "\n",

printNums([Eight, Two, Four, Six, Nine])
printNums(Two)
