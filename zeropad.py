#!/usr/bin/env python
import os
euler_dir = os.path.expanduser('~/bin/euler')
for directory in os.listdir(euler_dir):
    if os.path.isdir(directory) and directory.isdigit():
        os.rename(os.path.join(euler_dir, directory), os.path.join(euler_dir, "%03i" % int(directory)))
