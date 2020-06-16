import random
class Card:                                             #Holds structure of cards
    def __init__(self,suit,type,value):
        self.suit=suit
        self.type=type
        self.value=value

    def show(self):
        print('{} of {}'.format(self.type,self.suit))
class Deck:
    def __init__(self):
        self.cards=[]
        self.build()
        self.shuffle()
    
    def build(self):                                       #To fill the deck with 52 cards
        for s in ['Hearts','Spades','Diamonds','Clubs']:
            type=2
            for x in range(2,11):
                self.cards.append(Card(s,type,x))
                type+=1
            self.cards.append(Card(s,"Jack",11))
            self.cards.append(Card(s,"Queen",12))
            self.cards.append(Card(s,"King",13))
            self.cards.append(Card(s,"Ace",14))
    
    def show_cards(self):
        for v in self.cards:
            v.show()
    
    def draw(self):                                          #To draw cards from deck
        return self.cards.pop()
    def shuffle(self):                                       #To shuffle the whole deck
        random.shuffle(self.cards)


        
class Player:
    def __init__(self):
        self.cards=[]
    def draw_card(self,deck):
        self.cards.append(deck.draw())
    
class Base:
    def __init__(self,player,computer,deck):
        self.player=player
        self.computer=computer
        self.deck=deck
        #self.deck.shuffle()

    def Game(self):
        print()
        print("Card World!")
        print("Player card shown first.")
        player.draw_card(self.deck)
        computer.draw_card(self.deck)
        #self.deck.shuffle()

        if self.player.cards[0].value > self.computer.cards[0].value :
            print(str(self.player.cards[0].type) +" VS "+str(self.computer.cards[0].type))
            print("CONGRATULATIONS  YOU WINS!!")
        elif self.player.cards[0].value < self.computer.cards[0].value:
            print(str(self.player.cards[0].type) +" VS " + str(self.computer.cards[0].type))
            print("BETTER LUCK NEXT TIME.")
        else:
            print(str(self.player.cards[0].type) +" VS "+ str(self.computer.cards[0].type))
            print("ITS A TIE")


#ybase=Base(player,computer,deck)
ch='y'
while (ch!='n'):    
    deck=Deck()
    player=Player()
    computer=Player()
    base=Base(player,computer,deck)
    base.Game()
    print("Do you want to play more? y or n")
    ch=input()
