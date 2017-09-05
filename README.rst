gluster-zeroconf is project that provides an autodiscovery mechanism for
Gluster Storage Servers. It uses [Avahi](http://www.avahi.org/) to register a
GlusterD service, and provides `gluster-discovery` that can be used to display
the storage servers that announce themselves.


# Installation

The recommended installation method is though RPMs. Building the RPMs is
trivial:

    $ python setup.py sdist
    $ rpmbuild -ta dist/gluster-zeroconf-0.1.0.tar.gz


# Usage

1. On a storage server that should become discoverable, install the
   gluster-zeroconf-avahi RPM. This will automatically pull in the avahi
   package as well. Avahi should haveb be enabled after it got installed.

2. On at least one storage server, install the python-gluster-zeroconf RPM.
   This package provides the `gluster-discovery` tool.

After installation, run `gluster-discovery` to list the storage servers that
announce themselves. It is possible to let `gluster-discovery` do a `gluster
peer probe` for all discovered servers with:

    \# gluster-discovery probe


# Limitations

Avahi uses the Zeroconf protocols (multicat DNS/DNS-SD) for service
announcement and discovery. For this to work, multicast needs to be available
on the (local) network. There are most likely limitations in public/private
cloud environments and networks that span multiple subnets.


# TODO

This project has just started as a proof-of-concept and there are many
improvements possible. The following is a list in no particular order:

- filter servers that do not need `gluster peer probe`
- report a warning for a failed `gluster peer probe`
- resolve the hostnames of the discovered storage servers
- ... 
