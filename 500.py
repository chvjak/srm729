#https://www.youtube.com/watch?v=qLnMoPPMX9Q
#https://www.youtube.com/watch?v=NeU3SY21aMA
#https://www.youtube.com/watch?v=f4mXJGEKBaA

'''
Several rectangles are on the plane, some possibly overlapping others. The rectangles are described in s x1, y1, x2 and y2. Rectangle i has it's lower-left corner (x1[i], y1[i]), and upper-right corner (x2[i], y2[i]).

Two or more rectangles overlap if they have a common area. Meeting along an edge or a corner only is not an overlap. Return the largest number of rectangles that overlap.
'''

import sys

class IntervalTree:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.maxop = r #max on path
        self.left = None
        self.right = None

def add(self, root, node):

    if node.l < root.l:
        if root.left is None:
            root.left = node
        else:
            add(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            add(root.right, node)

    root.maxop = max(root.maxop, node.maxop)

def intersects(root, node):
    return False


import bisect
class SoManyRectangles:
    def maxOverlap(self, x1arr, y1arr, x2arr, y2arr):
        res = 0

        rects = []
        rects_x1 = []
        min_x = sys.maxsize
        max_x = -sys.maxsize
        for (x1, y1, x2, y2) in zip(x1arr, y1arr, x2arr, y2arr):
            rects.append((x1, y1, x2, y2))
            rects_x1.append(x1)
            min_x = min(min_x, x1, x2)
            max_x = max(max_x, x1, x2)

        rects.sort(key=lambda x: x[0])
        rects_x1.sort()

        active_rects = IntervalTree()
        for x in range(min_x, max_x):
            #add rects which x1 < x <x2 (bsec) to active_rects

            bs_l = bisect.bisect_left(rects_x1, x)
            bs_r = bisect.bisect_right(rects_x1, x)
            for x1,y1,x2,y2  in rects[bs_l:bs_r]:
                add(active_rects, IntervalTree(y1, y2))

            # remove those rects which become inactive from active_rects
            # how?
            ...

            # check each vs each other in active rects for intersection
            # get max intersect







        return res
