#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize instance of server class."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self,
                        index: int = None,
                        page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination."""
        assert type(index) == int and type(page_size) == int
        assert index >= 0 and page_size > 0
        assert index < len(self.__indexed_dataset)
        n_idx = index + page_size
        n_idx = n_idx if len(self.__indexed_dataset) > n_idx else None
        data = [self.__indexed_dataset.get(i)
                for i in range(index, index + page_size)
                if self.__indexed_dataset.get(i)]
        return {
                   'index': index,
                   'next_index': n_idx,
                   'page_size': page_size,
                   'data': data
               }
