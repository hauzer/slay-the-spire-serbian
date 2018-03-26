#!/usr/bin/env python3

import os
import subprocess


root_dir = os.path.dirname(os.path.abspath(__file__))
srb_cyr_dir = os.path.join(root_dir, 'srb-cyr')
srb_lat_dir = os.path.join(root_dir, 'srb-lat')

os.makedirs(srb_lat_dir, exist_ok=True)
_, _, files = next(os.walk(srb_cyr_dir))

for f in files:
    with open(os.path.join(srb_cyr_dir, f), 'rb') as cyr, \
            open(os.path.join(srb_lat_dir, f), 'wb') as lat:
        ret = subprocess.run(['recode-sr-latin'], input=cyr.read(), stdout=subprocess.PIPE)
        lat.write(ret.stdout)
