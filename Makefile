DATE = $(shell date +'%Y-%m-%d')
KINDLE_CLIPPINGS = $(HOME)/Documents/kindle-clippings/kindle-clippings--$(DATE).txt

test:
	echo $(KINDLE_CLIPPINGS)

all: ru2en clippy marky

ru2en:
	python ClippyKindle/russian-to-english.py /Volumes/Kindle/documents/My\ Clippings.txt $(KINDLE_CLIPPINGS)

clippy:
	python clippy.py $(KINDLE_CLIPPINGS)

marky:
	python marky.py collection.json output/

dates:
	rg -A 3 '"title"' collection.json | less -S