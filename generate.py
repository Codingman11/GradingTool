import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.configure_app(docking=True, docking_space=True,
                  init_file="custom_layout.ini") # must be called before create_viewport
dpg.create_viewport()
dpg.setup_dearpygui()

# generate IDs - the IDs are used by the init file, they must be the
#                same between sessions
left_window = dpg.generate_uuid()
right_window = dpg.generate_uuid()
bottom_window = dpg.generate_uuid()
center_window = dpg.generate_uuid()

dpg.add_window(label="Opiskelijat", tag=left_window,
               menubar=False, no_close=True, horizontal_scrollbar=True)

dpg.add_window(label="Arviointitaulukko", tag=right_window,
               menubar=False, no_close=True)
dpg.add_window(label="Toiminnot", tag=bottom_window,
               menubar=False, no_close=True)
dpg.add_window(label="Virheet", tag=center_window,
               menubar=False, no_close=True, horizontal_scrollbar=True)

with dpg.window(label="Temporary Window"):
    dpg.add_button(label="Save Ini File", callback=lambda: dpg.save_init_file("custom_layout.ini"))


# main loop
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()  

dpg.destroy_context()