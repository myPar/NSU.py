import random
from typing import List


def get_random_list(length: int) -> List[float]:  # generates random list with fixed length
    random_list = []

    for i in range(length):
        random_list.append(random.uniform(-10000, 10000))
    return random_list
