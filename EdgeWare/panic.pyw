import os
import ctypes
import pathlib
import hashlib
import subprocess
import tkinter as tk
from tkinter.simpledialog import askstring

PATH = str(pathlib.Path(__file__).parent.absolute())

hash_file_path = os.path.join(PATH, 'pass.hash')
time_file_path = os.path.join(PATH, 'hid_time.dat')

HIDDEN_ATTR = 0x02
SHOWN_ATTR  = 0x08
#checking timer
try:
    ctypes.windll.kernel32.SetFileAttributesW(time_file_path, SHOWN_ATTR)
except:
    ''
if os.path.exists(time_file_path):
    with open(hash_file_path, 'r') as file:
        HASHED_PATH = file.readline()
    ctypes.windll.kernel32.SetFileAttributesW(time_file_path, HIDDEN_ATTR)
    try:
        # root = tk.Tk()
        pass_ = askstring('Panic', 'Enter Panic Password')
        t_hash = None if pass_ == None or pass_ == '' else hashlib.sha256(pass_.encode(encoding='ascii', errors='ignore')).hexdigest()
        if t_hash == HASHED_PATH:
            #revealing hidden files
            SHOWN_ATTR = 0x08
            ctypes.windll.kernel32.SetFileAttributesW(time_file_path, SHOWN_ATTR)
            os.remove(time_file_path)
            os.startfile('panic.bat')
        else:
            hashObjPath = os.path.join(PATH, 'pass.hash')
            timeObjPath = os.path.join(PATH, 'hid_time.dat')
            if os.path.exists(timeObjPath):
                subprocess.call('pythonw prompt.pyw timerEarly')
                # os.system(r'python prompt.pyw timerEarly')
            else:
                os.startfile('panic.pyw')
    except Exception as e:
        print(e)
        #if some issue occurs with the hash or time files just emergency panic
        os.startfile('panic.pyw')
else:
    #continue if no timer
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH + '\\default_assets\\default_win10.jpg', 0)
    os.startfile('panic.bat')