from distutils.core import setup

import netlib

setup(
    name='netlib',
    version=netlib.__version__,
    url='https://github.com/jtdub/netlib',
    author='James Williams',
    license='MIT',
    install_requires=['ecdsa>=0.13', 'paramiko>=1.15.2', 'pyasn1>=0.1.8', 'pycrypto>=2.6.1', 'pysnmp>=4.2.5'],
    description='Simple access to network devices, such as routers and switches, via Telnet, SSH, and SNMP',
    packages=['netlib',],
    )
