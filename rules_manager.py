from range_store_list import RangeList

class RulesManager:
    """RulesManager object stores the rules and abstracts away the underlying datastructure that is used.
    Current rule storage layer implementations include RangeList or SegmentTree"""

    def __init__(self):
        
        # RangeStore can be either a RangeList / SegmentTree
        self.RangeStore = RangeList # or SegmentTree
        
        # Keep track of multiple RangeStores to facilitate parallel independent lookups if the application is scaled to multiple processors
        self.root = {
            'inbound_tcp': self.RangeStore(),
            'outbound_tcp': self.RangeStore(),
            'inbound_udp': self.RangeStore(),
            'outbound_udp': self.RangeStore()
        }


    def addRule(self, permission, dir, pktType, startIP, endIP, startPort, endPort):
        """Add a rule to the RangeStore"""
        # Traverse to the correct Range Store first
        treeKey = dir + '_' + pktType
        ipRangeStore = self.root[treeKey]
        
        # Create IP Range
        ipRangeStoreNode = ipRangeStore.insertRange(startIP, endIP, {'portRangeTree': self.RangeStore()})
        
        # Insert a Port Range within the IP Range Node
        portRangeStore = ipRangeStoreNode['data']['portRangeTree']
        portRangeStoreNode = portRangeStore.insertRange(startPort, endPort, {'perm': permission})

    
    def checkPacket(self, dir, pktType, ip, port):
        """Check if a certain packet is allowed to pass using the stored rules"""
        # Traverse to the correct Range Store first
        treeKey = dir + '_' + pktType
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
        # If no range is found, then the packet is not allowed
        return False

    