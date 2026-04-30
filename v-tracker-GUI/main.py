import os, time, argparse, time
global start, run, folder
files = []

def folder(folder):
    os.makedirs(f"{os.getcwd()}/v-track/{folder}")

    with open(folder, mode="r") as f:
        stuff = f.read()
    with open(f"v-track/{folder}/{folder}",mode="w") as f2:
        f2.write(stuff)

            

def start():   
    with open("v-track/tracker.txt", 'r') as f:     
            for line in f:
                files.append(line.strip())


    last_mtime = {}
    for file in files:
        last_mtime[file] = os.path.getmtime(file)
    while True:
        for file in files:
            current = os.path.getmtime(file)
            if current != last_mtime[file]:
                root, extension = os.path.splitext(file)
                print("did you know Minecraft was orginally called the cave game !")
                last_mtime[file] = current
                from random import randint
                try:
                    with open(file, mode='r') as f4:
                        stoof = f4.read()
                    with open(f"v-track/{file}/{file}{randint(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)}{extension}", mode="w") as f32:
                        f32.write(stoof)                
                #           time.sleep(5)
                    #   last_mtime[file] = current
                except PermissionError as e:
                    print(f" permission denied most likley that one of the tracked files is being used howerver other things can happen error {e}")
                    time.sleep(5)
        



            

            #  time.sleep(1)            




            
def run(name, file=None):
    if name == "init":
        import subprocess
        #   import os
        subprocess.run(['mkdir', 'v-track'])
        subprocess.run(['cd', 'v-track'],shell=True)
        with open("v-track/tracker.txt", mode="a+") as f:
            pass
       # file = input("file: ") 
    #  print("addding", file, "to tracker.txt")
     #   with open("v-track/tracker.txt", mode="a+") as f:
    #      stoof = f.read()
        #     print(stoof)
            #    if file in stoof:
            #       print("sorry duplicates will crash the thing")
            #      exit(0)
           # f.write(file)
            #f.write("\n")
        #folder(file)
    elif name == "read":
        with open("v-track/tracker.txt", mode="r") as f:
            v_tracker_gui.result_of_option.config(text = f"files that are being tracked:\n{f.read()}")
    elif name == "add":
           # file = input("file: ") 
            #    print("addding", file, "to tracker.txt")
            with open("v-track/tracker.txt", mode="a+") as f:
        #      stoof = f.read()
        #     print(stoof)
            #    if file in stoof:
            #       print("sorry duplicates will crash the thing")
            #      exit(0)
                f.write(f"{file}\n")
                #    f.write("\n")
                folder(file)
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



















from v_tracker_gui import v_tracker_gui
import webbrowser
def Event2(name):
    if v_tracker_gui.select_option_dropdown.get() == "add - add a tracked file":
      #  print(name)
        print("a")
        print(v_tracker_gui.insert_text.get())
        v_tracker_gui.result_of_option.config(text = f"File name entered. File name is: {v_tracker_gui.insert_text.get()}")
        print(f"File name entered. File name is: {v_tracker_gui.insert_text.get()}")
        try:
            run("add", v_tracker_gui.insert_text.get())
        except Exception as e:
            v_tracker_gui.result_of_option.config(text = f"Error occurred: {e}")
def Event1(name):
    print(name)
    dropdown = v_tracker_gui.select_option_dropdown.get()
    if name == "run_option_button":
        if dropdown == "read - check tracked files":
            v_tracker_gui.result_of_option.config(text = "reading...")
            run("read")
        elif dropdown == "add - add a tracked file":
            v_tracker_gui.result_of_option.config(text = " type the name of the file you would like to be tracked to add it presss the ok button")
        elif dropdown == "init - initialize a chosen folder":
            v_tracker_gui.result_of_option.config(text = "initializing")
            try:
                run("init")
            except Exception as e:
                v_tracker_gui.result_of_option.config(text = f"Error occurred: {e}")
            print("Initialization complete.")
        elif dropdown == "start - starts the file checking":
            try:
                start()
            except Exception as e:
                v_tracker_gui.result_of_option.config(text = f"Error occurred: {e}")
            print("File checking started.")
    elif name == "info_button":
        webbrowser.open("https://github.com/superuser5698/v-tracker")
v_tracker_gui.run()