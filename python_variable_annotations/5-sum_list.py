#!/usr/bin/env python3
"""
    Function that return the sum of floats included in a list
"""


def sum_list(input_list: list[float]) -> float:
    """
        Argument : a list of floats = [floats]

        Returns: the sum of all the floats included in the list

    """
    sum = 0
    for num in input_list:
        sum = float(sum) + num
    return float(sum)
