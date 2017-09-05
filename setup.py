from setuptools import setup

from zeroconf.version import __version__ as version

name = 'gluster-zeroconf'

setup(
    name=name,
    version=version,
    description='Tools for autodiscovery of Gluster Storage servers',
    license='LGPLv3',
    author='Niels de Vos',
    author_email='ndevos@redhat.com',
    url='https://www.gluster.org',
    packages=['gluster.zeroconf'],
    package_dir={'gluster':''},
    classifiers=[
        'Development Status :: 4 - Beta'
        'Environment :: Console'
        'Intended Audience :: System Administrators'
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python'
        'Topic :: System :: Filesystems'
    ],
    install_requires=[
#        'gluster', # misses egg support?
        'zeroconf',
        'xmltodict'
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'gluster-discovery = gluster.zeroconf.cli:main'
         ]
    },
    data_files=[
        ('/etc/avahi/services', ['config/glusterd.service']),
    ],
)

