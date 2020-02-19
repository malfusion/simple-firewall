class RangeList:
    """A Naive Implementation of a range checker, that uses a list of ranges, each containing some custom data"""

    def __init__(self):
        self.nodes = []

    def findNodes(self, point):
        """Finds all the ranges in the list that overlap with the given point"""
        return [node for node in self.nodes if node['start']<=point<=node['end']]
            

    def insertRange(self, start, end, data):
        """Inserts the given range into the list of ranges"""
        node = {
            'start': start,
            'end': end,
            'data': data
        }
        self.nodes.append(node)
        return node

    def _printNodes(self):
        """Prints the nodes for debugging purposes"""
        print(self.nodes)