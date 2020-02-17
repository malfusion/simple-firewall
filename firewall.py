from utils import parseRuleLine
from rules_manager import RulesManager

class Firewall:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.rulesManager = RulesManager()
        self._loadRulesFromFile(self.filepath)
        

    def _loadRulesFromFile(self, filepath):
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                self._loadRule(line)
    
    def _loadRule(self, line):
        (dir, typ, ipstart, ipend, pstart, pend) = parseRuleLine(line)
        self.rulesManager.addRule(True, dir, typ, ipstart, ipend, pstart, pend)


    def isAllowed(self, line):
        (dir, typ, ip, _ ,  port, _ ) = parseRuleLine(',')
        return self.rules.checkRule(dir, typ, ip, port)