import collections

from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 定义每种花色牌面
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 定义花色类型
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
print(deck[-1])

print(choice(deck))
