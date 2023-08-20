#!/usr/bin/env python3
"""Helper function."""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return range of indexes.

    args:
        page (int): page you are on
        page_size (int): size of the page
    Return:
        range of indexes
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
