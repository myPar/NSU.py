from backward_polish_notation.build_notation import Node
from typing import List
from backward_polish_notation.Exception import *


def calculate(polish_notation: List[Node]) -> float:
    if len(polish_notation) == 1:
        if not (polish_notation[0].type == "operand"):
            raise CalculateException("incorrect expression")
        return polish_notation[0].value

