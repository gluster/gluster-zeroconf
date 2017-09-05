import argparse
import os

from .actions import discover_hosts, connected_peers, peer_probe

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timeout', help='seconds to wait for replies', type=int, default=5)
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='count')
    parser.add_argument('action', help='command to execute', choices=['discover', 'probe'], default='discover', nargs='?')

    try:
        args = parser.parse_args()
    except:
        return os.EX_USAGE

    hosts = discover_hosts(args.timeout)
    for host in hosts:
        print('discovered host: %s' % (host))

    peers = connected_peers()
    for peer in peers:
        print('connected peer: %s' % (peer))

    if args.action == 'probe':
        for host in hosts:
            if host not in peers:
                # TODO: resolve all IPs to hostnames
                peer_probe(host)

    return os.EX_OK
