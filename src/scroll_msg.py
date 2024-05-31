class ScrollMessage:  # 4char alphanumeric scrolling message
    max_char_len = 4

    def __init__(self, msg, index=0):
        self.text = msg
        self.index = index

    def set_index(self, index):
        self.index = index

    def is_next(self):
        return self.index < len(self.text)

    def get_next(self, index=-1):
        result = ""
        dot_count = 0
        message_to_display = self.text[self.index:]

        self.index = self.index if index == -1 else index
        leading_dot_count = len(message_to_display) - len(message_to_display.lstrip('.'))
        self.index += leading_dot_count

        for char in message_to_display.lstrip("."):
            if char != ".":
                result += char
                dot_count = 0
            elif char == "." and dot_count < 1:
                result += char
                dot_count += 1
            if len(result.replace(".", "")) >= self.max_char_len:
                break
        self.index += 1
        return result

    def __str__(self):
        return f"ScrollMessage({self.text}, {self.index})"
