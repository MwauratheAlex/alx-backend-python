#!/usr/bin/env python3
"""This module contains the function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list - returns sum of floats in input_list as a float.
    @input_list: list of floats
    Return: sum of floats in input_list
    """
    return sum([n for n in input_list])
