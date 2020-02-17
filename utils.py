def convert_ip_to_number(ipstr):
    return sum([int(part) * (256**(3-indx)) for indx, part in enumerate(ipstr.split('.'))])


