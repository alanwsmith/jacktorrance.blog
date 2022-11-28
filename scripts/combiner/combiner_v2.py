#!/usr/bin/env python3

import glob
import os
import sys

script_dir = sys.path[0]
source_dir = os.path.abspath(os.path.join(
    script_dir, '..', 'page_makers', 'output'
))

for i in range(1, 100):
    files = [
        file for file in glob.glob(f"{source_dir}/{i}-*")
    ]

    files.sort()

    for file in files:
        with open(file) as _in:
            max_length = 0
            data = _in.read()
            lines = data.split("\n")
            for line in lines:
                max_length = max(max_length, len(line))
            
            if max_length > 57:
                print(file)










