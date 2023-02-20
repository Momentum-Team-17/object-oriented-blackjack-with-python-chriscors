# Object Oriented Blackjack With Python

## Upon completion of this assignment, students will be able to:
- Write classes in Python, and determine appropriate attributes for those classes.
- Write methods appropriate to each class.
- Use classes and methods to design a program.

## This assignment is based on the card game blackjack (also called 21). If you are unfamiliar with the game, instructions can be found [here](https://bicyclecards.com/how-to-play/blackjack/).
- The main objective is to have a hand of cards whose sum is as close to 21 as possible without going over. 
- This game will have two players, one dealer (computer) and one human.

## Reqirements
- Build a blackjack game using python between a player and a dealer. 
    - The deck is shuffled, and the dealer and player are dealt 2 cards.  
    - The dealer's play is dictated by the rules of the game, and the dealer goes first. The dealer "hits" (is dealt a card) until their hand total is 17 or greater, at which point they stay. The dealers cards are all visible to the player.
    - The player then chooses whether to hit (be dealt a card) or stay. The player may hit as many times as they want before staying, but if their hand totals over 21, they "bust" and lose. 
    - If you want to make the game work for multiple players, go for it.
    - The deck is a standard 52 card deck with 4 suits. Face cards are worth 10. The Ace card can be worth 1 or 11. 
        - SUITS = Hearts, Diamonds, Spades, Clubs
        - RANKS = A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
- Use classes. One way to think about classes is that they are the _nouns_ involved in what you are modeling, so Card, Deck, Player, Dealer, and Game are all nouns that could be classes.
- Give those classes methods. Think about the _actions_ that happen to or are caused by these different elements. These choices are subjective and hard, and there is no one right way.
- Use your classes and methods to execute the gameplay. It is always a great idea to sketch and/or comment this out first before writing code.

## Optional items once your game works
- Keep track of total wins over multiple games.
- Introduce betting.
- Try an automated non-dealer player and figure out how you dictate their behavior.
- Make your program [count cards](https://en.wikipedia.org/wiki/Card_counting). Note this gets you kicked out of casinos.
