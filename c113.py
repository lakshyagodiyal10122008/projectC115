import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir="C:/Users/pc/Downloads"
to_dir="C:/Users/pc/Contacts/Desktop/CDE"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        name,extension=os.path.splittext(event.src_path)
        event.src_path
        for key,value in dir_tree.items():
            if extension in value:
                file_name=os.path.basename(event.source_path)
        path1 = to_dir + '/' + file_name
        path2 = from_dir + '/' + "Image_Files"
        path3 = from_dir + '/' + "Image_Files" + '/' + file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
            print ("moving")
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving")

                

        print(event)
        print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
while True:
    time.sleep(2)
    print("running...")