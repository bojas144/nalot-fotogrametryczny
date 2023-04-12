import math as m
from tkinter import *
from tkinter.ttk import *
import customtkinter
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Arc
from classes import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    WIDTH = 1000
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Symulacja nalotu fotogrametrycznego")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(False, False)

        # ============ Global variables =============

        self.planes_input = ['Cessna 402', 'Cessna T206H NAV III',
                             'Vulcan Air P86 \n Observer 2', 'Tencam MMA']
        self.planes_obj = [Plane(132, 428, 8200, 5),
                           Plane(100, 280, 4785, 5),
                           Plane(135, 275, 6100, 6),
                           Plane(120, 267, 4572, 6)]
        self.plane_var = StringVar(self)
        self.cameras_input = ['Z/I DMC II 250', 'Leica DMC III',
                              'UltraCam Falcon M2 70', 'Z/I DMC II 230', 'UltraCam Eagle M3']
        self.cameras_obj = [Camera([16768, 14016], 5.6, ['R', 'G', 'B', 'NIR'], 112, 2.3, 66),
                            Camera([25728, 14592], 3.9, [
                                   'R', 'G', 'B', 'NIR'], 92, 1.9, 63),
                            Camera([17310, 11310], 6.0, [
                                   'R', 'G', 'B', 'NIR'], 70, 1.35, 61),
                            Camera([15552, 14144], 5.6, [
                                   'R', 'G', 'B', 'NIR'], 92, 2.3, 66),
                            Camera([26460, 17004], 4.0, ['R', 'G', 'B', 'NIR'], 80, 1.5, 61)]
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
                                              text="Nalot fotogrametryczny",
                                              text_font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.dx_entry = customtkinter.CTkEntry(master=self.frame_left,
                                               width=145,
                                               placeholder_text="dx terenu [m]")
        self.dx_entry.grid(row=3, column=0, pady=10)

        self.dy_entry = customtkinter.CTkEntry(master=self.frame_left,
                                               width=145,
                                               placeholder_text="dy terenu [m]")
        self.dy_entry.grid(row=3, column=1, pady=10, padx=20)

        self.p_entry = customtkinter.CTkEntry(master=self.frame_left,
                                              width=145,
                                              placeholder_text="p [%]")
        self.p_entry.grid(row=4, column=0, pady=10)

        self.q_entry = customtkinter.CTkEntry(master=self.frame_left,
                                              width=145,
                                              placeholder_text="q [%]")
        self.q_entry.grid(row=4, column=1, pady=10, padx=20)

        self.gsd_entry = customtkinter.CTkEntry(master=self.frame_left,
                                                width=145,
                                                placeholder_text="GSD [cm]")
        self.gsd_entry.grid(row=5, column=0, pady=10, padx=20)

        self.hsr_entry = customtkinter.CTkEntry(master=self.frame_left,
                                                width=145,
                                                placeholder_text="Śr. wysokość terenu [m]",
                                                text_font=("Roboto Medium", -11))
        self.hsr_entry.grid(row=5, column=1, pady=10, padx=20)

        self.w_entry = customtkinter.CTkEntry(master=self.frame_left,
                                              width=145,
                                              placeholder_text="Wysokość lotu [m]")
        self.w_entry.grid(row=6, column=0, pady=10, padx=20)

        self.airport_entry = customtkinter.CTkEntry(master=self.frame_left,
                                                    width=145,
                                                    placeholder_text="Odl. do lotniska [km]",
                                                    text_font=("Roboto Medium", -11))
        self.airport_entry.grid(row=6, column=1, pady=10, padx=20)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Wybierz samolot:",
                                              text_font=("Roboto Medium", -13))
        self.label_2.grid(row=7, column=0, pady=10)

        self.plane_menu = OptionMenu(
            self.frame_left, self.plane_var, self.planes_input[0], *self.planes_input)
        self.plane_menu.grid(row=7, column=1, pady=10)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Wybierz kamerę:",
                                              text_font=("Roboto Medium", -13))
        self.label_3.grid(row=8, column=0, pady=10)

        self.camera_menu = OptionMenu(
            self.frame_left, self.camera_var, self.cameras_input[0], *self.cameras_input)
        self.camera_menu.grid(row=8, column=1, pady=10)

        self.draw_button = customtkinter.CTkButton(self.frame_left,
                                                   text="Rysuj",
                                                   command=self.draw)
        self.draw_button.grid(row=9, column=0, columnspan=2, pady=20)

        # ============ frame_right ============

        # ============ frame_right ============

    def draw(self):
        plane = self.selectPlane()
        camera = self.selectCamera()
        p = float(self.p_entry.get())
        q = float(self.q_entry.get())
        gsd = float(self.gsd_entry.get())
        hsr = float(self.hsr_entry.get())
        dx = float(self.dx_entry.get())
        dy = float(self.dy_entry.get())
        w = float(self.w_entry.get())
        airport_dis = float(self.airport_entry.get())
        if w > plane.height:
            self.error = customtkinter.CTkLabel(master=self.frame_left,
                                                text="Wysokość lotu jest zbyt wysoka!",
                                                text_font=(
                                                    "Roboto Medium", -13),
                                                text_color='white',
                                                fg_color='red')
            self.error.grid(row=10, column=0, columnspan=2, pady=10)
            return -1
        lx, ly, bx, nx, by, ny = self.calculations(
            plane, camera, p, q, gsd, dx, dy, hsr, airport_dis)
        for widget in self.frame_right.winfo_children():
            widget.destroy()
        self.plotPlane(dx, dy, lx, ly, bx, nx, by, ny)

    def selectPlane(self, *args):
        plane = str(self.plane_var.get())
        for x in self.planes_input:
            if x == plane:
                id = self.planes_input.index(x)
                break
        return self.planes_obj[id]

    def selectCamera(self, *args):
        camera = str(self.camera_var.get())
        for x in self.cameras_input:
            if x == camera:
                id = self.cameras_input.index(x)
                break
        return self.cameras_obj[id]

    # percent, percent, cm, m, m, m, km
    def calculations(self, plane, camera, p, q, gsd, dx, dy, hsr, airport_dis):
        w = gsd/100 * (camera.focalLength/1000) / \
            (camera.sizeOfPixel/1000000)  # meter
        airport_dis = airport_dis * 1000
        habs = w + hsr  # meter
        lx = camera.sizeOfMatrix[1] * gsd/100  # meter
        ly = camera.sizeOfMatrix[0] * gsd/100  # meter
        bx = lx * (100 - p) / 100
        by = ly * (100 - q) / 100
        ny = m.ceil(dy / by)
        nx = m.ceil(dx / bx + 4)
        n = nx * ny
        k = n * ((bx * by) / (dx * dy))

        line_dis = (n - 1) * bx * ny
        back_dis = m.sqrt((airport_dis + (n - 1) * bx)**2 + (by * (ny-1))**2)
        sum_dis = airport_dis + line_dis + back_dis
        time = ((ny-1) * 140 + sum_dis / plane.velocityMax) / 60  # minutes
        print("Czas lotu: ", time, " minut")

        return lx, ly, bx, nx, by, ny

    def plotPlane(self, dx, dy, lx, ly, bx, nx, by, ny):
        figure_width = self.frame_right.winfo_width()/100
        figure_height = self.frame_right.winfo_height()/100
        fig = plt.figure(figsize=(figure_width, figure_height),
                         dpi=100)
        axes = fig.add_subplot(111)

        def plot_line(beginLine, endLine):
            x_values = [beginLine[0], endLine[0]]
            y_values = [beginLine[1], endLine[1]]
            axes.plot(x_values, y_values, color='blue', linestyle='dashed')

        axes.add_patch(Rectangle((3*bx, by/2), dx, dy,
                       edgecolor='black', facecolor='none', linewidth=2))

        for i in range(0, nx):
            for j in range(0, ny):
                axes.add_patch(Rectangle(
                    (i*bx, j*by), lx, ly, edgecolor="grey", facecolor="none", linewidth=0.5))

        xy = []

        for i in range(0, ny):
            for j in range(0, nx):
                photoXY = (0.5*lx+j*bx, 0.5*ly+i*by)
                axes.add_artist(plt.Circle(photoXY, 150, color='blue'))
                if xy:
                    plot_line(xy.pop(), photoXY)
                xy.append(photoXY)
            if i != ny-1:
                xy.clear()

        for i in range(1, ny):
            if i % 2 != 0:
                am1 = Arc((0.5*lx+(nx-1)*bx, (0.5*ly+(i-0.5)*by)), by,
                          by, 0, 270, 90, color='blue', linestyle='--')
                axes.add_patch(am1)
                plt.arrow(0.5*lx+(nx-1)*bx+by/2, (0.5*ly+(i-0.5)*by), 0, -1, width=0,
                          head_width=700, head_length=1000, ec='blue', color='blue')
            else:
                am1 = Arc((0.5*lx, (0.5*ly+(i-0.5)*by)), by, by,
                          0, 90, 270, color='blue', linestyle='--')
                axes.add_patch(am1)
                plt.arrow(0.5*lx-by/2, (0.5*ly+(i-0.5)*by), 0, -1, width=0,
                          head_width=700, head_length=1000, ec='blue', color='blue')

        plt.arrow(-5000, 10000, 0, 1, width=0, head_width=2500,
                  head_length=1500, ec='black', color='black')
        axes.annotate("N", (-5000, 10000), (-5500, 9000))

        canvas = FigureCanvasTkAgg(fig,
                                   master=self.frame_right)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0)

        plt.autoscale()

    def on_closing(self, event=0):
        self.quit()

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = App()
    app.start()
