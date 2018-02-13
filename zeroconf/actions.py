from time import sleep
import socket
from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf
from subprocess import Popen, PIPE
import xmltodict

__all__ = [
    'discover_hosts',
    'connected_peers',
    'peer_probe'
]

glusterd_hosts = []

def _on_service_state_change(zeroconf, service_type, name, state_change):
    """ Event handler for zeroconf.ServideBrowser()
    """
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            glusterd_hosts.append(socket.inet_ntoa(info.address))


def discover_hosts(timeout=5):
    """ Find hosts that announce themselves with _glusterd._tcp.local.
    """
    zeroconf = Zeroconf()
    browser = ServiceBrowser(zeroconf, '_glusterd._tcp.local.',
                             handlers=[_on_service_state_change])

    sleep(timeout)
    zeroconf.close()

    return glusterd_hosts


def connected_peers():
    """ List connected peers as given by GlusterD.
    """
    peers = []

    cli = Popen('gluster --xml pool list', shell=True, stdout=PIPE, stderr=PIPE)
    (out, err) = cli.communicate()
    # TODO: catch errors (not even xml format when glusterd is not running)

    """ example output:
    # TODO: verify for multiple hosts

    <cliOutput>
      <opRet>0</opRet>
      <opErrno>0</opErrno>
      <opErrstr/>
      <peerStatus>
        <peer>
          <uuid>28724efd-b1dd-4d6b-8012-1dfe8d2c698a</uuid>
          <hostname>localhost</hostname>
          <connected>1</connected>
        </peer>
      </peerStatus>
    </cliOutput>
    """

    result = xmltodict.parse(out)
    if not (result['cliOutput'] and result['cliOutput']['peerStatus']):
        return peers

    for peer in result['cliOutput']['peerStatus']['peer']:
        hostname = peer['hostname']
        if hostname != 'localhost':
            peers.append(hostname)

    return peers


def peer_probe(hostname):
    """ Run 'gluster peer probe $hostname' against the given hostname (or IP).
    """
    cli = Popen('gluster --xml peer probe %s' % hostname, shell=True, stdout=PIPE, stderr=PIPE)
    (out, err) = cli.communicate()

    # TODO: catch errors

    return None
