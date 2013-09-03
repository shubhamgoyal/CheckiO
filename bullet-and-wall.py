import math

def checkio(data):

    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]

    #replace this for solution
    #return True or False
    
    vecW1W2x = xw2 - xw1
    vecW1W2y = yw2 - yw1
    vecABx = xb - xa
    vecABy = yb - ya

    dirW1W2x = vecW1W2x/math.sqrt(vecW1W2x * vecW1W2x + vecW1W2y * vecW1W2y)
    dirW1W2y = vecW1W2y/math.sqrt(vecW1W2x * vecW1W2x + vecW1W2y * vecW1W2y)

    dirABx = vecABx/math.sqrt(vecABx * vecABx + vecABy * vecABy)
    dirABy = vecABy/math.sqrt(vecABx * vecABx + vecABy * vecABy)
    
    if (dirABx * dirW1W2y - dirABy * dirW1W2x) == 0.0:
        if ((xw1 - xa)/dirABx == (yw1 - ya)/dirABy) and ((xw1 - xa)/dirABx > 0):
            return True
        else:
            return False
    if (dirW1W2x * dirABy - dirW1W2y * dirABx) == 0.0:
        if ((xw1 - xa)/dirABx == (yw1 - ya)/dirABy) and ((xw1 - xa)/dirABx > 0):
            return True
        else:
            return False
    
    t = (xw1 * dirW1W2y - yw1 * dirW1W2x - xa * dirW1W2y + ya * dirW1W2x)/(dirABx * dirW1W2y - dirABy * dirW1W2x)
    s = (xa * dirABy - ya * dirABx - xw1 * dirABy + yw1 * dirABx)/(dirW1W2x * dirABy - dirW1W2y * dirABx)
    
    if t < 0:
        return False;
    if s < 0:
        return False;
        
    if ((s * dirW1W2x + xw1) > xw2) and ((s * dirW1W2x + xw1) > xw1):
        return False;
        
    if ((s * dirW1W2x + xw1) < xw2) and ((s * dirW1W2x + xw1) < xw1):
        return False;
    
    return True;

#Some hints
#You can search intersection point for lines
#Or look to rays geometry


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "1st example"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"
