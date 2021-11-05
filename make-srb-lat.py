import os
import shutil
import subprocess


root_dir = os.path.dirname(os.path.abspath(__file__))
srb_cyr_dir = os.path.join(root_dir, 'srp')
srb_lat_dir = os.path.join(root_dir, 'srb')

shutil.rmtree(srb_lat_dir, ignore_errors=True)
os.makedirs(srb_lat_dir)

_, _, files = next(os.walk(srb_cyr_dir))
for f in files:
    with open(os.path.join(srb_cyr_dir, f), 'r') as cyr, \
            open(os.path.join(srb_lat_dir, f), 'w') as lat:
        ret = subprocess.run(['recode-sr-latin'], input=cyr.read().encode(), stdout=subprocess.PIPE)
        data = ret.stdout.decode()

        if f == 'ui.json':
            data = data.replace(
                '"Tajlandski",\n{}"Srpski"'.format(' ' * 6),
                '"Tajlandski",\n{}"Српски"'.format(' ' * 6)
            )
        lat.write(data)
