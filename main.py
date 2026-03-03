import argparse
files = []
def line():
    with open("v-track/tracker.txt", 'r') as f:
        return sum(1 for line in f)
def start():
    while True:
            with open("v-track/tracker.txt", 'r') as f:     
                 for line in f:
                      files.append(line.strip())
            print(files)          
         
def run(name):
    if name == "init":
        import subprocess
        import os
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
    elif name == "read":
        with open("v-track/tracker.txt", mode="r") as f:
            print(f"files that are being tracked:\n{f.read()}")
    elif name == "add":
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
    elif name == "help":
         print("help:\n")
         print("commands: read write init add help")
         print("read: get list of files being tracked")
         print("add: adds a file to be tracked")
         print("init: init a folder")
         print("help: prints this help text")

arg = argparse.ArgumentParser(description="git like program")
arg.add_argument("action", help="do something")
args = arg.parse_args()
run(args.action)
start()
