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

indent = 20
left_window = dpg.generate_uuid()

right_window = dpg.generate_uuid()
bottom_window = dpg.generate_uuid()
center_window = dpg.generate_uuid()
activities = dpg.generate_uuid()
student_list = dpg.generate_uuid()
file_director = dpg.generate_uuid()
error_list_window = dpg.generate_uuid()

gui.initiate_problem_list()

dpg.add_window(label="Opiskelijat", tag=left_window,
                menubar=False, no_close=True, horizontal_scrollbar=True)

dpg.add_window(label="Arviointitaulukko", tag=right_window,
                menubar=False, no_close=True, no_move=True)

dpg.add_window(label="Toiminnot", tag=bottom_window,
                menubar=False, no_close=True, no_move=True)
dpg.add_window(label="Virheet", tag=center_window,
                menubar=False, no_close=True, no_move=True, autosize=True)

dpg.add_group(tag=activities, horizontal=True,
                parent=bottom_window, track_offset=0.5)
dpg.add_spacer(width=2, parent=activities)
dpg.add_button(label="Kirjoita arvostellut tiedostoon",
                parent=activities)
dpg.add_spacer(width=2, parent=activities)
dpg.add_button(label="Kopioi palautekommentti leikepöydälle",
                parent=activities)
dpg.add_group(tag = student_list, parent=left_window, width=300)
studentList = []
# for i in range(25):
#     studentList.append(random.randint(0, 100))
dpg.add_listbox(items=[], parent=student_list, width=300, num_items=100, tag="Test")
dpg.add_file_dialog(label="Valitse kansio", directory_selector=True, show=True, tag=file_director, width=700, height=400, callback=gui.dir_callback_exam, user_data=studentList)

category_texts = [
                "toiminnallisuus tehtäväksiannon mukaan ja CodeGradesta läpi",
                "tiedostorakenne useita tiedostoja",
                "ohjeiden mukaiset alkukommentit",
                "ohjelmarakenne pääohjelma ja aliohjelmat",
                "perusoperaatiot tulostus, syöte, valintarakenne, toistorakenne",
                "tiedonvälitys parametrit ja paluuarvot, ei globaaleja muuttujia",
                "tiedostonkäsittely luku ja kirjoittaminen",
                "tietorakenteet lista, luokka ja olio",
                "poikkeustenkäsittely tiedostonkäsittelyssä",
                "analyysien toteutus",
                "toteutuksen selkeys, ymmärrettävä, ylläpidettävä ja laajennettava",
            ]
error_list = []

for i in range(0, 11):
    error_list.append("import ei ole päätasolla, vaan sisennettynä aliohjelman/luokan sisään.")
with dpg.group(tag=error_list_window, parent=center_window):
    i = 0    
    j= 0
    for category in category_texts:      
        dpg.add_collapsing_header(label=category, default_open=False, parent=error_list_window, tag="header_" + str(i))
            #with dpg.tree_node(label= "Tree node 1", default_open=True, tag = "Tree_Node"):
        
      
            
        with dpg.group(horizontal=True, parent="header_" + str(i)):
            dpg.add_text(default_value=error_list[i])
            dpg.add_spacer()
            dpg.add_button(label="+", callback=gui.add_value, tag="button" + str(i))
            dpg.add_spacer()
            dpg.add_text(default_value="0", tag="value"+str(i))
            dpg.add_spacer()
            dpg.add_button(label="-")
             
        i += 1
    # with dpg.table(header_row=True):
    #     dpg.add_table_column(label="Virheet")
    #     dpg.add_table_column(label="Määrä")
  

    #     for i in range(0,4):
    #         with dpg.table_row():
    #             for j in range(0, 2):
    #                 dpg.add_button(label="+")
    #                 dpg.add_spacer()
    #                 dpg.add_text(amount)
    #                 dpg.add_spacer()
    #                 dpg.add_button(label="-")
                    


    

# with dpg.font_registry():
#     with dpg.font("NotoSerif-Regular.ttf", 15) as font1:
#         dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
# dpg.bind(font)




dpg.show_viewport(maximized=True)

dpg.show_item_registry()
# dpg.show_item_debug(38)

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    if (studentList != []):
        dpg.configure_item("Test", items=studentList)

dpg.destroy_context()
