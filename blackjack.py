import random


class Game:
    def __init__(self) -> None:
        self.deck = None

        self.ante = 5
        self.bet = None

        self.dealer = None
        self.player = Player()
        self.dealer = Dealer()
        self.setup()

    def setup(self):  # Initial game set up
        self.deck = Deck()
        self.deck.add_cards()
        self.deck.shuffle()

    def reset(self):  # Reset on new round
        self.deck = Deck()
        self.deck.add_cards()
        self.deck.shuffle()

        self.bet = None

        self.player.reset()
        self.dealer.reset()


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
        self.cards = []  # Card player receives
        self.hand = []  # List of values of cards (number/Ace)
        self.total = 0
        self.bust = False
        self.stay = False

    def draw(self) -> None:
        """Draws new card, handles hand value assignment and total with Aces
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

        if (self.total > 21):
            self.bust = True

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
                self.draw()
            elif inp == "s" or inp == "stay":
                print(f"\nYou stayed. You have {game.player.total}\n")
                self.stay = True
                valid = True
            else:
                invalid()


class Dealer(Player):
    def __init__(self) -> None:
        self.money = None


def invalid():
    print("Please input a valid response")


def greet():
    print("---------------------\nWelcome to BlackJack! I am your dealer")
    print("You have $100 to start - each hand has a $5 ante\n")


def ante() -> bool:
    inp = input(
        f"Would you like to ante ${game.ante} for the next round? You have "
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


def initial_draw():
    game.dealer.initial_draw()
    game.player.draw()

    print(f"\nThe dealer drew a {game.dealer.cards[0]}")
    print(f"\nYou received a {game.player.cards[0]}\n")
    game.player.hit_stay()


def player_draw() -> bool:
    game.player.draw()

    print(f"\nYou received a {game.player.cards[-1]}\n")
    if game.player.bust:
        print(f"Total:  {game.player.total}. You busted!")
    if game.player.total == 21:
        print("You got 21! You stay")
        game.player.stay = True
    else:
        print("Hand:")
        [print(f"   {card}") for card in game.player.cards]
        print(f"Total: {game.player.total}\n")


def dealer_draw() -> bool:
    game.dealer.draw()

    print(f"\nDealer received a {game.dealer.cards[-1]}\n")
    if game.dealer.bust:
        print(f"Total:  {game.player.total}. Dealer busted!")
    else:
        print("Hand:")
        [print(f"   {card}") for card in game.player.cards]
        print(f"Total: {game.player.total}\n")

    if game.dealer.total < 17:
        print("Dealer draws again!")
        dealer_draw()
    else:
        print("Dealer stays!")
        game.dealer.stay = True


def win_loss():
    if game.player.bust:
        print("You lost this round!")
    elif game.player.total == 21 and len(game.player.hand) == 2:
        print(f"You got BLACKJACK! You received {game.bet}.")
        game.player.money += game.bet * 3
    elif game.dealer.bust or game.player.total > game.dealer.total:
        print(f"You win! You received {game.bet}.")
        game.player.money += game.bet * 2

    game.reset()


game = Game()


def play_game():
    game.setup()

    greet()

    while (game.player.money > 0):
        if not ante():
            break

        initial_draw()  # Player and Dealer receive cards

        # Player turns (hit stay bust)
        while not game.player.bust and not game.player.stay:
            player_draw()
            if game.player.bust or game.player.stay:
                break
            game.player.hit_stay()

        # Dealer turns (hit stay bust)
        # while not game.dealer.bust and not game.dealer.stay:
        # ?I THINK this handles recursion for us
        if not game.player.bust:
            dealer_draw()

        win_loss()
    print("You are out of money. Thanks for playing!")


if __name__ == "__main__":
    play_game()
