#!/usr/bin/env python3

""" simple helper function """
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
    
    def index_range(page: int, page_size: int):
        """
        takes two integer args and returns a tuple of size two
        """
        if page < 1 or page_size < 1:
            raise ValueError("page numbers should be positive integers")

        start = (page - 1) * page_size
        end = start + page_size

        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page with the given page number and page size
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = Server.index_range(page, page_size)
        dataset = self.dataset()

        return dataset[startIndex:endIndex]