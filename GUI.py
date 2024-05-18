import os
import tkinter
import customtkinter
from NFA import NFA
from PIL import Image

width = 950
height = 500

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("NFA Simulator")
        self.geometry(f"{width}x{height}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "nfa_simulator.png")), size=(750, 188))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(30, 30))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(30, 30))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(30, 30))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  NFA Simulator", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Generic NFA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="NFA Examples",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Generic NFA", command=self.frame_2_button_event, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="NFA Examples", command=self.frame_3_button_event, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)


        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # configure grid layout (4x4)
        self.second_frame.grid_columnconfigure(1, weight=1)
        self.second_frame.grid_columnconfigure((2, 3), weight=0)
        self.second_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # self.second_main_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=0, fg_color="transparent")
        # self.second_main_frame.pack()

        # self.second_output_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=0, fg_color="transparent")
        # self.second_output_frame.pack()

        self.regex_entry = customtkinter.CTkEntry(self.second_frame, placeholder_text="Enter the regular expression here...", width=150)
        self.regex_entry.grid(row=0, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.input_string_entry = customtkinter.CTkEntry(self.second_frame, placeholder_text="Enter the input string here...", width=150)
        self.input_string_entry.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.check_button = customtkinter.CTkButton(self.second_frame, text="Check", command=self.check_event)
        self.check_button.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # output frame
        self.true_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=20)
        self.true_frame.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.true_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "true.png")), size=(50, 50))
        self.true_image_label = customtkinter.CTkLabel(self.true_frame, text="", image=self.true_image)
        self.true_image_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.true_label = customtkinter.CTkLabel(self.true_frame, text="The NFA accepts the input string.", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.true_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.false_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=20)
        self.false_frame.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.false_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "false.png")), size=(50, 50))
        self.false_image_label = customtkinter.CTkLabel(self.false_frame, text="", image=self.false_image)
        self.false_image_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.false_label = customtkinter.CTkLabel(self.false_frame, text="The NFA does not accept the input string.", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.false_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.invalid_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=20)
        self.invalid_frame.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.invalid_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "false.png")), size=(50, 50))
        self.invalid_image_label = customtkinter.CTkLabel(self.invalid_frame, text="", image=self.invalid_image)
        self.invalid_image_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.invalid_label = customtkinter.CTkLabel(self.invalid_frame, text="Invalid regular expression.", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.invalid_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # configure grid layout (4x4)
        self.third_frame.grid_columnconfigure(1, weight=1)
        self.third_frame.grid_columnconfigure((2, 3), weight=0)
        self.third_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        
        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkScrollableFrame(self.third_frame, label_text="Expressions", label_font=customtkinter.CTkFont(size=20, weight="bold"))
        self.radiobutton_frame.grid(row=0, column=0, rowspan=2, columnspan=2 ,padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0, text="x(x|y)*|z", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text="(a|b)*abb", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2, text="XY|Z*", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # output frame
        self.examples_true_frame = customtkinter.CTkFrame(self.third_frame, corner_radius=20)
        self.examples_true_frame.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.true_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "true.png")), size=(50, 50))
        self.true_image_label = customtkinter.CTkLabel(self.examples_true_frame, text="", image=self.true_image)
        self.true_image_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.true_label = customtkinter.CTkLabel(self.examples_true_frame, text="The NFA accepts the input string.", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.true_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.examples_false_frame = customtkinter.CTkFrame(self.third_frame, corner_radius=20)
        self.examples_false_frame.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.false_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "false.png")), size=(50, 50))
        self.false_image_label = customtkinter.CTkLabel(self.examples_false_frame, text="", image=self.false_image)
        self.false_image_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.false_label = customtkinter.CTkLabel(self.examples_false_frame, text="The NFA does not accept the input string.", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.false_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.examples_invalid_frame = customtkinter.CTkFrame(self.third_frame, corner_radius=20)
        self.examples_invalid_frame.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.invalid_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "false.png")), size=(50, 50))
        self.invalid_image_label = customtkinter.CTkLabel(self.examples_invalid_frame, text="", image=self.invalid_image)
        self.invalid_image_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.invalid_label = customtkinter.CTkLabel(self.examples_invalid_frame, text="Invalid regular expression.", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.invalid_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        # create main entry and button
        self.examples_string = customtkinter.CTkEntry(self.third_frame, placeholder_text="Enter the input string here...")
        self.examples_string.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(self.third_frame, text="Check",command=self.examples_check_event)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        # set default values
        self.true_frame.grid_remove()
        self.false_frame.grid_remove()
        self.invalid_frame.grid_remove()
        self.examples_false_frame.grid_remove()
        self.examples_true_frame.grid_remove()
        self.examples_invalid_frame.grid_remove()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        self.geometry(f"{int(1100 * new_scaling_float)}x{int(580 * new_scaling_float)}")
        customtkinter.set_widget_scaling(new_scaling_float)

    def examples_check_event(self):
        regex = self.radio_button_1.cget("text") if self.radio_var.get() == 0 else \
                self.radio_button_2.cget("text") if self.radio_var.get() == 1 else \
                self.radio_button_3.cget("text") 
        
        input_string = self.examples_string.get()

        nfa = NFA(regex, input_string)

        valide = nfa.validate()
        is_match = nfa.check()

        # show the appropriate frame
        if valide:
            if is_match:
                self.examples_true_frame.grid()
                self.examples_false_frame.grid_remove()
                self.examples_invalid_frame.grid_remove()
            else:
                self.examples_true_frame.grid_remove()
                self.examples_invalid_frame.grid_remove()
                self.examples_false_frame.grid()
        else:
            self.examples_true_frame.grid_remove()
            self.examples_false_frame.grid_remove()
            self.examples_invalid_frame.grid()

    def check_event(self):
        regex = self.regex_entry.get()
        input_string = self.input_string_entry.get()

        nfa = NFA(regex, input_string)
        
        valide = nfa.validate()
        is_match = nfa.check()

        # show the appropriate frame
        if valide:
            if is_match:
                self.true_frame.grid()
                self.invalid_frame.grid_remove()
                self.false_frame.grid_remove()
            else:
                self.true_frame.grid_remove()
                self.invalid_frame.grid_remove()
                self.false_frame.grid()
            
        else:
            self.true_frame.grid_remove()
            self.false_frame.grid_remove()
            self.invalid_frame.grid()

if __name__ == "__main__":
    app = App()
    app.mainloop()