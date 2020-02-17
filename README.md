# simple-firewall
A firewall that efficiently implements only allow rules on network traffic.

# Usage
python main.py
- Make sure that the rules are present in 'rules.csv' within the same directory as the main script.

# Testing
python tests.py

# Things to Note
- We convert IPv4 addresses and IPv4 address ranges to an integer, because any ip range specified will be contiguous in the integer domain.
- However we cannot include the port range into this, because ip-port combination ranges need not be contiguous and there will be multiple disconnections. Eg: 10.1.1.1-10.1.1.5 35000-36000: The ports 35000-36000 is contiguous for the first ip in the ip range, and then after a large gap, we will encounter the next IP's 35000-36000. So we do not include the port together with the ip during conversion.


