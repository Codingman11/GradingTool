import dearpygui.dearpygui as dpg
import pathlib
import os


dpg.create_context()
dpg.configure_app(docking=True, docking_space=True, load_init_file="custom_layout.ini")
dpg.create_viewport(title="Testing", width=1200, height=600, resizable=True)
dpg.setup_dearpygui()


left_window = dpg.generate_uuid()
right_window = dpg.generate_uuid()
top_window = dpg.generate_uuid()
bottom_window = dpg.generate_uuid()
center_window = dpg.generate_uuid()
activities = dpg.generate_uuid()
student_list = dpg.generate_uuid()


    


with dpg.font_registry():
    with dpg.font("NotoSerif-Regular.ttf", 15) as font1:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        
       

# dpg.add_file_dialog(directory_selector=True, show=False, callback=callback, tag="file_dialog_id", cancel_callback=cancel_callback, width=600, height=300)
# with dpg.window(label="Testi", tag = "main"):
#     with dpg.child_window(height=40, autosize_x=True):
#         with dpg.group(tag="students", horizontal=False):
#             with dpg.tree_node(label="Students", tag="treedata", pos=(0,0)):
#                 dpg.add_listbox(tag="student_list",)
#         with dpg.group(horizontal=True):
#             dpg.add_text("Valitse Kansio")
#             dpg.add_button(label="Directory Selector", tag="dir_selected", callback=lambda: dpg.show_item("file_dialog_id"))
#             dpg.bind_item_handler_registry("dir_selected", "directory handler")

#     with dpg.child_window(height=300, label="Button"):
#         dpg.add_button(label="Tallenna", tag="save")

dpg.add_window(label="Opiskelijat", tag=left_window, menubar=False, no_close=True, horizontal_scrollbar=True )
    
dpg.add_window(label="Arviointitaulukko", tag=right_window, menubar=False, no_close=True)
dpg.add_window(label="Kommenttikenttä", tag=top_window, menubar=False, no_close=True)
dpg.add_window(label="Toiminnot", tag=bottom_window, menubar=False, no_close=True)
dpg.add_window(label="Virheet", tag=center_window, menubar=False, no_close=True)

dpg.add_group(tag=activities, horizontal=True, parent=bottom_window)
dpg.add_button(label="Tallenna", parent=activities)
dpg.add_button(label="Kirjoita arvostellut tiedostoon", parent=activities)
dpg.add_button(label="Kirjoita", parent=activities)

        
dpg.bind_font(font1)

dpg.show_viewport()


while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()