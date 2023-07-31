class Hand:

    def __init__(self, card=[], value = 0, aces = 0):
        self.card=card
        self.value=value
        self.aces=aces

    def add_card(self,card):
        self.card.append(card)
        self.value += value [card.rank]

    def adjust_for_ace(self):
        pass
