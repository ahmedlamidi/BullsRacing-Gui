import tkinter as tk 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from Models import Channel

Total_channels = {"none": 0}
unique = 0

class MainPage(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.geometry("700x600")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, AddChannel, BasicAnalyis, PlotChannel):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
      
class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        def refresh_channel():
            channels_var.set("\n".join([str(channel) for channel in Total_channels if str(channel) != 'none']))

        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Elementary Data analysis")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Add Channel",
                            command=lambda: controller.show_frame(AddChannel))
        button.pack()

        button2 = tk.Button(self, text="Calculations Page",
                            command=lambda: controller.show_frame(BasicAnalyis))
        button2.pack()

        button3 = tk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PlotChannel))
        button3.pack()


        available_channel_headers = tk.Label(self, text="These are the available channels: ")
        available_channel_headers.pack()

        channels_var = tk.StringVar()
        show_available_channel_label = tk.Label(self, textvariable=channels_var, width=100, height=20, anchor='n')
        show_available_channel_label.pack(side=tk.TOP)


        button4 = tk.Button(self, text="Refresh channels list",
                            command=refresh_channel)
        button4.pack()

        


class AddChannel(tk.Frame):

    def __init__(self, parent, controller):

        def add_channel_button():
            global unique
            if selected_data_type.get() and selected_location.get() and selected_name.get():
                new_channel = Channel.Channel(channel_name=selected_name.get(),
                        location = selected_location.get(), data_type=selected_data_type.get(),
                        hertz_rate = 1, data_points = [float(data_point) for data_point in data.get().split()],
                        time_points = [float(time_point) for time_point in time.get().split()], 
                        unique_id = unique)
                Total_channels[str(new_channel)] = new_channel
                unique += 1
                unique_channel_var.set(unique_channel_var.get() + 1)
            reset_drop_down()

        def reset_drop_down():
            selected_name.set("")
            selected_location.set("")
            selected_data_type.set("")
            data.set("")
            time.set("")

          
             
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add channels Below")
        label.pack(pady=10,padx=10)

        unique_id_channel_frame = tk.Frame(self)
        unique_id_channel_frame.pack()
        unique_id_channel_label = tk.Label(unique_id_channel_frame,text="Number of Channels inputted: ")
        unique_id_channel_label.pack(side=tk.LEFT)
        unique_channel_var = tk.IntVar()
        unique_channel_var_label = tk.Label(unique_id_channel_frame, textvariable=unique_channel_var)
        unique_channel_var_label.pack(side=tk.RIGHT)
        

        channel_name_frame = tk.Frame(self)
        channel_name_frame.pack()
        selected_name = tk.StringVar(value="")
        name_dropdown= tk.OptionMenu(channel_name_frame, selected_name, *["brake_temperature","brake_pressure"])
        name_dropdown.pack(side=tk.RIGHT)
        name_label = tk.Label(channel_name_frame,text="Select channel name: ")
        name_label.pack(side=tk.LEFT)

        channel_data_type_frame = tk.Frame(self)
        channel_data_type_frame.pack()
        selected_data_type = tk.StringVar(value="")
        data_type_dropdown= tk.OptionMenu(channel_data_type_frame, selected_data_type, *["pressure","temperature"])
        data_type_dropdown.pack(side=tk.RIGHT)
        data_type_label = tk.Label(channel_data_type_frame,text="Select a data type for the channel: ")
        data_type_label.pack(side=tk.LEFT)

        channel_location_frame = tk.Frame(self)
        channel_location_frame.pack()
        selected_location = tk.StringVar(value="")
        location_dropdown= tk.OptionMenu(channel_location_frame, selected_location, *["front","rear","front_left","front_right","rear_left", "rear_right"])
        location_dropdown.pack(side=tk.RIGHT)
        location_label = tk.Label(channel_location_frame,text="Select a location for the channel: ")
        location_label.pack(side=tk.LEFT)


        data_location_frame = tk.Frame(self)
        data_location_frame.pack()
        data = tk.StringVar(value="")
        data_entry = tk.Entry(data_location_frame,textvariable=data)
        data_entry.pack(side=tk.RIGHT)
        data_label = tk.Label(data_location_frame, text="Enter the data seperated by a space: ")
        data_label.pack(side=tk.LEFT)

        time_location_frame = tk.Frame(self)
        time_location_frame.pack()
        time = tk.StringVar(value="")
        time_entry = tk.Entry(time_location_frame,textvariable=time)
        time_entry.pack(side=tk.RIGHT)
        time_label = tk.Label(time_location_frame, text="Enter the time values seperated by a space: ")
        time_label.pack(side=tk.LEFT)


        button_add_channel = tk.Button(self, text="Add new channel",
                  command=add_channel_button)

        button_add_channel.pack()

        buttonhome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        buttonhome.pack(side=tk.BOTTOM)



