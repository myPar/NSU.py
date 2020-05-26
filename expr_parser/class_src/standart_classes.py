from enum import Enum
from expr_parser.class_src.Exception import*
import re
mode = 1    # global variable means the mode of exception printing


# character type enum
class Type(Enum):
    OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
    CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"
    OPERATOR = "OPERATOR"
    OPERAND = "OPERAND"
    IDENT = "IDENT"


# just standard node for tree structures
class StandardNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# this child class is using for making nodes of arithmetic expressions AST
class AstNode(StandardNode):
    def __init__(self, value, pos):
        StandardNode.__init__(self, value)
        self.position = pos  # Token position in input arithmetic expression
        self.type = self.get_type()  # Token type

        self.size = 0       # this field recognize the vertical size of OPERATOR block or vertical size of IDENT
        self.h_offset = 0   # horizontal offset of Token
        self.v_offset = 0   # vertical offset of Token

    # check if IDENT consist from several number of characters and starts with zero
    def is_correct_ident(self):
        if len(self.value) > 1 and self.value[0] == "0":
            StandardExpressionException("incorrect IDENT", self.position).throw(mode)

    def get_type(self):
        if self.value == "(":
            return Type.OPEN_PARENTHESIS
        if self.value == ")":
            return Type.CLOSE_PARENTHESIS
        if re.search(r'[\+\*\/\-\(\)]', self.value):
            return Type.OPERATOR
        if re.search(r'[0-9]', self.value):
            self.is_correct_ident()
            return Type.IDENT
        if re.search(r'[A-Za-z]', self.value):
            return Type.OPERAND
        GetTypeException("Unresolved character in arithmetic expression", self.position).throw(mode)

    def get_priority(self) -> int:
        if self.type == Type.OPERATOR:
            if self.value == "-" or self.value == "+":
                return 1
            if self.value == "/" or self.value == "*":
                return 2
        GetOperatorPriorityException("only OPERATOR type tokens has the priority", self.position).throw(mode)

    def print(self):
        print("{type=" + self.type.name + " , val= '" + self.value + "'" + " , pos=" + str(self.position) + "}")
