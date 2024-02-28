#!/usr/bin/env python3
from yaml import safe_load
from json import dump

with open("photos.yml") as f:
    data = safe_load(f)

with open("photos.json", "w") as f:
    dump(data, f)
