#!/usr/bin/env python3

import os
import sys

script_dir = sys.path[0]
output_dir = os.path.join(script_dir, "output")

contents = [
'All work and no play makes Jack a dull boy',
'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy''',
'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy''',
'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy''',
'''All WORK AND NO PLAY makes JACK a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy''',

'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy''',
'''All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy'''
] 


for index, content in enumerate(contents):
    output_path = os.path.join(output_dir, f"00-{index}.txt")
    with open(output_path, 'w') as _out:
        _out.write(content)





