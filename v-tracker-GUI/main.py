from v_tracker_gui import v_tracker_gui
import webbrowser
def Eventread(name):
    print(name)
def Eventaddd(name):
    print(name)
def Eventinit(name):
    print(name)
def Event1(name):
    print(name)
    if name == "info_button":
        webbrowser.open("https://github.com/superuser5698/v-tracker")
    elif name == "help_button":
        webbrowser.open("https://github.com/superuser5698/v-tracker/blob/main/manual.txt")
v_tracker_gui.run()
