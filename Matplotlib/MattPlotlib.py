from matplotlib import pyplot
from numpy import NAN
import pandas





csv_reader = pandas.read_csv("Matplotlib/ads_endurance.csv", header=15) 
#read the data into a dictionary with column names as headers


figure, axis = pyplot.subplots(3, 1) # create subplots with x rows and y columns
figure.set_facecolor('black') #set back ground to black


# create a total pressure column in my csv_reader

axis[0].plot(csv_reader['Time'], csv_reader['Brake Pressure Front'] , label="Brake Pressure Front")
axis[0].plot(csv_reader['Time'], csv_reader['Brake Pressure Rear'], color='r', label="Brake Pressure Rear")
axis[0].legend(loc='upper left')
axis[0].spines['bottom'].set_color('#dddddd')
axis[0].spines['top'].set_color('#dddddd') 
axis[0].spines['right'].set_color('#dddddd')
axis[0].spines['left'].set_color('#dddddd')
axis[0].tick_params(axis='x', colors='#dddddd')
axis[0].tick_params(axis='y', colors='#dddddd')

axis[1].plot(csv_reader['Time'], csv_reader['Added Sensors Brakes Rear Brake Temp Sensor Voltage'], label="Added Sensors Brakes Rear")
axis[1].plot(csv_reader['Time'], csv_reader['Added Sensors Brakes Front Brake Temp Sensor'], color='r', label="Added Sensors Brakes front")
axis[1].legend(loc='upper left')

axis[1].spines['bottom'].set_color('#dddddd')
axis[1].spines['top'].set_color('#dddddd') 
axis[1].spines['right'].set_color('#dddddd')
axis[1].spines['left'].set_color('#dddddd')
axis[1].tick_params(axis='x', colors='#dddddd')
axis[1].tick_params(axis='y', colors='#dddddd')

axis[1].set_facecolor('#000000')  
axis[0].set_facecolor('#000000')
axis[2].set_facecolor('#000000')

# plot the top two graphs and set the design to specifications


csv_reader['Total Brake Pressure'] = csv_reader.apply(lambda column: column['Brake Pressure Front'] + column['Brake Pressure Rear'] if column['Brake Pressure Front'] + column['Brake Pressure Rear'] > 0 else NAN, axis=1)
csv_reader['Brake Bias'] = csv_reader.apply(lambda column: column['Brake Pressure Front'] / column['Total Brake Pressure'] if column['Total Brake Pressure'] > 5 else NAN, axis=1)
axis[2].scatter(csv_reader['Brake Pressure Front'], csv_reader['Brake Bias'], color='red')
axis[2].set_ylim(0.55, 0.95)
axis[2].spines['bottom'].set_color('#dddddd')
axis[2].spines['top'].set_color('#dddddd') 
axis[2].spines['right'].set_color('#dddddd')
axis[2].spines['left'].set_color('#dddddd')
axis[2].tick_params(axis='x', colors='#dddddd')
axis[2].tick_params(axis='y', colors='#dddddd')



pyplot.show()

"""

data_dictionary = {}

for _ in range(14):
    next(csv_reader) #remove top extra rows


headers =next(csv_reader)

for head in headers:
    data_dictionary[head] = []


units = next(csv_reader)

for _ in range(2):
    next(csv_reader) #remove more extra rows

for _ in range(30):
    rows = next(csv_reader)
    for index, item in enumerate(rows):
        data_dictionary[headers[index]].append(item)

pyplot.plot(data_dictionary['Time'], data_dictionary["Brake Pressure Front"])
pyplot.show()

"""