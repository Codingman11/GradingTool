import dearpygui.dearpygui as dpg
import os, json

class ErrorInfo:
    error = ("",)
    severity = 0
    amount = 0
    alternative = []
    exclude = []
    feedback = ""

class Category:
    category = ""
    category_sum = 0
    

#Calling if practical assignment
def dir_callback(sender, app_data, user_data):
    path = app_data["file_path_name"]
    files = os.listdir(path)
    for student_file in files:
        fullname = os.path.join(path, student_file).replace("\\", "/")
        if os.path.isdir(fullname):
            user_data.append(student_file)

    #print(f"Sender: {sender}, App Data: {app_data}, User data: {user_data}")
    return user_data

#calling if exam evaluating
def dir_callback_exam(sender, app_data, user_data):
    path = app_data["file_path_name"]
    files = os.listdir(path)
    for file in files:
        user_data.append(file)
    return user_data



def initiate_problem_list(sender, app_data, user_data):
    
    try:
        with open("Problem_list.json", "r", encoding="utf-8") as file:
            errorsList = json.load(file) #loads json file as dict
            file.close()
    except IOError as e:
        print("Error: ", e)

    
    categ = errorsList["violations"][0]["category"]
    
    
    
    for error in errorsList["violations"]:
        pass
