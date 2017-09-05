# python-gluster does not have python3 support yet
#%%global with_python3 1

Name:		gluster-zeroconf
Version:	0.1.0
Release:	1%{?dist}
%global sum	Automatic discovery for Gluster Storage servers
Summary:	%{sum}

License:	LGPLv3
URL:		https://github.com/nixpanic/gluster-zeroconf
Source0:	gluster-zeroconf-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel, python2-gluster
%if 0%{?with_python3}
BuildRequires:	python3-devel, python3-gluster
%endif

%description
gluster-zeroconf is project that provides an autodiscovery mechanism for
Gluster Storage Servers. It uses Avahi to register a GlusterD service, and
provides `gluster-discovery` that can be used to display the storage servers
that announce themselves.

%package -n python2-%{name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{name}}
Requires:	glusterfs-cli
Requires:	python2-zeroconf, python2-xmltodict, python2-gluster

%description -n python2-%{name}
gluster-zeroconf is project that provides an autodiscovery mechanism for
Gluster Storage Servers. It uses Avahi to register a GlusterD service, and
provides `gluster-discovery` that can be used to display the storage servers
that announce themselves.

This package provides `gluster-discovery` and the Python libraries to discover
storage servers.

%if 0%{?with_python3}
%package -n python3-%{name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{name}}
Requires:	glusterfs-cli
Requires:	python3-zeroconf, python3-xmltodict, python3-gluster

%description -n python3-%{name}
gluster-zeroconf is project that provides an autodiscovery mechanism for
Gluster Storage Servers. It uses Avahi to register a GlusterD service, and
provides `gluster-discovery` that can be used to display the storage servers
that announce themselves.

This package provides the Python libraries to discover storage servers.
%endif


%package -n %{name}-avahi
Summary:	%{sum}
Requires:	glusterfs-server
Requires:	avahi

%description -n %{name}-avahi
gluster-zeroconf is project that provides an autodiscovery mechanism for
Gluster Storage Servers. It uses Avahi to register a GlusterD service, and
provides `gluster-discovery` that can be used to display the storage servers
that announce themselves.

This package provides the configuration for Avahi, and makes the system
discoverable.


%prep
%setup -q


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%files -n python2-%{name}
%license COPYING COPYING.LESSER
%doc README.rst
%{python2_sitelib}/*
%if ! 0%{?with_python3}
%{_bindir}/gluster-discovery
%endif


%if 0%{?with_python3}
%files -n python3-%{name}
%license COPYING COPYING.LESSER
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/gluster-discovery
%endif


%files -n %{name}-avahi
# dropping the file in the avahi/services directory activates it immediately
/etc/avahi/services/glusterd.service


%changelog
* Fri Aug 25 2017 Niels de Vos <ndevos@redhat.com> - 0.1.0-1
- Initial packaging
