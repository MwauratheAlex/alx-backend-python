#!/usr/bin/env python3
"""This module contains the function element_length"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences and return
    a list of tuples containing the elements and their respective lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (e.g., a list of strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains a
        sequence from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
