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
    
def derivative(input_channel, return_channel, n_samples):
    return_channel.data.clear()
    return_channel.time.clear()

    for right_index in range(1, len(input_channel.data)):
        left_index = max(0, right_index - n_samples)

        time_delta = input_channel.time[right_index] - input_channel.time[left_index]
        data_delta = input_channel.time[right_index] - input_channel.data[left_index]

        if time_delta != 0:
            return_channel.data.append(data_delta / time_delta)
        else:
            return_channel.data.append(0)

        return_channel.time.append(input_channel.time[right_index])

def derivative(input_channel, return_channel, time_delta):
    return_channel.data.clear()
    return_channel.time.clear()

    start_time = input_channel.time[0]
    start_data = input_channel.data[0]
    current_end_time = start_time + time_delta
    index_input = 1

    while index_input < len(input_channel.data):
        if input_channel.time[index_input] < current_end_time:
            print(current_end_time, " ", input_channel.time[index_input], " ")
            index_input += 1
        elif input_channel.time[index_input] == current_end_time:
            return_channel.time.append(current_end_time)
            return_channel.data.append((input_channel.data[index_input] - start_data) / time_delta)
            start_data = input_channel.data[index_input]
            start_time = input_channel.time[index_input]
            current_end_time = start_time + time_delta
            index_input += 1
        else:
            approximate_data = linear_approximation(input_channel.time[index_input - 1],
                                                    input_channel.data[index_input - 1],
                                                    input_channel.time[index_input],
                                                    input_channel.data[index_input],
                                                    current_end_time)
            return_channel.time.append(current_end_time)
            return_channel.data.append((approximate_data - start_data) / time_delta)
            start_data = approximate_data
            start_time = current_end_time
            current_end_time = start_time + time_delta

def linear_approximation(time1, data1, time2, data2, expected_time):
    slope = (data2 - data1) / (time2 - time1)
    return ((expected_time - time1) * slope) + data1

def derivative(input_channel, return_channel, n_samples, start_sample, end_sample):
    return_channel.data.clear()
    return_channel.time.clear()

    for right_index in range(max(1, start_sample), min(input_channel.data.size(), end_sample)):
        left_index = max(0, right_index - n_samples)

        time_delta = input_channel.time[right_index] - input_channel.time[left_index]
        data_delta = input_channel.data[right_index] - input_channel.data[left_index]

        if time_delta != 0:
            return_channel.data.append(data_delta / time_delta)
        else:
            return_channel.data.append(0)

        return_channel.time.append(input_channel.time[right_index])

def derivative(input_channel, return_channel, time_delta, start_interval, end_interval):
    return_channel.data.clear()
    return_channel.time.clear()

    start_time = max(input_channel.time[0], start_interval)
    index_input = 0
    while start_time > input_channel.time[index_input]:
        index_input += 1
    
    if start_time == input_channel.time[index_input]:
        start_data = input_channel.data[index_input]
    else:
        start_data = linear_approximation(
            input_channel.time[index_input - 1],
            input_channel.data[index_input - 1],
            input_channel.time[index_input],
            input_channel.data[index_input],
            start_time
        )

    current_end_time = start_time + time_delta
    while index_input < input_channel.data.size() and current_end_time < end_interval:
        if input_channel.time[index_input] < current_end_time:
            index_input += 1
        elif input_channel.time[index_input] == current_end_time:
            return_channel.time.append(current_end_time)
            return_channel.data.append((input_channel.data[index_input] - start_data) / time_delta)
            
            start_data = input_channel.data[index_input]
            start_time = input_channel.time[index_input]
            current_end_time = start_time + time_delta
            index_input += 1 
        else:
            approximate_data = linear_approximation(input_channel.time[index_input - 1],
                                                    input_channel.data[index_input - 1],
                                                    input_channel.time[index_input],
                                                    input_channel.data[index_input],
                                                    current_end_time)
            return_channel.time.append(current_end_time)
            return_channel.data.append((approximate_data - start_data) / time_delta)
            start_data = approximate_data
            start_time = current_end_time
            current_end_time = start_time + time_delta


def add_constant(channel, constant):
    for i in range(len(channel.data)):
        channel.data[i] += constant

def multiply_by_constant(channel, constant):
    for i in range(len(channel.data)):
        channel.data[i] *= constant


