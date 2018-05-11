#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:54:38 2018

@author: denisealfonso
"""

from shapely.geometry import Point, LineString, Polygon
import numpy as np


#Save the travelTimes_2015_Helsinki.txt into your computer.
traveldatafile = "data/travelTimes_2015_Helsinki.txt"

#Read 4 columns, i.e. 'from_x', 'from_y', 'to_x', 'to_y' from the data into 
#Python using numpy.
columns = [5,6,7,8]
traveldata = numpy.loadtxt(traveldatafile, delimiter = ';', usecols=columns, skiprows=1 )


#Create two lists called orig_points and dest_points
org_points = []
dest_points = []

#Iterate over the rows of your numpy array and add Shapely Point -objects 
#into the orig_points -list and dest_point -list representing the origin 
#locations and destination locations accordingly.

for row in traveldata:
    newpoint = Point(row[0], row[1])
    org_points.append(newpoint)
    
    
for row in traveldata:
    newpoint = Point(row[2], row[3])
    dest_points.append(newpoint)
    
#Create a list called lines
lines = []

#Iterate over the origin and destination lists and create a Shapely LineString
# -object between the origin and destination point
#Add that line into the lines -list.

for i in range(len(org_points)):
    newLS = LineString([org_points[i], dest_points[i]])
    lines.append(newLS)


#Find out what is the average (Euclidian) distance of all the 
#origin-destination LineStrings that we just created, and print it out.
linedist = length for l in lines
avgdist = np.average(linedist)


#To make things more reusable: write creation of the LineString and 
#calculating the average distance into dedicated functions and use them.


#[[p.x, p.y] for p in inputdata]

