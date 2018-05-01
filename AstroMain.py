import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
import WebScrapeClearDarkSky as cds


def initialize_variables():
    global width, height
    width, height = 600, 700


class AstroMain(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=22, weight="bold", slant="italic")
        self.general_font = tkfont.Font(family='Helvetica', size=14, weight="bold", slant="italic")
        self.general_font_small = tkfont.Font(family='Helvetica', size=10, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (AstroMainView, ClearDarkSkyView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AstroMainView")

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
            for widget in frame.winfo_children():
                widget.destroy()

        if page_name == 'AstroMainView':
            self.frames[page_name].display_astromainview()
        elif page_name == 'ClearDarkSkyView':
            self.frames[page_name].display_cleardarkskyview()

        frame = self.frames[page_name]
        frame.grid()
        frame.winfo_toplevel().geometry("600x700+200+200")


class AstroMainView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def display_astromainview(self):
        label = tk.Label(self, text="Astrophotography Sidekick", font=self.controller.title_font)
        label.place(relx=.10, rely=.1, width=.8 * width)

        check_cleardarksky = tk.Button(self, text="Check ClearDarkSky", width=10, height=2, font=("Helvetica", 20),
                            command=lambda: [self.controller.show_frame("ClearDarkSkyView")], bg='skyblue1')

        check_cleardarksky.place(relx=.25, rely=.2, width=.5 * width)


class ClearDarkSkyView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def display_cleardarkskyview(self):
        title_label = tk.Label(self, text="ClearDarkSky Check", font=self.controller.title_font)
        title_label.place(relx=.10, rely=.1, width=.8 * width)

        start_time_label = tk.Label(self, text="Pick a start time: ", font=self.controller.general_font)
        start_time_label.place(relx=.10, rely=.3, width=.35 * width)

        OPTIONS = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        ]
        time_var_start = StringVar(self)
        time_var_end = StringVar(self)
        time_var_start.set(OPTIONS[0])
        time_var_end.set(OPTIONS[0])

        start_am = True
        end_am = True

        start_time_option = tk.OptionMenu(self, time_var_start, *OPTIONS)
        start_time_option.place(relx=.45, rely=.3, width=.35 * width)

        am_button = tk.Button(self, text="AM", width=2, height=1, font=self.controller.general_font_small,
                                command=lambda: am_pm_button(am_pm_button(1)))
        pm_button = tk.Button(self, text="PM", width=2, height=1, font=self.controller.general_font_small,
                              command=lambda: am_pm_button(am_pm_button(2)))
        am_button.place(relx=.81, rely=.3, width=.05 * width)
        pm_button.place(relx=.87, rely=.3, width=.05 * width)

        end_time_label = tk.Label(self, text="Pick a end time: ", font=self.controller.general_font)
        end_time_label.place(relx=.10, rely=.4, width=.35 * width)

        end_time_option = tk.OptionMenu(self, time_var_end, *OPTIONS)
        end_time_option.place(relx=.45, rely=.4, width=.35 * width)

        am_button2 = tk.Button(self, text="AM", width=2, height=1, font=self.controller.general_font_small,
                              command=lambda: am_pm_button(am_pm_button2(1)))
        pm_button2 = tk.Button(self, text="PM", width=2, height=1, font=self.controller.general_font_small,
                              command=lambda: am_pm_button(am_pm_button2(2)))
        am_button2.place(relx=.81, rely=.4, width=.05 * width)
        pm_button2.place(relx=.87, rely=.4, width=.05 * width)

        check_conditions_button = tk.Button(self, text="Check Conditions", width=2, height=1, font=self.controller.general_font_small,
                               command=lambda: check_conditions())
        check_conditions_button.place(relx=.2, rely=.5, width=.6 * width)

        def am_pm_button(x):
            if x == 1:
                am_button.config(bg='skyblue1')
                pm_button.config(bg='SystemButtonFace')
                start_am = True
            elif x == 2:
                am_button.config(bg='SystemButtonFace')
                pm_button.config(bg='skyblue1')
                start_am = False

        def am_pm_button2(x):
            if x == 1:
                am_button2.config(bg='skyblue1')
                pm_button2.config(bg='SystemButtonFace')
                end_am = True
            elif x == 2:
                am_button2.config(bg='SystemButtonFace')
                pm_button2.config(bg='skyblue1')
                end_am = False

        def check_conditions():
            print("Checking conditions")
            if start_am == True:
                start = int(time_var_start.get()) + 12
            elif start_am == False:
                start = int(time_var_start.get())

            if end_am == True:
                end = int(time_var_end.get())
            elif end_am == False:
                end = int(time_var_end.get()) + 12

            cds.getWeatherData2(start, end)


if __name__ == "__main__":
    initialize_variables()
    app = AstroMain()
    app.mainloop()