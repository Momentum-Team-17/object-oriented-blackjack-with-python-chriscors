import random


class Game:
    def __init__(self) -> None:
        self.deck = None
        self.play = None
        self.dealer = None
        self.player = Player()
        self.dealer = Dealer()
        self.setup()

    def setup(self):
        self.deck = Deck()
        self.deck.add_cards()
        self.deck.shuffle()


class Deck:
    SUITS = ["♥️", "♦️", "♣️", "♠️"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self) -> None:
        self.cards = []

    def add_cards(self):
        [[self.cards.append(Card(suit, rank))
            for rank in self.RANKS] for suit in self.SUITS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

        if self.rank.isdigit():
            self.value = int(self.rank)
        elif self.rank == "A":
            self.value = "A"
        else:
            self.value = 10

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Player:
    def __init__(self) -> None:
        self.money = 100
        self.card = []  # Card player receives
        self.hand = []  # List of values of cards (number/Ace)
        self.bust = False

    def draw(self) -> None:
        self.card.append(game.deck.draw_card())
        self.hand.append(self.card[-1].value)


class Dealer(Player):
    def __init__(self) -> None:
        self.money = None

    def draw(self):
        self.card.append(game.deck.draw_card())


def greet():
    print("---------------------\nWelcome to BlackJack! I am your dealer")
    print("You have $100 to start - each hand has a $5 ante\n")


def ante() -> bool:
    inp = input(
        f"Would you like to ante $5 for the next round? You have ${game.player.money} (y/n): ").lower()
    if inp == "y":
        game.player.money -= 5
        return True
    elif inp == "n":
        return False
    else:
        print("Please input a valid response")
        ante()


def initial_draw():
    game.dealer.initial_draw()
    game.player.draw()

    print(f"\nThe dealer drew a {game.dealer.card[0]}")
    print(f"\nYou received a {game.player.card[0]}")


def player_draw() -> bool:
    game.player.draw()
    print(f"\nYou received a {game.player.card[0]}\n")
    print(f"Hand:\n")
    [print(f"   {card}")]


game = Game()


def play_game():
    game.setup()

    greet()

    while (game.player.money > 0):
        if not ante():
            break

        initial_draw()

        while not game.player.bust:
            player_draw()


if __name__ == "__main__":
    play_game()
