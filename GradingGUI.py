import dearpygui.dearpygui as dpg
import pathlib
import os
import random
import GradingGUI_library as gui

dpg.create_context()

dpg.create_viewport(title="Testing", width=1200, height=600,
                    resizable=True, always_on_top=True)
dpg.configure_app(docking=True, docking_space=True,
                  load_init_file="custom_layout.ini")
dpg.setup_dearpygui()

left_window = dpg.generate_uuid()

right_window = dpg.generate_uuid()
bottom_window = dpg.generate_uuid()
center_window = dpg.generate_uuid()
activities = dpg.generate_uuid()
student_list = dpg.generate_uuid()
file_director = dpg.generate_uuid()



dpg.add_window(label="Opiskelijat", tag=left_window,
                menubar=False, no_close=True, horizontal_scrollbar=True)

dpg.add_window(label="Arviointitaulukko", tag=right_window,
                menubar=False, no_close=True, no_move=True)

dpg.add_window(label="Toiminnot", tag=bottom_window,
                menubar=False, no_close=True, no_move=True)
dpg.add_window(label="Virheet", tag=center_window,
                menubar=False, no_close=True, no_move=True)

dpg.add_group(tag=activities, horizontal=True,
                parent=bottom_window, track_offset=0.5)
dpg.add_spacing(width=2, parent=activities)
dpg.add_button(label="Kirjoita arvostellut tiedostoon",
                parent=activities)
dpg.add_spacing(width=2, parent=activities)
dpg.add_button(label="Kopioi palautekommentti leikepöydälle",
                parent=activities)
dpg.add_group(tag = student_list, parent=left_window, width=300)
studentList = []
for i in range(25):
    studentList.append(random.randint(0, 100))
dpg.add_listbox(studentList, parent=student_list, width=300, num_items=100)

# with dpg.group("ui", mousebutton=dpg.mvMouseButton_Left, modal=True, tag="popup_modal"):
#     dpg.add_file_dialog(label="Valitse kansio", directory_selector=True, show=True, tag=file_director, width=700, height=400)
# with dpg.font_registry():
#     with dpg.font("NotoSerif-Regular.ttf", 15) as font1:
#         dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)




dpg.show_viewport(maximized=True)


while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()
