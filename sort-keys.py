#!/usr/bin/env python3

from collections import OrderedDict
import json
import os


dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'srp')

_, _, files = next(os.walk(dir_path))
for f in files:
    with open(os.path.join(dir_path, f), 'r+', encoding='utf8') as f:
        data = json.load(f)
        f.seek(0)
        f.truncate()
        json.dump(OrderedDict(sorted(data.items())), f, ensure_ascii=False, indent=2)
