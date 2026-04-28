from v_tracker_gui import v_tracker_gui
def Event2(name):
    if v_tracker_gui.select_option_dropdown.get() == "add - add a tracked file":
        print(name)
        print("a")
        print(v_tracker_gui.insert_text.get())
        v_tracker_gui.result_of_option.config(text = f"File name entered. File name is: {v_tracker_gui.insert_text.get()}")
        print(f"File name entered. File name is: {v_tracker_gui.insert_text.get()}")
def Event1(name):
    print(name)
    dropdown = v_tracker_gui.select_option_dropdown.get()
    if name == "run_option_button":
        if dropdown == "read - check tracked files":
            v_tracker_gui.result_of_option.config(text = "reading(reminder to add actual read function here)")
        elif dropdown == "add - add a tracked file":
            v_tracker_gui.result_of_option.config(text = " type the name of the file you would like to be tracked to add it presss the ok button")
        elif dropdown == "init - init the  working folder":
            v_tracker_gui.result_of_option.config(text = "initializing(reminder to add actual init function here)")

v_tracker_gui.run()