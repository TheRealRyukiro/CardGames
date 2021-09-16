"""
    This class controls the creation of a card.
    
    Numbers are as followed:
    0 = No Number
    1 = Ace
    2-10 is self explainatory
    11 = Jack
    12 = Queen
    13 = King
    14 = Joker

    Suits are as followed(Alphabetical order):
    0 = No Suit
    1 = Clubs
    2 = Diamonds
    3 = Hearts
    4 = Spades
"""
import random as rand

class Card:
    def __init__(self, Suit = 0, Number = 0):
        self.Suit = Suit
        self.Number = Number
        self.Image = None # Not implemented yet... 
    
    def randomizeCard(self, Cards): #Takes Self param as well as Cards. Cards can either be a single card or a deck of cards
        # a forever loop to keep randomizing the number / suit combo until one isn't in the current Cards
        while True:
            randNum = rand.randint()
            randSuit = rand.randint()
            okToUse = True
            if(isinstance(Cards, Card)):
                if(Cards.Suit == randSuit and Cards.Number == randNum):
                    okToUse = False
                    break
                else:
                    self.Suit = randSuit
                    self.Number = randNum
            elif(isinstance(Cards, Deck)):
                for Card in Cards:
                    if(Card.Suit == randSuit and Card.Number == randNum):
                        okToUse = False
                        break
                if (okToUse):
                    self.Suit = randSuit
                    self.Number = randNum
                    break
    def isSameCard(self, cardToCompare):
        if(self.Suit == cardToCompare.Suit and self.Number == cardToCompare.Number): return True
        else: return False
    def isJoker(self):
        if(self.Suit == 0 and self.Number == 14): return True
        else: return False
    def displaySuit(self):
        if(self.Suit == 1): return "Clubs"
        elif(self.Suit == 2): return "Diamonds"
        elif(self.Suit == 3): return "Hearts"
        elif(self.Suit == 4): return "Spades"
        elif(self.isJoker()): return "Joker"
        elif(self.Suit == 0): return "No Suit"
        else:
            raise TypeError(f"Suit number is outside the range 0-4 & is not a Joker.\nSuit Number given: {self.Suit}")
    def displayNumber(self):
        if(self.Number == 1): return "Ace"
        elif(self.Number > 1 and self.Number < 11): return str(self.Number)
        elif(self.Number == 11): return "Jack"
        elif(self.Number == 12): return "Queen"
        elif(self.Number == 13): return "King"
        elif(self.isJoker()): return "Joker"
        elif(self.Number == 0): return "No Number"
        else: 
            raise TypeError(f"Number is outside the range 0-13 & is not a Joker.\nNumber given: {self.Number}")
    def displayCard(self):
        return f"{self.displayNumber()} of {self.displaySuit()}"

class Deck:
    def __init__(self, deckOfCards = []):
        self.deckOfCards = deckOfCards
        
    def createDeck(self, howManyDecks = 1):
        deckOfCards = []
        while howManyDecks > 0:
            for suit in range(4):
                for num in range(13):
                    deckOfCards.append(Card(suit+1,num+1))
            self.deckOfCards = deckOfCards
            howManyDecks -= 1
    def displayDeck(self):
        deckString = ""
        for card in self.deckOfCards:
            deckString += f" - {card.displayCard()}\n"
        return deckString
    def shuffleDeck(self): return rand.shuffle(self.deckOfCards)

class Hand:
    def __init__(self, Cards = []):
        self.Cards = Cards
    def drawCard(self):
        pass
    def cardScore(self):
        score1 = 0
        score2 = 0
        for card in self.Cards:
            if(card.Number == 1):
                score1 += 11
                score2 += 1
            else:
                score1 += card.Number
                score2 += card.Number
        if(score1 > 21):
            return score2
        elif(score1 <= 21):
            return score1

class DealerHand(Hand):
    def __init__(self, Cards = [], dealerStand = 17):
        super().__init__(Cards)
        self.dealerStand = dealerStand

class PlayerHand(Hand):
    def __init__(self, Cards = []):
        super().__init__(Cards)
    def displayHand(self):
        hand = ""
        for card in self.Cards:
            hand += f" - {card.displayCard()}\n"
        return hand