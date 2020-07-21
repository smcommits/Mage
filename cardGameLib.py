#cards
import os
from graphics import*
import random

"""This library is designed to facilitate the coding process for the Guess Game.
    It aims to provide encapsulation and provides classes and functions which are used
    to make the code for guess game more efficient and readable"""

class Cards:

    """A card is an object which can correspond to any of the 52 deck playing cards."""

 
    def __init__(self, rank, suit):

        """Creates a card from 52 deck playig card by taking 
        rank and suit as parameters, eg: Cards(1, 'c') will 
        create an Ace of Clubs"""

        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10

    def __str__(self):

        """Returns the name of card as string.
           Eg: If the rank of the card is 1 and the suit is 'c', this method
           will return a string = 'Ace of Clubs'"""

        ranks = [None, 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        rankStr = ranks[self.rank]

        if self.suit == 'c':
            suitStr = 'Clubs'
        elif self.suit == 'd':
            suitStr = 'Diamonds'
        elif self.suit == 'h':
            suitStr = 'Hearts'
        else:
            suitStr = 'Spades'

        return "{0} of {1}".format(rankStr, suitStr)

    def draw(self, win, center):
        """Draws the image of the card on a graphical window.
        The image will centered at the point center"""

        self.filename = os.getcwd() +'/Images/' + self.__str__() + ".png"
        self.cardImage = Image(center, self.filename)
        self.cardImage.draw(win)
    def getImage(self):
        return self.filename
    def undraw(self):
        """Undraws the image of the card from a graphical window"""
        self.cardImage.undraw()

def drawCards(n):
    """ This function returns provided number of random instances of the 
    'Cards' object in a list. To avoid duplication, all the possible unique
    instances are created and then a required number of instances are stored
    in a set and then finally returned as a list."""
    
    fullDeck = []
    cards = set()
    
    for i in ['c','d','s','h']:
        for x in range(1, 14):
            c = Cards(x, i)
            fullDeck.append(c)
    
    while len(cards) != 21:
        cards.add(random.choice(fullDeck))


    return list(cards)


            

def displayCards(window,cardList, initialX, initialY, incrementX, margin, decrementY):
    """This function display each card in a list on a graphic window.
    Staring from the X and Y position. Margin here signifies the limit of image display 
    on x axis, if x > margin, images will start to display in from the start of x axis 
    with some decremented value of Y"""
   
    x, y = initialX, initialY
    for i in cardList:
        i.draw(window, Point(x,y))
        update(20)
        x += incrementX
        if margin > 0 and x > margin:
            x = initialX
            y -= decrementY


