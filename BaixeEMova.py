import sys
import time
import ramdom
import os
import shutil
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

from_dir ="C:/Users/vitorcodes2/Dowloads"
to_dir = "C:/Users/vitorcodes2/Desktop/dowmload_files"

dir_tree = {
  "Image_Files": ['.jpg', '.jpeg', '.png,' '.gif,' '.jfif'],
  "Video_Files": ['.mpg', '.mp2', '.mpeg,' '.mpe,' '.mpv' '.mp4,''.m4p,''.m4v,''.avi,''.mov'],
  "Document_Files":['.ppt', '.xls', '.xlsx,' '.csv,' '.pdf,''.txt'],
  "Setup_Files":['.exe', '.bin', '.cmd,' '.msi,''.dmg'],
