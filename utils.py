def convert_ip_to_number(ipstr):
    return sum([int(part) * (256**(3-indx)) for indx, part in enumerate(ipstr.split('.'))])


def parse_rule_line(rule):
    dir, typ, prange, iprange = rule.split(',')
    pstart, pend = prange, prange
    if '-' in prange:
        pstart, pend = prange.split('-')
    pstart, pend = int(pstart), int(pend)
    
    ipstart, ipend = None, None
    if '-' in iprange:
        ipstart, ipend = map(convert_ip_to_number, iprange.split('-'))
    else:
        convertedIp = convert_ip_to_number(iprange)
        ipstart, ipend = convertedIp, convertedIp
    return (dir, typ, ipstart, ipend, pstart, pend)
