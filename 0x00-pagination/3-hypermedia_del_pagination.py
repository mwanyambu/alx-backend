#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """Get a dictionary with the following key-value pairs
        """
        assert type(index) == int and type(page_size) == int
        assert index >= 0 and index < len(self.dataset())
        indexed_dataset = self.indexed_dataset()
        dataset = []
        i = index
        while len(dataset) < page_size and i < len(indexed_dataset):
            if i in indexed_dataset:
                dataset.append(indexed_dataset[i])
            i += 1
        return {
            "index": index,
            "next_index": i,
            "page_size": page_size,
            "data": dataset
        }
