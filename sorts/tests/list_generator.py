import random
from typing import List


def get_random_list(length: int) -> List[float]:  # generates random float list with fixed length
    random_list = []

    for i in range(length):
        random_list.append(random.uniform(-10000, 10000))
    return random_list


def get_random_int_list(length: int) -> List[int]:  # generates random int list with fixed length
    random_list = []

    for i in range(length):
        random_list.append(int(random.uniform(0, 1000)))
    return random_list
