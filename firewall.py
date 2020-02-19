from utils import parseRuleLine, convertIpToNumber
from rules_manager import RulesManager


class Firewall:
    """The Firewall class implements the public interfaces required to load the rules 
     of the firewall and to check if a packet is allowed through the firewall rules"""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.rulesManager = RulesManager()
        # Call a private method to load the rules from the file
        self._loadRulesFromFile(self.filepath)

    #Public interface        
    
    def accept_packet(self, direction, protocol, port, ip_address):
        """Check if an input is allowed with reference to the rules stored"""
        return self.rulesManager.checkPacket(direction, protocol, convertIpToNumber(ip_address), port)

    
    # Private Methods

    def _loadRulesFromFile(self, filepath):
        """Reads a file, loads the rules line by line from it"""
        with open(self.filepath, 'r') as f:
            # Load each line of the file
            for line in f.readlines():
                self._loadRule(line)
    
    
    def _loadRule(self, line):
        """Parses one line of text that contains a single rule"""
        (dir, typ, ipstart, ipend, pstart, pend) = parseRuleLine(line)
        self.rulesManager.addRule(True, dir, typ, ipstart, ipend, pstart, pend)


    