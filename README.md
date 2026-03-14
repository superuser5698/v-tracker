# v-tracker
a file tracker like git but it auto commits when file is changed and has like 5 commands
commands(so far) read, init, add, help and write a
read: check what files are being tracked
write: add a file to tracker.txt
init: init a folder by creating v-track and tracker.txt inside
add: add a file to tracker.txt
help: print the help message
I have only tested on windows 11 with python installed
version: 1.00
installation:
	swithch to the builds branch and download the .exe file (only win 11 at the moment)
	when it is downloaded open it if something pops up saying Windows protected you PC jst click more info then run anyway
building or running from source:
	to build it download the main.py file and install pyinstaller(pip install pyinstaller or pip3 install pyinstaller) 
	then run
	
	python -m pyinstaller --onefile main.py

in the same folder as the main.py file (if you used pip3 then do python3 instead of python)
	to run it from source:
		download main.py
		run main.py using 
		
		python main.py
(or python3 if you have python3)

