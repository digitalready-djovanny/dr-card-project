import random
from card import Card

stop = 0

deck = Card.new_deck()

def player_input():
    x = ""
    while x!= "hit" and x!= "stop":
        x = input("Do you want to hit or stop, dont matter u going to lose anyway stooooooobid: ")
    return x
         
class Player():
    def __init__ (self,name,hand=[],money=0):
        self.name = name
        self.hand = hand
        self.money = money

Bob = Player("Bob", [], 100 )

computer = Player("computer", [], 100)

def print_cards(cards, hidden):
         
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()
#whenever new_card is called, print_cards will be called and  a card will be printed. Too bad the computer doesn't get that privilege.
def new_card():
    card = deck.pop()
    print_cards([card], hidden=False)
    return card

def sum_Player():
    total = 0
    for card in Bob.hand:
        total += card.value
    return total

def sum_computer():
    total = 0
    for card in computer.hand:
        total += card.value
    return total


def check_win():
    if sum_Player() >21:
        return print("You such dumb stubid u bust")
 
def computer_hand():
    while sum_computer() < 21:

        computer.hand.append(deck.pop())
        
    computer.hand.pop()
    return sum_computer()

def black_jack():
        Bob.hand.append(new_card())
        Bob.hand.append(new_card())
        if sum_Player() > 21:
            return print(f"Your hand is {Bob.hand}, {sum_Player()}, You have {Bob.money} dollars worth of chips.")

        print(f"You bust, {Bob.hand}, {sum_Player()}, You have {Bob.money} dollars worth of chips.")


        while player_input() != "stop":

            Bob.hand.append(new_card())
            print(f"{Bob.hand}, {sum_Player()}, You have {Bob.money} dollars worth of chips.")
            if sum_Player() > 21:
                check_win()
                break
        
        if sum_Player() <21 or sum_Player() == 21:

            computer_hand()
            print(f"The dealer's cards are {computer.hand} and the value of his hand is {sum_computer()}.")


            if sum_Player() < sum_computer():
                print("You lose")
            else:
                print("You win")
    
                
        
            
    

if __name__ == "__main__":

    black_jack()












