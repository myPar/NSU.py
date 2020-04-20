# standard exception class in parsing of arithmetic expressions
class StandardExpressionException(Exception):
    def __index__(self, text, pos):
        self.text = text
        self.position = pos


class ZeroDivisionException(StandardExpressionException):
    pass


class GetTypeException(StandardExpressionException):
    pass


class ParenthesisBalanceException(StandardExpressionException):
    pass
