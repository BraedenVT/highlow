all: highlow

highlow:
	pyinstaller --onefile --copy-metadata readchar highlow.py

clean:
	rm -rf build *.spec

run:
	./dist/highlow
