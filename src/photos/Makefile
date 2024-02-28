IMAGES=$(patsubst orig/%,%,$(wildcard orig/*))
IMAGES_2048=$(patsubst %,2048w/%,$(IMAGES))
IMAGES_1024=$(patsubst %,1024w/%,$(IMAGES))
IMAGES_512=$(patsubst %,512w/%,$(IMAGES))
IMAGES_THUMB=$(patsubst %,thumb/%,$(IMAGES))

.PHONY: all
all: dirs $(IMAGES_512) $(IMAGES_1024) $(IMAGES_2048) $(IMAGES_THUMB) photos.json

.PHONY: dirs
dirs:
	mkdir -p 512w 1024w 2048w thumb

2048w/%: orig/%
	convert $^ -resize 2048x4096 $@
	jpegoptim -s -m80 $@

1024w/%: orig/%
	convert $^ -resize 1024x2048 $@
	jpegoptim -s -m80 $@

512w/%: orig/%
	convert $^ -resize 512x1024 $@
	jpegoptim -s -m80 $@

thumb/%: orig/%
	convert $^ -thumbnail 100x100 $@
	jpegoptim -s -m80 $@

photos.json: photos.yml
	./yml-to-json.py $^ > $@

.PHONY: clean
clean:
	rm -rf 512w 1024w 2048w thumb photos.json
