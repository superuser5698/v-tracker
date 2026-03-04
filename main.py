import argparse
from time import sleep
from os import makedirs
files = []
def folder(folder):
    makedirs(f"c:/Users/Ayaansh_Joshi/Desktop/v-tracker-latest/v-track/{folder}")

    with open(folder, mode="r") as f:
        stuff = f.read()
    with open(f"v-track/{folder}/{folder}",mode="w") as f2:
        f2.write(stuff)

         
def start():
    global files
    
    with open("v-track/tracker.txt", 'r') as f:     
        for line in f:
            files.append(line.strip())
    while True:
        for tracked_file in files:
            with open(f"v-track/{tracked_file}/{tracked_file}", mode='r') as f3:
                with open(tracked_file, mode='r') as f4:
                    if f4.read() != f3.read():
                        




         
def run(name):
    if name == "init":
        import subprocess
     #   import os
        subprocess.run(['mkdir', 'v-track'],shell=True)
        subprocess.run(['cd', 'v-track'],shell=True)
        file = input("file: ") 
        print("addding", file, "to tracker.txt")
        with open("v-track/tracker.txt", mode="a+") as f:
      #      stoof = f.read()
       #     print(stoof)
        #    if file in stoof:
         #       print("sorry duplicates will crash the thing")
          #      exit(0)
            f.write(file)
            f.write("\n")
        folder(file)
    elif name == "read":
        with open("v-track/tracker.txt", mode="r") as f:
            print(f"files that are being tracked:\n{f.read()}")
    elif name == "add":
            file2 = input("file: ") 
            print("addding", file, "to tracker.txt")
            with open("v-track/tracker.txt", mode="a+") as f:
      #      stoof = f.read()
       #     print(stoof)
        #    if file in stoof:
         #       print("sorry duplicates will crash the thing")
          #      exit(0)
                f.write(file2)
                f.write("\n")
                folder(file2)
    elif name == "help":
         print("help:\n")
         print("commands: read write init add help")
         print("read: get list of files being tracked")
         print("add: adds a file to be tracked")
         print("init: init a folder")
         print("help: prints this help text")
    elif name == "start":
        pass
    else:
         print("sorry unkown command")

arg = argparse.ArgumentParser(description="git like program")
arg.add_argument("action", help="do something")
args = arg.parse_args()
run(args.action)
start()
