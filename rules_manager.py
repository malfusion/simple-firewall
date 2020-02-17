from range_store_list import RangeList

class RulesManager:

    def __init__(self):
        # Simple Naive List of Ranges
        RangeStore = RangeList
        # High performance Segment Tree Implementation (Uncomment when implemented)
        # RangeStore = SegmentTree

        self.root = {
            'inbound_tcp': RangeStore(),
            'outbound_tcp': RangeStore(),
            'inbound_udp': RangeStore(),
            'outbound_udp': RangeStore(),
        }

    def add_rule(self, permission, dir, typ, ipstart, ipend, pstart, pend):
        pass

    