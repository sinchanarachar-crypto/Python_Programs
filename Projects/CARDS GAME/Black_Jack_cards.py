#Cards Module
#Basic Classes for a game with playing cards

class Card(object):
    """A Playing Card.. """
    RANKS  = ["A","2","3","4","5","6","7","8",
             "9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """A Hand of Playing Cards. """
    def __init__(self):
        self.cards = []

    def __str__ (self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) +"\t"

        else:
            rep ="<empty>"
        return rep
    
    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """A Deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Can't continue deal..Out of Cards!")

if __name__== "__main__":
    print("This is a module with classes for playing cards.")
    input("\n\nPress Enter Key to exit.")


#BlackJack
#From 1 to 7 players compete against a dealer

import cards, games

class BJ_Card(cards.Card):
    """A BlackJack Card. """
    ACE_VALUE= 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v>10:
                v=10
            else:
                v = None
            return v
        
    
class BJ_Deck(cards.Deck):
    """A BlackJack Deck."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank,suit))

class BJ_Hand(cards.Hand):
    """A BlackJack Hand"""
    def __init__(self,name):
        super(BJ_Hand,self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand,self).__str__()
        if self.total:
            rep += "("+ str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        #if a card in hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
            
        #add up card values, treat each ace as 1
        t=0
        for card in self.cards:
            t += card.value

        #determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        #if hand contins Ace and Total is low enough, treat ace as 11
        if contains_ace and t<=11:
            #add only 10 since we've aready added 1 for ace
            t += 10

        return t

    def is_busted(self):
        return self.total>21
    
class BJ_Player(BJ_Hand):
    """A BlackJack Player."""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ",do you want a hit? (Y/N)")
        return response == "y"
    
    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name,"loses")

    def win(self):
        print(self.name,"wins.")

    def push(self):
        print(self.name,"pushes.")

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
    """A BlackJack Game. """
    def __init__(self,names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp=[]
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    
    def __additional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def player(self):
        #Deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  #hides dealer first card
        for player in self.players:
            print(player)
        print(self.dealer)

        #Deal additional cards to players
        for player in self.players:
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                #everyone still playing winns
                for player in self.still_playing:
                    player.win()

            else:
                #compare each player still playing t dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        #Remove everyone's card
        for player in self.players:
            player.clear()
        self.dealer.clear()


#MAIN FUNCTION
def main():
    print("\t\tWELCOME TO BLACKJACK\n")

    names=[]
    number = games.ask_number("How many players? (1 - 7)", low=1,high=8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again=games.ask_yes_no("\nDo you want to play again?: ")

main()
input("\n\nPress the Enter Key to exit.")