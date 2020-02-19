import argparse
from firewall import Firewall


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Create a firewall using the \'allow\' rules provided as input.')
    parser.add_argument('rules_path', type=str, help='Path to csv file that contains the rules seperated by newlines')

    args = parser.parse_args()

    # Construct firewall object which reads given file
    firewall = Firewall(args.rules_path)
    
    # Simple tests
    print('Input:', 'inbound', 'tcp', 80, '192.168.1.1')
    print('Output:', firewall.accept_packet('inbound', 'tcp', 80, '192.168.1.1'))
    print('Input:', 'inbound', 'tcp', 80, '192.168.1.2')
    print('Output:', firewall.accept_packet('inbound', 'tcp', 80, '192.168.1.2'))
