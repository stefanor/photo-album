# photo-album
A photo album script

## Instructions:

1. `apt install jpegoptim python3-pil python3-yaml npm`
1. Run `cd src && npm install` to download JS assets.
1. Edit `index.html` to taste.
1. Place photos into `src/photos/orig`.
1. Run `make -C src/photos` to build resized versions. The Makefile supports parallelism. You can pass e.g. `-j 8`.
1. Run `cd src/photos && list.py > photos.yml` to generate a basic photo listing.
1. Edit `photos.yml` to organize into sections with titles. Photos can also have titles.
1. Run `make photos.json` after editing to build JSON.
1. Preview with a simple webserver like `python3 -m http.server`.
