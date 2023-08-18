def checkStraightLine(c):
        x0 = c[0][0] 
        y0 = c[0][1]
        x1 = c[1][0] 
        y1 = c[1][1]
        
       

        for i in range(2,len(c)):
            x = c[i][0]
            y = c[i][1]
             
            if (y1-y0)*(x - x0) != (y - y0)*(x1-x0):
                return False
        return True 

c = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
if checkStraightLine(c):
     print("The points are collinear :)")
else:
     print("The points are not collinear :(")