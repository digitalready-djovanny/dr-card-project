import random
from card import Card


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

class Computer():
    def __init__ (self,computer,hand=[0],money=0):
        self.computer = computer  
        self.hand = hand
        self.money = money
Computer = Computer("Computer")

def new_card():
    card = deck.pop()
    return card

def sum_Player():
    sum = 0
    for card in Bob.hand:
        sum+= card.value
    return sum



def black_jack():
    Bob.hand.append(new_card())
    print(f"{Bob.hand}, {sum_Player()}, You have {Bob.money} dollars worth of chips.")

    if player_input() == "hit":
        Bob.hand.append(new_card())
        print(f"{Bob.hand}, {sum_Player()}, You have {Bob.money} dollars worth of chips.")

    else:
        return sum_Player()


if __name__ == "__main__":
    black_jack()


'''def black_jack():
    
    #first card that the player is given
    player_hand = 0 
    deck = Card.new_deck()
    card = deck.pop()
    player_hand += card.value
    computer_hand = random.randint(2,21)
    print(f' you drew: {card}, your hand is {player_hand}')
    
    #player starts playing
    while not player_hand >21:
        
        if player_input()== "hit":
            card=deck.pop()
            player_hand += card.value
            print(f'you drew {card}, your hand is {player_hand}')


        elif player_input()== "stop":
            if player_hand > computer_hand:
                print("you win, we will need your right eye")
            elif player_hand == computer_hand:
                print("tie, we will be taking your left foot")
            else:
                print("you lose, we will be taking your wife and children, thank you come again")
    
    if player_hand ==21:
            print("you win, you only need to sell 1 of your kidneys now")
    if player_hand >21:
            print("bust, you lose, we taking 2 generations of your children, your left kidney , your wife, and your 2nd cousin from your mother's side")

    '''

'''def player_input():
    x = ""
    while x!= "hit" and x!= "stop":
        x = input("Do you want to hit or stop, dont matter u going to lose anyway stooooooobid: ")
    return x
         
         '''
        
            
            

    

'''def hit():
    deck = Card.new_deck()
    draw_card = deck.pop()
    return (draw_card.suit, draw_card.value)


black_jack()
'''





