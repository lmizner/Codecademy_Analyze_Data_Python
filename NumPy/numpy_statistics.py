
# NUMPY AND MEAN
import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])


# Find the average sales for each store, and save them to the variables store_one_avg, store_two_avg, and store_three_avg.
store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)


# Print the averages to the terminal.
print(store_one_avg)
print(store_two_avg)
print(store_three_avg)


# Notice the average sales per week for each store. 
# The boss says that we should increase what we stock, but only if the store’s average sales are greater than 7 bottles per week.
# Save the store dataset variable name that fits this description to the variable best_seller.
best_seller = store_two



####################################



# MEAN AND LOGICAL OPERATIONS
import numpy as np

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952,
                       2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988,
                       2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013,
                       1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977,
                       1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015,
                       2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987,
                       1992, 2008, 1979, 1987])


# We’ve saved this list as a NumPy array to the variable class_year. 
# Calculate the percent of attending alumni who graduated on and after 2005 and save your result to the variable millennials.
millennials = np.mean(class_year >= 2005)


# Print the value of millennials to the terminal.
print(millennials)



####################################



# CALCULATING THE MEAN OF 2D ARRAYS
import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])


# Use np.mean to find the average level of drowsiness across all the trials and save the result to the variable total_mean.
total_mean = np.mean(allergy_trials)


# Use np.mean to find the average level of drowsiness across each day of the experiment and save to the variable trial_mean.
trial_mean = np.mean(allergy_trials, axis = 1)


# Use np.mean to find the average level of drowsiness across for each individual patient to see if some were more sensitive to the drug than others and save it to the variable patient_mean.
patient_mean = np.mean(allergy_trials, axis = 0)


# Print the variables for total_mean, trial_mean, and patient_mean on three separate lines.
print(total_mean)
print(trial_mean)
print(patient_mean)



####################################



# SORTING AND OUTLIERS
import numpy as np

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88,
                  96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86,
                  92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90,
                  90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])


# First, sort the temps data array and save the sorted data to a sorted_temps variable.
sorted_temps = np.sort(temps)


# Now, print the sorted_temps array. What do we see? Did the grill, in fact, create outliers in our data?
print(sorted_temps)



####################################



# NUMPY AND MEDIAN
import numpy as np

large_set = np.genfromtxt('household_income.csv', delimiter=',')


# You’re doing some research on household incomes and come across the following small dataset:
# 10100, 35500, 105000, 85000, 25500, 40500, 65000
# Calculate the median, without using Numpy, and save the value to the variable small_set_median.
small_set_median = 40500


# Use NumPy to find the median of large_set and save the result to the variable large_set_median.
large_set_median = np.median(large_set)


# Print the results of small_set_median and large_set_median to the terminal.
print(small_set_median)
print(large_set_median)



####################################



# MEAN VS. MEDIAN
import numpy as np

time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)


# Find the average amount of time in minutes spent on the website and save it to the variable minutes_mean.
minutes_mean = np.mean(time_spent)


# Now, find the median of the array and save it to the variable minutes_median.
minutes_median = np.median(time_spent)


# Print the mean and the median to the terminal.
print(minutes_mean)
print(minutes_median)


# Take a moment to notice the difference between the two values. Which one do you think best represents the majority of the data present?
# Choose the variable that represents this value, and save it to the variable best_measure.
best_measure = minutes_median



####################################



# PERCENTILES - PART I
import numpy as np

patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])


# Use NumPy to find the 30th percentile of the sorted array and save it to a variable named thirtieth_percentile.
thirtieth_percentile = np.percentile(patrons, 30)


# Next, use NumPy to find the 70th percentile and save it to the variable seventieth_percentile.
seventieth_percentile = np.percentile(patrons, 70)


# Print the 30th and 70th variables to the terminal.
print(thirtieth_percentile)
print(seventieth_percentile)



####################################



# PERCENTILES - PART II
import numpy as np

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])


# Find the 25th and 75th percentiles, and save them to the corresponding variables: first_quarter and third_quarter.
first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)


# Create a variable named interquartile_range. Calculate the interquartile range and save it to this variable.
interquartile_range = third_quarter - first_quarter


# Print the results of the 25th percentile, 75th percentile, and interquartile range to the terminal.
print(first_quarter)
print(third_quarter)
print(interquartile_range)



####################################



# STANDARD DEVIATION
import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])


# Given the two data sets at the top of script.py, find the average weight for each competition and save them to the variables pumpkin_avg and acorn_squash_avg.
pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)


# Calculate the standard deviation for each of the datasets to find and save them to the variables pumpkin_std and acorn_squash_std.
# Print them to the console to see their values.
pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)

print(pumpkin_std)
print(acorn_squash_std)


# Determine the squash dataset that has the greater standard deviation and save it to the variable winner.
winner = pumpkin



####################################



# REVIEW
import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])


# Find the mean of the rainfall array and save it to the variable rain_mean.
rain_mean = np.mean(rainfall)


# Find the median of the rainfall array and save it to the variable rain_median.
rain_median = np.median(rainfall)


# Find the 25th and the 75th percentiles of the original rainfall array and save them to the arrays first_quarter and third_quarter, respectively.
first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)


# Calculate the interquartile range and save it to the variable, interquartile_range.
interquartile_range = third_quarter - first_quarter


# Determine the standard deviation of the set and save it to the variable rain_std.
rain_std = np.std(rainfall)


# Print the variables to the terminal to see your results.
print(rain_mean)
print(rain_median)
print(first_quarter)
print(third_quarter)
print(interquartile_range)
print(rain_std)

