def convertIpToNumber(ipstr):
    return sum([int(part) * (256**(3-indx)) for indx, part in enumerate(ipstr.split('.'))])


def parseRuleLine(rule):
    dir, typ, prange, iprange = rule.split(',')
    pstart, pend = prange, prange
    if '-' in prange:
        pstart, pend = prange.split('-')
    pstart, pend = int(pstart), int(pend)
    
    ipstart, ipend = None, None
    if '-' in iprange:
        ipstart, ipend = map(convertIpToNumber, iprange.split('-'))
    else:
        convertedIp = convertIpToNumber(iprange)
        ipstart, ipend = convertedIp, convertedIp
    return (dir, typ, ipstart, ipend, pstart, pend)
