from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for character_index, character in enumerate(pattern):
        table[character] = max(1, len(pattern) - character_index - 1)
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.pattern_length = len(pattern)
        self.text_length = len(text)
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        return self.table.get(c, self.pattern_length)

    def search(self) -> int:
        if self.text == self.pattern:
            return 0
        pattern_index = self.pattern_length - 1
        text_index = 0
        while text_index <= self.text_length - self.pattern_length:
            shift_characters = 0
            while pattern_index >= 0:
                if self.pattern[pattern_index] != self.text[text_index + pattern_index]:
                    if self.decide_slide_width(self.text[text_index + pattern_index]):
                        shift_characters = self.decide_slide_width(
                            self.text[text_index + pattern_index])
                    else:
                        shift_characters = self.pattern_length
                    pattern_index -= 1
                    break
                pattern_index -= 1
            text_index += shift_characters
            if shift_characters == 0:
                return text_index

        return -1
