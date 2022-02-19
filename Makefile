DATE = $(shell date +'%Y-%m-%d')
KINDLE_CLIPPINGS = $(HOME)/Documents/kindle-clippings/kindle-clippings--$(DATE).txt

test:
	echo $(KINDLE_CLIPPINGS)

all: ru2en clippy marky

ru2en:
	python ClippyKindle/russian-to-english.py /Volumes/Kindle/documents/My\ Clippings.txt ~/Documents/$KINDLE_CLIPPINGS

clippy:
	python clippy.py ~/Documents/kindle-clippings--$(DATE).txt

marky:
	./marky.py collection.json output/