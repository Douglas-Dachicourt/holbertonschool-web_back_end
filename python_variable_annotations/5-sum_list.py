#!/usr/bin/env python3
"""
    Function that return the sum of floats included in a list
"""
from typing import List
"""
    typing import to get a list type annotation
"""


def sum_list(input_list: List[float]) -> float:
    """
        Argument : a list of floats = [floats] - type list and float

        Variables : sum = initialized to zero before entering in the loop
                    num = element at each index of the list to be added
                    to the sum

        Returns: the sum of all the floats included in the list - type float

    """
    sum = 0

    for num in input_list:
        sum = float(sum) + num
    return float(sum)