class BasicAnalyis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select A basic calculation to perform")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PlotChannel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Plot a channel")
        label.pack(pady=10,padx=10)

        graph = Figure(figsize=(4, 4), dpi=100)
        canvas = FigureCanvasTkAgg(graph, self)
        mine = canvas.get_tk_widget()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        def plot():
            nonlocal mine, graph
            mine.delete()
            mine.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas_2 = graph.add_subplot(111)
            if (first_channel_select.get() != "none" and first_channel_select.get() != ""):
                canvas_2.plot(Total_channels[first_channel_select.get()].time_points,Total_channels[first_channel_select.get()].data_points)
            else:
                canvas_2.plot([0,0], [0,0])

            if (second_channel_select.get() != "none" and second_channel_select.get() != ""):
                canvas_2.plot(Total_channels[second_channel_select.get()].time_points,Total_channels[second_channel_select.get()].data_points)
            else:
                canvas_2.plot([0,0], [0,0])

            if (third_channel_select.get() != "none" and third_channel_select.get() != ""):
                canvas_2.plot(Total_channels[third_channel_select.get()].time_points,Total_channels[third_channel_select.get()].data_points)
            else:
                canvas_2.plot([0,0], [0,0])

            if (fourth_channel_select.get() != "none" and fourth_channel_select.get() != ""):
                canvas_2.plot(Total_channels[fourth_channel_select.get()].time_points,Total_channels[fourth_channel_select.get()].data_points)
            else:
                canvas_2.plot([0,0], [0,0])

            canvas.draw()

        def refresh():
            nonlocal first_channel, second_channel, third_channel, fourth_channel
            first_channel.destroy()
            second_channel.destroy()
            third_channel.destroy()
            fourth_channel.destroy()
            first_channel= tk.OptionMenu(first_pick_frame, first_channel_select, *Total_channels.keys())
            first_channel.pack(side=tk.LEFT)
            second_channel= tk.OptionMenu(second_pick_frame, second_channel_select, *Total_channels.keys())
            second_channel.pack(side=tk.LEFT)
            third_channel= tk.OptionMenu(third_pick_frame, third_channel_select, *Total_channels.keys())
            third_channel.pack(side=tk.LEFT)
            fourth_channel= tk.OptionMenu(fourth_pick_frame, fourth_channel_select, *Total_channels.keys())
            fourth_channel.pack(side=tk.LEFT)

        frame_select = tk.Frame(self)


        first_pick_frame = tk.Frame(frame_select)
        first_channel_label = tk.Label(first_pick_frame, text="Select 1st:", fg='#00f')
        first_channel_label.pack(side=tk.LEFT)
        first_channel_select = tk.StringVar(value="")
        first_channel= tk.OptionMenu(first_pick_frame, first_channel_select, *Total_channels.keys())
        first_channel.pack(side=tk.LEFT)
        first_pick_frame.pack(side=tk.LEFT)


        second_pick_frame = tk.Frame(frame_select)
        second_channel_label = tk.Label(frame_select, text="Select 2nd:", fg='orange')
        second_channel_label.pack(side=tk.LEFT)
        second_channel_select = tk.StringVar(value="")
        second_channel= tk.OptionMenu(second_pick_frame, second_channel_select, *Total_channels.keys())
        second_channel.pack(side=tk.LEFT)
        second_pick_frame.pack(side=tk.LEFT)

        third_pick_frame = tk.Frame(frame_select)
        third_channel_label = tk.Label(frame_select, text="Select 3rd:", fg='green')
        third_channel_label.pack(side=tk.LEFT)
        third_channel_select = tk.StringVar(value="")
        third_channel= tk.OptionMenu(third_pick_frame, third_channel_select, *Total_channels.keys())
        third_channel.pack(side=tk.LEFT)
        third_pick_frame.pack(side=tk.LEFT)

        fourth_pick_frame = tk.Frame(frame_select)
        fourth_channel_label = tk.Label(frame_select, text="Select 4th:", fg='red')
        fourth_channel_label.pack(side=tk.LEFT)
        fourth_channel_select = tk.StringVar(value="")
        fourth_channel= tk.OptionMenu(fourth_pick_frame, fourth_channel_select, *Total_channels.keys())
        fourth_channel.pack(side=tk.LEFT)
        fourth_pick_frame.pack(side=tk.LEFT)


        Plot_button = tk.Button(frame_select, text="Plot selcted Functions", command=plot)
        Plot_button.pack(side=tk.LEFT)

        frame_select.pack(side=tk.TOP)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))

        button4 = tk.Button(self, text="Refresh channels list",
                            command=refresh)

        button1.pack(side=tk.BOTTOM)
        button4.pack(side=tk.BOTTOM)



app = MainPage()
app.mainloop()