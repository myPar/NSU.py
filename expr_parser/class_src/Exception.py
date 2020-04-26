import traceback


# standard exception class in parsing of arithmetic expressions
class StandardExpressionException(Exception):
    def __init__(self, text, pos):
        self.text = text
        self.position = pos

    # formatting exception printing
    def throw(self, mode: int):  # mode 0 - user mode; mode 1 - developer mode.
        print("| " + str(type(self)))
        print("| <" + self.__class__.__name__ + "> at pos = " + str(self.position) + ":")
        print("| " + self.text)
        print()
        if mode == 1:
            traceback.print_stack(f=None, limit=None, file=None)    # print full stack trace
        exit(1)


class ZeroDivisionException(StandardExpressionException):
    def __init__(self, text, pos):
        StandardExpressionException.__init__(self, text, pos)


class GetTypeException(StandardExpressionException):
    def __init__(self, text, pos):
        StandardExpressionException.__init__(self, text, pos)


class ParenthesisBalanceException(StandardExpressionException):
    def __init__(self, text, pos):
        StandardExpressionException.__init__(self, text, pos)


class GetOperatorPriorityException(StandardExpressionException):
    def __init__(self, text, pos):
        StandardExpressionException.__init__(self, text, pos)
