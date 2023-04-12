from tkinter import *
from tkinter.ttk import *
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 1000
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex example")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ Global variables =============

        self.planes = ['cesna', 'samolot2', 'samolot3']
        self.plane_var = StringVar(self)
        self.cameras = ['cesna', 'samolot2', 'samolot3']
        self.camera_var = StringVar(self)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=300,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="title",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=280,
                                            placeholder_text="CTkEntry")
        self.entry.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="w")

        self.dx_entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="dx")
        self.dx_entry.grid(row=3, column=0, pady=10)

        self.dy_entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="dy")
        self.dy_entry.grid(row=3, column=1, pady=10, padx=20)

        self.p_entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="p")
        self.p_entry.grid(row=4, column=0, pady=10)

        self.q_entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="q")
        self.q_entry.grid(row=4, column=1, pady=10, padx=20)

        self.gsd_entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="gsd")
        self.gsd_entry.grid(row=5, column=0, pady=10, padx=20)

        self.hsr_entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="hsr")
        self.hsr_entry.grid(row=5, column=1, pady=10, padx=20)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Wybierz samolot:",
                                              text_font=("Roboto Medium", -13))  # font name and size in px
        self.label_2.grid(row=6, column=0, pady=10)

        self.plane_menu = OptionMenu(self.frame_left, self.plane_var, self.planes[0], *self.planes)
        self.plane_menu.grid(row=6, column=1, pady=10)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Wybierz kamerę:",
                                              text_font=("Roboto Medium", -13))  # font name and size in px
        self.label_3.grid(row=7, column=0, pady=10)

        self.camera_menu = OptionMenu(self.frame_left, self.camera_var, self.cameras[0], *self.cameras)
        self.camera_menu.grid(row=7, column=1, pady=10)

        self.draw_button = customtkinter.CTkButton(self.frame_left,
                                                text="Rysuj",
                                                command=self.draw)
        self.draw_button.grid(row=8, column=0, columnspan=2, pady=20)

        # ============ frame_right ============



        # ============ frame_right ============

    def draw(self):
        print('dupa')

    def selectPlane(self, *args):
        print(self.plane_var.get())

    def selectCamera(self, *args):
        print(self.camera_var.get())

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()
