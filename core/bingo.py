import random


class BingoCage:
    def __init__(self, items_len=100):
        self._items = list(range(1, items_len))
        self._match_numbers = []
        random.shuffle(self._items)

    def pick(self):
        try:
            self._match_numbers.append(str(self._items.pop()))
        except IndexError:
            raise LookupError('pick from empty BingoCage')
