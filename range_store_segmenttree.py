class SegmentTreeNode():
    """
    The Segment Tree Node stores the ranges that overlap with the midpoint of the node's responsible domain space.
    It also stores the max value of all the ranges in itself and its right subtree, 
    so as to decide whether to traverse to it during lookups.
    """
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.mid = l + ((r-l)//2)
        self.max = 1
        self.ranges = []
        self.left = None
        self.right = None
    
    def insertRange(self, start, end, data):
        mx = end
        if (end < self.mid):
            if not self.left:
                self.left = SegmentTreeNode(self.l, self.mid)
            mx = self.left.insertRange(start, end, data)
            
        elif (self.mid < start):
            if not self.right:
                self.right = SegmentTreeNode(self.mid, self.r)
            self.right.insertRange(start, end, data)
        else:
            self.ranges.append({
                'start': start,
                'end': end,
                'data': data
            })
        self.max = max(self.max, mx)
        return self.max
    


class SegmentTree():
    """
    The Segment Tree implementation divides the entire input domain by half at every level,
    and stores those ranges within itself which overlap with the midpoint of the node's input domain.
    """
    def __init__(self):
        self.root = SegmentTreeNode(1, 255*255*255*255)

    def findNodes(self, point):
        """Finds all the ranges in the segmentTree that overlap with the given point"""
        stack = [self.root]
        res = []
        while stack:
            node = stack.pop()
            if(point <= node.max):
                for rangeNode in node.ranges:
                    if rangeNode['start'] <= point <= rangeNode['end']:
                        res.append(rangeNode)
            if node.left and point <= node.left.max:
                stack.append(node.left)
            if node.right and point >= node.right.l:
                stack.append(node.right)
        return res

    def insertRange(self, start, end, data):
        """Inserts the given range into the segmentTree"""
        self.root.insertRange(start, end, data)

    def _printNodes(self):
        """Prints the nodes for debugging purposes"""
        print(self.nodes)

