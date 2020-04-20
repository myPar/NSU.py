from enum import Enum
from expr_parser.class_src.Exception import*
import re


# character type enum
class Type(Enum):
    OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
    CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"
    OPERATOR = "OPERATOR"
    OPERAND = "OPERATOR"
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
        self.position = pos
        self.type = self.get_type(self)

    def get_type(self):
        if self.value == "(":
            return Type.OPEN_PARENTHESIS
        if self.value == ")":
            return Type.CLOSE_PARENTHESIS
        if re.search(r'[\+\*\/\-\(\)]', self.value):
            return Type.OPERATOR
        if re.search(r'[0-9]'):
            return Type.IDENT
        if re.search(r'[A-Za-z]'):
            return Type.OPERAND
        raise GetTypeException("Unresolved character in arithmetic expression", self.position)
