import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print(ridership[1, 3])
    print(ridership[1:3, 3:5])
    print(ridership[1, :])
    
# Vectorized operations on rows or columns
if False:
    print(ridership[0, :] + ridership[1, :])
    print(ridership[:, 0] + ridership[:, 1])
    
# Vectorized operations on entire arrays
if False:
    a = np.array([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]])
    b = np.array([
        [1, 1, 1], 
        [2, 2, 2], 
        [3, 3, 3]])
    print(a + b)

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    Hint: NumPy's argmax() function might be useful:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
    '''

    max_riders_station = ridership[0, :].argmax()
    
    overall_mean = ridership.mean()# Replace this with your code
    mean_for_max = ridership[:, max_riders_station].mean() # Replace this with your code
    
    return (overall_mean, mean_for_max)

def min_and_max_riders_per_day(ridership):
    '''
    Fill in this function. First, for each subway station, calculate the
    mean ridership per day. Then, out of all the subway stations, return the
    maximum and minimum of these values. That is, find the maximum
    mean-ridership-per-day and the minimum mean-ridership-per-day for any
    subway station.
    '''

    means_per_day = ridership.mean(axis=0)

    max_daily_ridership = means_per_day.max()
    min_daily_ridership = means_per_day.min()
    
    return (max_daily_ridership, min_daily_ridership)

print(mean_riders_for_max_station(ridership))