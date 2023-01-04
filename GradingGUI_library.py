import dearpygui.dearpygui as dpg
import os, json

class ERRORINFO:
    error = ("",)
    text = ""
    severity = 0
    amount = 0
    alternative = []
    exclude = []
    feedback = ""
    category = ""

class CATEGORY:
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

def add_value(sender, app_data, user_data):
    print(f"Sender: {sender} app_data: {app_data} user data: {user_data}")
    

def initiate_problem_list():
    try:
        with open("Problem_list.json", "r", encoding="utf-8") as file:
            ProblemList = json.load(file) #loads json file as dict
            file.close()
    except IOError as e:
        print("Error: ", e)

    
    categ = ProblemList["violations"][0]["category"]
    categoryList = []
    category_list = []

    for i in ProblemList["violations"]:
        if (i["category"] not in category_list):
            category_list.append(i["category"])
            c = CATEGORY()
            c.category = i["category"]
            c.category_sum = 0
            categoryList.append(c)
    ErrorList = []
    
           
            
        

    id = 0
    errorID = 0
    for section in ProblemList["violations"]:
        if (categ != section["category"]):
            errorID += 1
            ErrorInfo = ERRORINFO()
            ErrorInfo.error = section["ID"]
            ErrorInfo.text = section["text"]
            ErrorInfo.severity = section["error_values"] 
            ErrorInfo.amount = section["error_values"].keys()
            ErrorInfo.feedback = section["feedback"]
            ErrorInfo.category = section["category"]
            ErrorList.append(ErrorInfo)

            
        else:
            ErrorInfo = ERRORINFO()
            ErrorInfo.error = section["ID"]
            ErrorInfo.severity = section["error_values"] 
            ErrorInfo.amount = section["error_values"].keys()
            ErrorInfo.feedback = section["feedback"]
            ErrorList.append(ErrorInfo)

    return ErrorList, categoryList

# def add_error_to_group(id, text, id_number):
#     print(id)
#     with dpg.add_group(parent=id, horizontal=True, tag="group_" + str(id_number)):
#         dpg.add_text(default_value=text)
#         dpg.add_spacer()
#         dpg.add_button(label="+")
#         dpg.add_spacer()
#         dpg.add_button(label="-")


#     return 