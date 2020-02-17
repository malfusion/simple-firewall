class RangeList:

    def __init__(self):
        self.nodes = []

    def findNodes(self, point):
        return [node for node in self.nodes if node['start']<=point<=node['end']]
            

    def insertRange(self, start, end, data):
        node = {
            'start': start,
            'end': end,
            'data': data
        }
        self.nodes.append(node)
        return node

    def _printNodes(self):
        print(self.nodes)