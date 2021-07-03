#!/usr/bin/python

import tkinter
import random
import array
import math
import importlib #separate file to do the functions for the game of life??
#import argparse

#default values and ability to change window size from arguments

def distance(x2, x1, y2, y1):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

shots = 100000 #number of dots to be added between poitns
anchorCount = 3 #change number of points(eg for a pentagon change to 5)
windowDimensions = 1000, 1000
windowMidpoint = windowDimensions[0] / 2, windowDimensions[1] / 2
firstAnchorPt = windowMidpoint[0], 100
r = distance(firstAnchorPt[0], windowMidpoint[0], firstAnchorPt[1], windowMidpoint[1])

def fractionalMidpoint(pt1, pt2, denominator):
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    return x1 + (1 / denominator) * (x2 - x1), y1 + (1 / denominator) * (y2 - y1)

def generateAnchorPts(numPts):
    ret = [[0 for i in range(2)] for j in range(numPts)]
    angle = (2 * math.pi) / numPts
    ret[0][0] = firstAnchorPt[0]
    ret[0][1] = firstAnchorPt[1]
    C.create_oval(firstAnchorPt[0] - 5, firstAnchorPt[1] - 5, firstAnchorPt[0] + 5, firstAnchorPt[1] + 5, fill='red')
    cumAngle = angle
    i = 1
    while i < numPts:
        #converting from polar coordinates into Cartesian
        nextY = -1 * (r * math.cos(cumAngle)) #needs to be flipped due to y axis pointing down in tkinter
        nextX = -1 * (r * math.sin(cumAngle)) #(x, y) becomes (-y, x) to rotate ccw as x axis now rotated pi ccw
        #print(nextX + 250, nextY + 250)
        C.create_oval(nextX + windowMidpoint[0] - 5, nextY + windowMidpoint[1] - 5, nextX + windowMidpoint[0] + 5, nextY + windowMidpoint[1] + 5, fill='red')
        ret[i][0] = nextX + windowMidpoint[0]
        ret[i][1] = nextY + windowMidpoint[1]
        cumAngle += angle
        i += 1
    return ret

def getNextPt(lastPt, arr):
    n = len(arr) - 1
    num = random.randint(0, n)
    nextAnchor = arr[num][0], arr[num][1]
    return fractionalMidpoint(nextAnchor, lastPt, n)

top = tkinter.Tk()

C = tkinter.Canvas(top, bg='black', height=windowDimensions[1], width=windowDimensions[0])
C.pack()

anchors = generateAnchorPts(anchorCount)

pt = windowMidpoint[0], windowMidpoint[1] #initialize point to wherever, really doesnt matter
i = 0
while i < shots:
    lastPt = pt
    pt = getNextPt(lastPt, anchors)
    C.create_oval(pt[0], pt[1], pt[0]+2, pt[1]+2, fill='white')
    C.update()
    i += 1

top.mainloop()