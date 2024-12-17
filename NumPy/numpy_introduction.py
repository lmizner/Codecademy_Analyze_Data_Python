# You are working on a team of climate scientists and one of your roles is to take the weekly temperature data and input into NumPy arrays for later analysis. 
# The sensor records the temperature 4 times a day, at 0:00, 6:00, 12:00, and 18:00.
# You are given last weeks data (Monday through Friday) and asked to create a NumPy array.
# Get started by importing the numpy package.
import numpy as np


# Create an array temperatures by importing the data in the CSV temperature_data.csv
temperatures = np.genfromtxt('temperature_data.csv', delimiter = ',')


# Inspect the data by printing it to the terminal.
# The columns are the times, starting at 0:00, and the rows are days, starting on Monday, and the values are the recorded temperatures at that time on those days.
print(temperatures)


# One of the researchers noticed that the sensor had been incorrectly zeroed and all of the recorded temperatures are 3.0 degrees too cold.
# Adjust the array so that the temperature readings are accurate and save them to temperatures_fixed.
temperatures_fixed = temperatures + 3


# Another researcher asked you for the temperature values from Monday. Save them to a new array, monday_temperatures.
monday_temperatures = temperatures_fixed[0]


# “Hmmm, interesting” the researcher mumbles, “can you also give me the 6:00 AM data for Thursday and Friday?”
# Save this data to a new array thursday_friday_morning.
thursday_friday_morning = temperatures_fixed[3:5, 1]


# Finally, the persistent researcher now wants all the high and low temperatures over the week.
# Select all temperatures that are under 50 degrees or over 60 degrees and save them to a new array temperature_extremes.
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]




