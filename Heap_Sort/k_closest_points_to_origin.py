from os import *
from sys import *
from collections import *
import math
from heapq import heappush ,heappop

def distance(x,y):
    return math.sqrt(x**2 + y**2)

def KClosestPoints(points, k):
    # Write your code here.
    min_heap = []
    n = len(points)

    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        heappush(min_heap , (distance(x,y) ,points[i]))

    result = []
    for i in range(k):
        result.append(heappop(min_heap)[1])
    return result

points = [[1,3] , [-2,2]]
result = KClosestPoints(points, 1)
print(result)
