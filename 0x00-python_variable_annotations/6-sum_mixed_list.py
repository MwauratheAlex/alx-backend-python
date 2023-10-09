#!/usr/bin/env python3
"""This module contains the functon sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list - sums a list
    @mxd_lst: list to sum
    Return: sum of values in mxd_lst
    """
    return sum([n for n in mxd_lst])
