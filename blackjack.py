import random


class Game:
    def __init__(self) -> None:
        self.deck = None
        self.play = None
        self.dealer = None
        self.setup()

    def setup(self):
        self.deck = Deck()
        self.deck.add_cards()


class Deck:
    SUITS = ["♥️", "♦️", "♣️", "♠️"]
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self) -> None:
        self.cards_list = []

    def add_cards(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards_list.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards_list)


class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


game = Game()
