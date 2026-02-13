# blackjack.py
# Blackjack game using cards module

import cards

class BJ_Card(cards.Card):
    """A BlackJack Card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            return v
        return None


class BJ_Deck(cards.Deck):
    """A BlackJack Deck."""
    def populate(self):
        self.cards = []
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """A BlackJack Hand"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total is not None:
            rep += "(" + str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        # if a card in hand has value of None, then total is None
        for card in self.cards:
            if card.value is None:
                return None
            
        # add up card values, treat each ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an Ace
        contains_ace = any(card.rank == "A" for card in self.cards)

        # if hand contains Ace and total is low enough, treat ace as 11
        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """A BlackJack Player."""
    def is_hitting(self):
        response = input("\n" + self.name + ", do you want a hit? (Y/N): ").lower()
        return response == "y"
    
    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")


class BJ_Dealer(BJ_Hand):
    """A BlackJack Dealer"""
    def is_hitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """A BlackJack Game."""
    def __init__(self, names):
        self.players = [BJ_Player(name) for name in names]
        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        return [player for player in self.players if not player.is_busted()]
    
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # Deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # hides dealer first card

        for player in self.players:
            print(player)
        print(self.dealer)

        # Deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        # Reveal dealer's first card
        self.dealer.flip_first_card()
        print(self.dealer)

        # Dealer takes additional cards
        self.__additional_cards(self.dealer)

        if self.dealer.is_busted():
            for player in self.still_playing:
                player.win()
        else:
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()

        # Remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()


# MAIN FUNCTION
def main():
    print("\t\tWELCOME TO BLACKJACK\n")

    number = int(input("How many players? (1 - 7): "))
    names = [input("Enter player name: ") for _ in range(number)]
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = input("\nDo you want to play again? (Y/N): ").lower()

if __name__ == "__main__":
    main()
    input("\n\nPress the Enter Key to exit.")

