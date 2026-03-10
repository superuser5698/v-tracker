import os, time; file_path = '.'; last_mtime = os.path.getmtime(file_path)
while True:
    if os.path.getmtime(file_path) != last_mtime:
        print("File changed! Running code..."); last_mtime = os.path.getmtime(file_path)
        # YOUR CODE HERE
    time.sleep(1)
