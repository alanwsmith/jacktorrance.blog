#!/usr/bin/env python3

import os
base_filename = os.path.basename(__file__).split('.')[0]
output_path = f'output/{base_filename}-0.txt'

with open(output_path, 'w') as _file:
    _file.write("""~ REDRUM ~""")


