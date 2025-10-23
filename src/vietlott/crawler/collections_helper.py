"""collection utilities"""

import itertools


def chunks_iter(data, n):
    """split data"""
    it = iter(data)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk
