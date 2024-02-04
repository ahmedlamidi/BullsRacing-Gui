class Channel:
    def __init__(self, channel_name, location, data_type, hertz_rate, data, time, unique_id):
        self.channel_name = channel_name
        self.location = location
        self.data_type = data_type
        self.hertz_rate = hertz_rate
        self.data = data
        self.time = time
        self.unique_id = unique_id
    
    def add_constant(self, constant):
        self.data = [value + constant for value in self.data]

    def __str__(self):
        return f"A channel in {self.location} for {self.channel_name}"
