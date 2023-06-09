from csv import DictReader
from random import shuffle
from pprint import pformat


class Card:
    """A playing card."""

    def __init__(self, value, card_num, suit, color):
        self.value = value
        self.card_num = card_num
        self.suit = suit
        self.color = color

    @classmethod
    def from_dict(cls, card_dict):
        """Return a Card from a dict.

        Dict must have keys: value, card_num, suit, color."""

        return cls(value=card_dict['value'],
                   card_num=int(card_dict['card_num']),
                   suit=card_dict['suit'],
                   color=card_dict['color'])

    def __repr__(self):
        return f"<Card: {self.value} of {self.suit}>"


class Deck:
    """A Deck of Cards."""

    def __init__(self, cards=[]):
        self.cards = cards

    @classmethod
    def from_csv(cls, filename):
        """Return a Deck from a .csv file.

        File must have headings: value, card_num, suit, color."""

        cards = []

        with open(filename) as csvfile:
            reader = DictReader(csvfile)

            for row in reader:
                cards.append(Card.from_dict(row))

        return cls(cards=cards)

    def __repr__(self):
        return pformat(self.cards)

    def shuffle_cards(self):
        """Shuffle deck."""

        shuffle(self.cards)

    def sort_by_num(self):
        """Sort deck by Card.card_num"""

        self.cards.sort(key=lambda c: c.card_num)

    def sort_by_suit(self):
        """Sort deck by Card.suit"""

        self.cards.sort(key=lambda c: c.suit)

    def sort_by_color(self):
        """Sort deck by Card.color"""

        self.cards.sort(key=lambda c: c.color)


if __name__ == '__main__':
    csv_deck = Deck.from_csv('deck.csv')
    csv_deck.shuffle_cards()

    hand = Deck(csv_deck.cards[:13])
