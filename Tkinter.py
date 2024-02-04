import tkinter as tk 
from Models import Channel

Total_channels = []
unique = 0

class MainPage(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.geometry("600x600")
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
            channels_var.set("\n".join([str(channel) for channel in Total_channels]))

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
                Total_channels.append(Channel.Channel(channel_name=selected_name.get(),
                        location = selected_location.get(), data_type=selected_data_type.get(),
                        hertz_rate = 1, data = [], time = [], unique_id = unique))
                unique += 1
                unique_channel_var.set(unique_channel_var.get() + 1)
            reset_drop_down()

        def reset_drop_down():
            selected_name.set("")
            selected_location.set("")
            selected_data_type.set("")

          
             
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

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



app = MainPage()
app.mainloop()