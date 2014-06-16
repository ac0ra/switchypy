#!/bin/env python
###
###
###
Author = 'Adam Grigolato'
Version = '0'
###
###
###

import ciscoconfparse
import os, getpass
from twisted.python.filepath import FilePath
from twisted.python.usage import Options
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import UNIXClientEndpoint
from twisted.conch.ssh.keys import EncryptedKeyError, Key
from twisted.conch.client.knownhosts import KnownHostsFile
from twisted.conch.endpoints import SSHCommandClientEndpoint
