
import os, time, argparse, time

            
files = []

def folder(folder):
    os.makedirs(f"c:/Users/Ayaansh_Joshi/Desktop/v-tracker-latest - Copy/v-track/{folder}")

    with open(folder, mode="r") as f:
        stuff = f.read()
    with open(f"v-track/{folder}/{folder}",mode="w") as f2:
        f2.write(stuff)

         

    
with open("v-track/tracker.txt", 'r') as f:     
        for line in f:
            files.append(line.strip())
import os, time
def start():
    last_mtime = {}
    for file in files:
        last_mtime[file] = os.path.getmtime(file)
    while True:
        for file in files:
            current = os.path.getmtime(file)
            if current != last_mtime[file]:
                print("did you know Minecraft was orginally called the cave game !")
                last_mtime[file] = current
                from random import randint
                try:
                    with open(file, mode='r') as f4:
                        stoof = f4.read()
                    with open(f"v-track/{file}/{file}{randint(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)}", mode="w") as f32:
                        f32.write(stoof)                
             #           time.sleep(5)
                 #   last_mtime[file] = current
                except PermissionError as e:
                    print(f" permission denied most likley that one of the tracked files is being used howerver other things can happen error {e}")
                    time.sleep(5)
      #      time.sleep(5)           



        

          #  time.sleep(1)            




         
def run(name):
    if name == "init":
        import subprocess
     #   import os
        subprocess.run(['mkdir', 'v-track'],shell=True)
        subprocess.run(['cd', 'v-track'],shell=True)
        file = input("file: ") 
      #  print("addding", file, "to tracker.txt")
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
        #    print("addding", file, "to tracker.txt")
            with open("v-track/tracker.txt", mode="a+") as f:
      #      stoof = f.read()
       #     print(stoof)
        #    if file in stoof:
         #       print("sorry duplicates will crash the thing")
          #      exit(0)
                f.write(f"{file2}\n")
            #    f.write("\n")
                folder(file2)
    elif name == "help":
         print("help:\n")
         print("commands: read write init add help")
         print("read: get list of files being tracked")
         print("add: adds a file to be tracked")
         print("init: init a folder")
         print("help: prints this help text")
    elif name == "start":
        start()
    else:
         print("sorry unkown command")

arg = argparse.ArgumentParser(description="git like program")
arg.add_argument("action", help="do something")
args = arg.parse_args()
run(args.action)
