import dearpygui.dearpygui as dpg
import os
def dir_callback(sender, app_data):
    path = app_data["file_path_name"]
    students_folders = os.listdir(path)
    for student in students_folders:
        print(student)