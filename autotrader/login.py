import time
import pywinauto

def login(folder_path):

    try:
        pywinauto.Application().connect(path=folder_path + '\\xiadan.exe', timeout=1)
    except:
        pywinauto.Application(backend="uia").start(folder_path + '\\hexin.exe')

        time.sleep(2)
        while True:
            try:
                pywinauto.findwindows.find_window(class_name='#32770', found_index=1)
                break
            except:
                time.sleep(7)
        time.sleep(2)

        pywinauto.Application(backend="uia").start(folder_path + '\\xiadan.exe')



