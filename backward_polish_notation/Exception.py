class PolishNotationException(Exception):
    def __index__(self, text):
        self.text = text


class SyntaxException(PolishNotationException):
    pass


class ParenthesisException(PolishNotationException):
    pass


class CalculateException(PolishNotationException):
    pass
