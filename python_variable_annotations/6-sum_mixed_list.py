#!/usr/bin/env python3
"""
 Function that return the sum of floats included in a list
"""
from typing import List, Union
"""
    typing import to get a list type annotation: such as List and Union
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Argument : a list of int and floats = [int, floats]
            -> type list and float using Union notation

        Variables : sum = initialized to zero before entering in the loop
                    num = element at each index of the list to be added
                    to the sum

        Returns: the sum of all the int and floats included in the list
            -> type float

    """
    sum = 0
    for num in mxd_lst:
        sum = float(sum) + num
    return sum
