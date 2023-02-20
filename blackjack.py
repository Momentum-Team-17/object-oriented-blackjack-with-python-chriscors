class Game:
    pass


class Deck:
    SUITS = ["♥️", "♦️", "♣️", "♠️"]
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self) -> None:
        cards_list = []

    def add_cards():
        for suit in SUITS:
            for rank in RANKS:
                cards_list.append(Card(suit, rank))


class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


deck1 = Deck()
deck1.
