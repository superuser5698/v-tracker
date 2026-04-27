from v_tracker_gui import v_tracker_gui
def Event1(name):
    print(name)
    dropdown = v_tracker_gui.select_option_dropdown.get()
    if name == "run_option_button":
        v_tracker_gui.result_of_option.config(text = dropdown)
    if dropdown == "read":
        v_tracker_gui.result_of_option.config(text = "reading(reminder to add actual read function here)")
    if dropdown == "add":
        v_tracker_gui.result_of_option.config(text = "adding(reminder to add actual add function here)")

v_tracker_gui.run()