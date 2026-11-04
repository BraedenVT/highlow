.PHONY: all clean run

all: highlow

highlow:
	pyinstaller --onefile --copy-metadata readchar highlow.py

clean:
	rm -rf build dist *.spec

run:
	./dist/highlow
