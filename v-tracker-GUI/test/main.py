from v_tracker_gui import v_tracker_gui
import webbrowser
from tkinter import filedialog

def Eventdelete(name):
    print(name)
    v_tracker_gui.result_of_option.config(text = "deleting...")
def Eventread(name):
    print(name)
    v_tracker_gui.result_of_option.config(text = "reading...")
def Eventaddd(name):
    v_tracker_gui.result_of_option.config(text = "adding...")
    print(name)
    add_file = filedialog.askopenfilename(title="pick the file you want to add(to cancel close this window)")
    if not type(add_file) == "<type 'unicode>" or type(add_file) == "<type 'str>" or type(add_file) == "type 'tuple'>" or add_file == "" or add_file is None:
        print(add_file)
        v_tracker_gui.result_of_option.config(text = f"adding {add_file}")
  #  v_tracker_gui.result_of_option.config(text = "Canceled")
def Eventinit(name):
    print(name)
    v_tracker_gui.result_of_option.config(text = "initializing...")
    init_folder_file = filedialog.askdirectory(title="pick the folder you want to initialize(to cancel close this window)")
    if not type(init_folder_file) == "<type 'unicode>" or type(init_folder_file) == "<type 'str>" or type(init_folder_file) == "type 'tuple'>" or init_folder_file == "" or init_folder_file is None:
        print(init_folder_file)
        v_tracker_gui.result_of_option.config(text = f"initializing {init_folder_file}")
   # v_tracker_gui.result_of_option.config(text = "Canceled")
def Event1(name):
    print(name)
    if name == "info_button":
        webbrowser.open("https://github.com/superuser5698/v-tracker")
    elif name == "help_button":
        webbrowser.open("https://github.com/superuser5698/v-tracker/blob/main/manual.txt")
v_tracker_gui.run()
