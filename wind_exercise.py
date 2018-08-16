import numpy as np

data = np.loadtxt("Numpy-Tutorial-SciPyConf-2018\exercises\wind_statistics\wind.data")
wind_dates = data[:, 0:-12]
wind_data = data[:,-12:]
print(data.shape)

#Wind Statistics
#----------------

#Topics: Using array methods over different axes, fancy indexing.

#1. The data in 'wind.data' has the following format::
#
#        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
#        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
#        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

#   The first three columns are year, month and day.  The
#   remaining 12 columns are average windspeeds in knots at 12
#   locations in Ireland on that day.

#   Use the 'loadtxt' function from numpy to read the data into
#   an array.

#2. Calculate the min, max and mean windspeeds and standard deviation of the
#   windspeeds over all the locations and all the times (a single set of numbers
#   for the entire dataset).

print(wind_data)
min = np.min(wind_data)
max = np.max(wind_data)
mean = np.mean(wind_data)
std = np.std(wind_data)

print(min, max, mean, std)

#3. Calculate the min, max and mean windspeeds and standard deviations of the
#   windspeeds at each location over all the days (a different set of numbers
#   for each location)

print(np.min(wind_data, axis=0))
print(wind_data.max(axis=0))

#4. Calculate the min, max and mean windspeed and standard deviations of the
#   windspeeds across all the locations at each day (a different set of numbers
#   for each day)

print(np.min(wind_data, axis=1))

#5. Find the location which has the greatest windspeed on each day (an integer
#   column number for each day).

print(np.argmax(wind_data, axis=0))

#6. Find the year, month and day on which the greatest windspeed was recorded.
wind_table_of_truth = wind_data == wind_data.max()
position_of_max = np.nonzero(wind_table_of_truth)

print(wind_dates[position_of_max[0], :])

#7. Find the average windspeed in January for each location.

wind_table_of_truth = wind_dates[:, 1] == 1

print(wind_table_of_truth)
print(np.mean(wind_data[wind_table_of_truth, :], axis=0))

#You should be able to perform all of these operations without using a for
#loop or other looping construct.

"""
#Bonus
1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)
"""

"""
2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.
"""

"""
Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)
"""

"""
Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.

See :ref:`wind-statistics-solution`.
"""
