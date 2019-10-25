# Write your tests here
import numpy as np
import math
from task import *
from data import *


def test_get_temperature_closest_to_zero():
    assert 0.1 == (get_temperature_closest_to_zero(T))
    print("+ test_get_temperature_closest_to_zero complite with SUCCESS")

def test_get_zero_if_list_is_empty():
    assert 0 == (get_temperature_closest_to_zero(t_empty))
    print("+ test_list_is_empty complite with SUCCESS")

def test_get_temperature_if_list_have_same_values():
    assert 0.1 == (get_temperature_closest_to_zero(T))
    print("+ test_get_temperature_if_list_same_values complite with SUCCESS")


test_get_temperature_closest_to_zero()
test_get_zero_if_list_is_empty()
test_get_temperature_if_list_have_same_values()
