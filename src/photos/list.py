#!/bin/python3

import pathlib
import sys

import yaml
from PIL import Image, ExifTags

images = []
path = pathlib.Path('2048w')
orientation_tag = [tag for tag in ExifTags.TAGS.keys() if ExifTags.TAGS[tag] == 'Orientation'][0]
for file in sorted(path.iterdir()):
    with Image.open(file) as f:
        dimensions = f.size
        if f.getexif() is not None:
            exif=dict(f.getexif().items())
            if (orientation_tag in exif) and (exif[orientation_tag] in (6, 8)):
                max_d = f'{dimensions[1]}x{dimensions[0]}'
            else:
                max_d = f'{dimensions[0]}x{dimensions[1]}'
        else:
            max_d = f'{dimensions[0]}x{dimensions[1]}'

    images.append({
        'file': file.name,
        'max_d': max_d,
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
