#!/usr/bin/python3
import os
import sys

if os.path.isdir(sys.argv[1]):
    os.system("pkexec dde-file-manager " + sys.argv[1])
