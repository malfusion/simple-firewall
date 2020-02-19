import unittest
from range_store_list import RangeList
from firewall import Firewall



class RangeListTest(unittest.TestCase):
    def test(self):
        store = RangeList()

        # Test single range
        store.insertRange(10, 20, {'1': 'one'})
        self.assertEqual(len(store.findNodes(10)), 1)
        self.assertEqual(len(store.findNodes(9)), 0)
        self.assertEqual(len(store.findNodes(21)), 0)

    
        # Test overlapping ranges
        store.insertRange(10, 15, {'2': 'two'})
        store.insertRange(17, 25, {'3': 'three'})
        self.assertEqual(len(store.findNodes(9)), 0)
        self.assertEqual(len(store.findNodes(10)), 2)
        self.assertEqual(len(store.findNodes(12)), 2)
        self.assertEqual(len(store.findNodes(15)), 2)
        self.assertEqual(len(store.findNodes(16)), 1)
        self.assertEqual(len(store.findNodes(17)), 2)
        self.assertEqual(len(store.findNodes(21)), 1)
        self.assertEqual(len(store.findNodes(26)), 0)

        
        # Test single point
        store.insertRange(20, 20, {'4': 'four'})
        self.assertEqual(len(store.findNodes(19)), 2)
        self.assertEqual(len(store.findNodes(20)), 3)
        self.assertEqual(len(store.findNodes(21)), 1)

        # Test nodes returned, and order of nodes
        res = store.findNodes(20)
        expected = [{'1': 'one'}, {'3': 'three'}, {'4': 'four'}]
        self.assertEqual(len(res), len(expected))
        for i in range(len(res)):
            self.assertDictEqual(res[i]['data'], expected[i])

 
class FirewallTest(unittest.TestCase):
    def test(self):
        firewall = Firewall('./rules.csv')
        
        # `Test Rules`
        # inbound,tcp,80,192.168.1.2
        # outbound,tcp,10000-20000,192.168.10.11
        # inbound,udp,53,192.168.1.1-192.168.2.5
        # outbound,udp,1000-2000,52.12.48.92
        # inbound,tcp,65535,255.255.255.255

        self.assertEqual(firewall.accept_packet('inbound','tcp',80,'192.168.1.1'), False)
        self.assertEqual(firewall.accept_packet('inbound','tcp',80,'192.168.1.2'), True)

        self.assertEqual(firewall.accept_packet('inbound','tcp',10000,'192.168.10.11'), False)
        self.assertEqual(firewall.accept_packet('outbound','tcp',10000,'192.168.10.11'), True)
        self.assertEqual(firewall.accept_packet('inbound','tcp',20000,'192.168.10.11'), False)
        self.assertEqual(firewall.accept_packet('outbound','tcp',20000,'192.168.10.11'), True)
        self.assertEqual(firewall.accept_packet('inbound','tcp',15000,'192.168.10.11'), False)
        self.assertEqual(firewall.accept_packet('outbound','tcp',15000,'192.168.10.11'), True)
        self.assertEqual(firewall.accept_packet('inbound','udp',15000,'192.168.10.11'), False)
        self.assertEqual(firewall.accept_packet('outbound','udp',15000,'192.168.10.11'), False)

        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.1.1'), True)
        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.1.15'), True)
        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.1.255'), True)
        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.2.1'), True)
        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.2.5'), True)
        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.2.6'), False)
        self.assertEqual(firewall.accept_packet('inbound','udp',53,'192.168.3.1'), False)

        self.assertEqual(firewall.accept_packet('outbound','udp',999,'52.12.48.92'), False)
        self.assertEqual(firewall.accept_packet('outbound','udp',1000,'52.12.48.92'), True)
        self.assertEqual(firewall.accept_packet('outbound','udp',1500,'52.12.48.92'), True)
        self.assertEqual(firewall.accept_packet('outbound','udp',2000,'52.12.48.92'), True)
        self.assertEqual(firewall.accept_packet('outbound','udp',2001,'52.12.48.92'), False)
        self.assertEqual(firewall.accept_packet('outbound','tcp',1500,'52.12.48.92'), False)
        self.assertEqual(firewall.accept_packet('inbound','udp',1500,'52.12.48.92'), False)

        self.assertEqual(firewall.accept_packet('inbound','tcp',65535,'255.255.255.255'), True)
        self.assertEqual(firewall.accept_packet('inbound','tcp',65534,'255.255.255.255'), False)
        self.assertEqual(firewall.accept_packet('inbound','tcp',1,'1.1.1.1'), False)


if __name__ == '__main__':
    unittest.main()