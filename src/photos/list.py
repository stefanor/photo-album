#!/bin/python3

import pathlib
import sys

import yaml
from PIL import Image

images = []
path = pathlib.Path('2048w')
for file in sorted(path.iterdir()):
    with Image.open(file) as f:
        dimensions = f.size
    images.append({
        'file': file.name,
        'max_d': f'{dimensions[0]}x{dimensions[1]}',
    })

data = {
    "sections": [
        {
            "title": "Unsorted",
            "photos": images,
        }
    ]
}
yaml.dump(data, sys.stdout)
