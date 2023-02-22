import random
from time import sleep


class Game:
    def __init__(self) -> None:
        self.deck = None

        self.ante = 5
        self.bet = 0

        self.player = Player(input("What is your name?"))
        self.dealer = Dealer("Dealer")
        self.setup()

    def setup(self):  # Initial game set up
        self.deck = Deck()
        self.deck.add_cards()
        self.deck.shuffle()

    def reset(self):  # Reset on new round
        self.deck = Deck()
        self.deck.add_cards()
        self.deck.shuffle()

        self.bet = 0

        self.player.reset()
        self.dealer.reset()

    def greet():
        print("---------------------\nWelcome to BlackJack! I am your dealer")
        print("You have $100 to start - each hand has a $5 ante\n")

    def ante() -> bool:
        inp = input(
            f"\nWould you like to ante ${game.ante} for the next round? You have "
            f"${game.player.money} (y/n): ").lower()
        if inp == "y":
            game.player.money -= game.ante
            game.bet += game.ante
            return True
        elif inp == "n":
            return False
        else:
            invalid()
            ante()


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
    def __init__(self, name: str = "User") -> None:
        self.money = 100
        self.cards = []  # Card player receives
        self.hand = []  # List of values of cards (number/Ace)
        self.total = 0
        self.bust = False
        self.stay = False
        self.name = name

    def draw(self) -> None:
        """Draws new card, handles value assignment and total with Aces
        """
        self.cards.append(game.deck.draw_card())
        self.hand.append(self.cards[-1].value)

        # Calculate total and consider aces
        if "A" not in self.hand:  # No aces, simple addition
            self.total = sum(self.hand)
        else:
            ace_eleven = sum(
                [val if val != "A" else 11 for val in self.hand])
            if ace_eleven <= 21:  # Total with aces < 21, Ace = 11
                self.total = ace_eleven
            else:  # Total with aces > 21, Ace = 1
                ace_one = sum(
                    [val if val != "A" else 1 for val in self.hand])
                self.total = ace_one

        print(f"\n{self.user} received a {self.cards[-1]}\n")

        if (self.total > 21):
            self.bust = True

        sleep(.5)

        if self.bust:
            print(f"Total:  {self.total}. {self.name} busted!")
        if self.total == 21:
            print(f"{self.name} got 21! {self.name} stays")
            self.stay = True

    def reset(self):
        """Reset hand for new round
        """
        self.cards = []  # Card player receives
        self.hand = []  # List of values of cards (number/Ace)
        self.total = 0
        self.bust = False
        self.stay = False

    def hit_stay(self):
        valid = False
        while not valid:
            inp = input("Hit or Stay? (h/s) ").lower()
            if inp == "h" or inp == "hit":
                valid = True
                player_draw()
            elif inp == "s" or inp == "stay":
                print(
                    f"\n{self.name} stayed. {self.name} has {self.total} in hand\n")
                self.stay = True
                valid = True
            else:
                invalid()


class Dealer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.money = None


game = Game()


def invalid():
    print("Please input a valid response")


def print_hands():
    print("\nCurrent Hands:\n")
    print(f"{game.player.name: < 11}{'Dealer': < 10}")
    [print(f"{player_card: > 8} |  {dealer_card: <10}")
     for player_card, dealer_card in zip(game.player.cards, game.dealer.cards)]


def win_loss():
    if game.player.bust:
        print("You lost this round!")
    elif game.player.total == 21 and len(game.player.hand) == 2:
        print(f"You got BLACKJACK! You received {game.bet * 3}.")
        game.player.money += game.bet * 3
    elif game.dealer.bust or game.player.total > game.dealer.total:
        print(f"You win! You received {game.bet * 2}.")
        game.player.money += game.bet * 2
    elif game.dealer.bust or game.player.total <= game.dealer.total:
        print("House wins, You lose!")

    game.reset()


def play_game():
    game.setup()

    game.greet()

    while (game.player.money > 0):
        if not game.ante():
            print("Thanks for playing!")
            return

        # Initial deal
        game.dealer.draw()

        sleep(.5)
        game.player.draw()
        sleep(.5)
        game.player.draw()

        print_hands()

        # game.player.hit_stay()

        # Player turn
        while not game.player.bust and not game.player.stay and game.player.total != 21:
            # player_draw()
            if game.player.bust or game.player.stay:
                break
            game.player.hit_stay()
            sleep(.5)
            print_hands()

        # Dealer turn
        if not game.player.bust:
            sleep(.5)
            game.dealer.draw()

        while game.dealer.total < 17:
            sleep(.5)
            print("Dealer draws again!")
            sleep(5)
            game.dealer.draw()

        if not game.dealer.bust and not game.dealer.stay:
            print("Dealer stays!")
            game.dealer.stay = True

        sleep(5)
        print_hands()

        sleep(5)
        win_loss()

    print("You are out of money. Thanks for playing!")


if __name__ == "__main__":
    play_game()
