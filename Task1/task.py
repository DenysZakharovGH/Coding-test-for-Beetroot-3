# Write your code here
# You're given a list of temperatures. Your job is to write a function that finds the temperature closest to zero in the list. You are also to write a test showing that your function works as expected.
#
# If two temperatures are equally close to zero, return the positive temperature.
#
# If the list is empty the function should return 0.

import numpy as np
import math
from data import *

def get_temperature_closest_to_zero(temperatures):

    if temperatures == [] or temperatures == None : # if list is Empty
        return 0
    value = 0 # value for which we come closer
    array = np.array(temperatures) # make np array
    idx = (np.abs(array - value)).argmin() # find proper index

    # if we have more then 1 proper value in array but in different sides of 0 - use module for make it positive
    if math.fabs(array[idx]) in temperatures:
        return math.fabs(array[idx])

    return array[idx]



#print(get_temperature_closest_to_zero(T))




