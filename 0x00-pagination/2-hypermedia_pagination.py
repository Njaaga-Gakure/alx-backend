#!/usr/bin/env python3
"""Helper function."""

import csv
import math
from typing import Tuple, List, Dict, Union


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


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize an instance of the Server class."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a range of entries in a file.

        args:
            page (int): the you want to start with
            page_size: the size of the page
        Return:
            data from the specified range

        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        self.dataset()
        range = index_range(page, page_size)
        if range[0] >= len(self.__dataset) or range[1] > len(self.__dataset):
            return []
        return self.__dataset[range[0]:range[1]]

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> Dict[str,
                                               Union[int, str, List[List]]]:
        """Return a dict with attributes decribing a paginated dataset."""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if total_pages > page else None
        prev_page = page - 1 if page != 1 else None
        return ({
                    'page_size': page_size,
                    'page': page,
                    'data': self.get_page(page, page_size),
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': total_pages,
                })
