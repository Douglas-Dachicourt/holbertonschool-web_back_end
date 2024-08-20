#!/usr/bin/env python3
"""
    Module that provide a function that return a tuple of size two
    containing a start index and an end index corresponding to the
    range of indexes to return in a list for those particular pagination
    parameters.
"""
from typing import Tuple, List, Dict
import csv
"""
    import Tuple and csv from typing module and python
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        index_range function that takes two arguments

        Arguments:
            - page: type int,
            - page_size: type int,

        Returns: a tuple of numbers , type int

    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "./Popular_Baby_Names.csv"

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            get_page method to find the right informations to show up

            Arguments:
                - page: type int, current page we are visiting, default page 1
                - page_size: type int, number of item showed per page

            Returns:
                a list of list with content

        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
            get_hyper method to find the right informations to show up

            Arguments:
                - page: type int, current page we are visiting, default page 1
                - page_size: type int, number of item showed per page

            Returns:
                a dictionary with key/values needed for pagination
        """
        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = (total_items + page_size - 1) // page_size
        start_index, end_index = index_range(page, page_size)
        data = dataset[start_index:end_index]

        dictionary = {
            "page_size": page_size % 10,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_page": total_pages
        }

        return dictionary
