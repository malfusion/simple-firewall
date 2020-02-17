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

    def add_rule(self, permission, dir, pktType, startIP, endIP, startPort, endPort):
        treeKey = dir + '_' + pktType
        ipRangeStore = self.root[treeKey]
        ipRangeStoreNode = ipRangeStore.insertRange(startIP, endIP, {'portRangeTree': self.RangeStore()})
        portRangeStore = ipRangeStoreNode['data']['portRangeTree']
        portRangeStoreNode = portRangeStore.insertRange(startPort, endPort, {'perm': permission})

    