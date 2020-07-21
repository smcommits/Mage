from graphics import*
from button import*
from cardGameLib import*
import random

#I am extremely sorry that you have to go through worst code of your life but I am still learning
# and I hope to reach there someday. Enjoy!

#creating a graphical window with width and height of 1280x720
win = GraphWin('Cards', 1280, 720, autoflush=False)
win.setCoords(0,0, 12,7) #setting the coordinates of the window from (0,0) to (12,7)


#displaying the instructions
instructions = Text(Point(5,6.5),'Please choose one card from below and keep it in your mind, the computer will display the the card you chose.')
instructions.setSize(14)
instructions.setStyle('bold')
instructions.draw(win)


#drawing and displaying 21 random cards on the screen
cards = drawCards(21)
displayCards(win, cards, 1.5,5.5,1.2,9,2)

#creating ready and quit button
quit = Button(win, Point(11,.5), 1, .3, 'Quit')
quit.activate()
ready = Button(win, Point(9.5, .5), 1, .3, 'Ready')
ready.activate()


while True:

    #asking for user input to check if the user wants to quit or is ready to play
    p = win.getMouse()
    if quit.clicked(p):
        win.close()
        break
    if ready.clicked(p):
        ready.deactivate()
        quit.deactivate()
        for i in cards:
            i.undraw() #undrawing the already displayed cards
            update(30)
            instructions.undraw()
        
        for i in range(3):
            
            instructions = Text(Point(5,6.5),'Please, select the deck which contains your card by clicking on the corresponding deck button. We will do this thrice! ')
            instructions.setSize(14)
            instructions.setStyle('bold')
            instructions.draw(win)

            
            #dividing and displayin the deck of 21 cards into three decks of seven cards each
            f = []
            m = []
            l = []

            for i in range(0, len(cards), 3):

                f.append(cards[i])
                m.append(cards[i+1])
                l.append(cards[i+2])
            
            
            displayCards(win, f, 1.5,5.5, 1.2,0,0) 
            displayCards(win, m, 1.5,3.5, 1.2,0,0) 
            displayCards(win, l, 1.5,1.5, 1.2,0,0) 


            #displaying text and buttons for corresponding decks 
            text = Text(Point(.5, 5.5), "Deck 1 --> ").draw(win)
            text1 = Text(Point(.5, 3.5), "Deck 2 --> ").draw(win)
            text2 = Text(Point(.5, 1.5), "Deck 3 --> ").draw(win)
            deck1 = Button(win,Point(10.5, 5.5), 1, .5, 'Deck 1')
            deck1.activate()
            deck2 = Button(win,Point(10.5, 3.5), 1, .5, 'Deck 2')
            deck2.activate()
            deck3 = Button(win,Point(10.5, 1.5), 1, .5, 'Deck 3')
            deck3.activate()
             
            
            while True:
            #infinite loop forcing user to click on either of the deck buttons
                p = win.getMouse()
                if deck1.clicked(p) or deck2.clicked(p) or deck3.clicked(p):
                    break
            
            #undrawing the cards and instructions already on display
            for each in [f,m,l]:
                for image in each:
                    image.undraw()
            
            instructions.undraw()
            
            group = [deck1, deck2, deck3, text, text1, text2] 
            for each in group:
                each.undraw()
            
            #with respect to whatever deck is selected, keeping the selected deck in the middle
            if deck1.clicked(p):
                f,m = m,f
            elif deck3.clicked(p):
                l, m = m, l


            deckSort = [f,m,l]

            cards = []

            for i in range(len(deckSort)):
                for x in range(len(deckSort[i])):
                    cards.append(deckSort[i][x])
        
        #displaying text for dramatic purposes :D
        ca = Text(Point(6,3.5), "And your card is!").draw(win)
        for i in range(100):
            ca.setSize(36)
            update(60)

        ca.undraw()
        
        #displaying users card
        yourCard = cards[10]
        yourCard.draw(win, Point(6,3.5))
        


        
        ready.setLabel('Reset')
        quit.activate()
        ready.activate()

        while True:

            p = win.getMouse()
            if quit.clicked(p):
                win.close()
                break
                    
            elif ready.clicked(p):
                ready.setLabel('Ready')
                yourCard.undraw()
                cards = drawCards(21)
                displayCards(win, cards, 1.5,5.5,1.2,9,2)
                instructions = Text(Point(5,6.5),'Please choose one card from below and keep it in your mind, the computer will display the the card you chose.')
                instructions.setSize(14)
                instructions.setStyle('bold')
                instructions.draw(win)
                break

