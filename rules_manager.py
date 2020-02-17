from range_store_list import RangeList

class RulesManager:

    def __init__(self):
        # Simple Naive List of Ranges
        self.RangeStore = RangeList
        # High performance Segment Tree Implementation (Uncomment when implemented)
        # RangeStore = SegmentTree

        self.root = {
            'inbound_tcp': self.RangeStore(),
            'outbound_tcp': self.RangeStore(),
            'inbound_udp': self.RangeStore(),
            'outbound_udp': self.RangeStore()
        }

    def addRule(self, permission, dir, pktType, startIP, endIP, startPort, endPort):
        treeKey = dir + '_' + pktType
        # Traverse to the correct Range Store first
        ipRangeStore = self.root[treeKey]
        # Create IP Range
        ipRangeStoreNode = ipRangeStore.insertRange(startIP, endIP, {'portRangeTree': self.RangeStore()})
        # Insert a Port Range within the IP Range Node
        portRangeStore = ipRangeStoreNode['data']['portRangeTree']
        portRangeStoreNode = portRangeStore.insertRange(startPort, endPort, {'perm': permission})

    def checkRule(self, dir, pktType, ip, port):
        treeKey = dir + '_' + pktType
        # Traverse to the correct Range Store first
        ipRangeTree = self.root[treeKey]
        
        # Get all Nodes that contain the IP
        ipRangeTreeNodes = ipRangeTree.findNodes(ip)

        # Get all the valid Port Range Nodes within each IP Range Node
        finalNodes = []
        for node in ipRangeTreeNodes:
            portRangeNodes = node['data']['portRangeTree'].findNodes(port)
            # Return early if Allow Node is present
            if (any(node['data']['perm'] for node in portRangeNodes)):
                return True
        return False

    