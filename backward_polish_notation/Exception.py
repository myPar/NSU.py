class SyntaxException(Exception):
    def __index__(self, text):
        self.text = text


class ParenthesisException(Exception):
    def __index__(self, text):
        self.text = text


class CalculateException(Exception):
    def __index__(self, text):
        self.text = text
