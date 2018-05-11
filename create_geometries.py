#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:04:42 2018

@author: denisealfonso
"""
#install numpy
#install shapely

from shapely.geometry import Point, LineString, Polygon
import numpy

def createPointGeom(x_coord, y_coord): 
    #Function should create a shapely Point geometry object and return that
    return Point(x_coord, y_coord)

test1 = createPointGeom(1,2)
    
def createLineGeom(ptlist):
    #takes a list of Shapely Point objects as parameter and returns 
    #a LineString object of those input points. Function should first 
    #check that the input list really contains Shapely Point(s)
    
    for pt in ptlist: 
        if type(pt) != shapely.geometry.point.Point:
            print("Not a Shapely Point")
            return

    return LineString(ptlist)
        
    
def createPolyGeom(inputdata):
    #takes a list of coordinate tuples OR a list of Shapely Point objects and
    #creates/returns a Polygon object of the input data. Both ways of passing
    #the data to the function should be working
    
    #inputdata is list of coord tuples or list of Shapely Point objects
    #for data in inputdata:
    
    if len(inputdata) < 3 :
        print("Denise you idiot you forgot that you need 3 points to make a plane")
        return

    if all(isinstance(x, tuple) for x in inputdata):
        return Polygon(inputdata)
    
    elif all(isinstance(x, shapely.geometry.point.Point) for x in inputdata):
        return Polygon([[p.x, p.y] for p in inputdata])
    
    else:
        print("Not a list of coordinate tuples or list of Shapely Points")
        return
    
    
