from utils import parse_rule_line
from rules_manager import RulesManager

class Firewall:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self._load_rules_from_file(self.filepath)
        self.rule_manager = RulesManager()
        

    def _load_rules_from_file(self, filepath):
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                self._load_rule(line)
    
    def _load_rule(self, line):
        (dir, typ, ipstart, ipend, pstart, pend) = parse_rule_line(line)
        self.rule_manager.add_rule(True, dir, typ, ipstart, ipend, pstart, pend)


    def is_point_valid(self, point):
        pass