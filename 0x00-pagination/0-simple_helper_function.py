#!/usr/bin/env python3

""" simple helper function """


def index_range(page, page_size):
    """ takes two integer args and returns a tuple of size two """
    if page < 1 or page_size < 1:
        raise ValueError("page numbers should be positive integers")

    start = (page - 1) * page_size
    end = start + page_size

    return start, end
