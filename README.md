# simple-firewall
A firewall that efficiently implements only allow rules on network traffic.

## Usage
``` bash
python main.py <rulesFilePath>
```
rulesFilePath is a csv file that contain one rule per line

`python main.py ./rules.csv`


 
### Testing
`python tests.py`
- Tests have been written using unittest package
- The List of Ranges implementation (underlying algorithm) and the Firewall class (the public interface) as a whole have been tested.


### Implementation
- The Firewall can either use a 'List of Ranges' implementation or a Segment Tree Implementation. 
- Currently the 'List of Ranges' Implementation is working and fully tested.
- SegmentTree Implementation is not yet complete.
- We convert IPv4 addresses and IPv4 address ranges to an integer from 0 - 2^32-1, because any IP range will be contiguous in the integer domain and can be used as a valid interval.
- However we cannot include the port in the integer conversion, because IP-port combination ranges need not be contiguous in the integer domain and there could be multiple disconnected ranges. 
  - Eg: 10.1.1.1-10.1.1.5 35000-36000
  - The ports 35000-36000 is contiguous within 10.1.1.1, and then after a large gap, we will encounter the next IP's 35000-36000. So I decided not to include the port number with the integer conversion.
  - Instead we nest the port range data structure within the IP range data structure.
- Since we only need one rule to approve a packet, we perform early stopping in the algorithm the moment we find a valid rule that allows the packet.


### Refinements:
- The progress of the segment tree will be continued in the repo https://github.com/malfusion/interval-ds and later integrated into this repository.
- Adding deny rules could follow the same method, with one caveat being that we can have a wider allow range and after that rule having a smaller deny range within it.
  - To implement this, we can add a counter to each rule inserted, so that after we obtain all the matched rules, we can use the rule that has the highest counter value (ie, the rules that were farther down the rules.csv file as they overwrite previous rules)
  - Alternate strategies such as fail-fast (to deny on the first matched deny range) can also be implemented similarly.
- Randomised tests can be added to provide a wider test coverage of the input domain.


### Team Interest (By priority):
1. Platform Team
2. Data Team