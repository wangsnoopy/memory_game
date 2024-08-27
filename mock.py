# You are tasked with designing a memory card game system. In this game, cards are laid face down. You are the only player in this game, 
# and you will score by how many rounds you use to complete the game.
# You need to simulate the game, monitor game state and return how many rounds the player takes to complete the game

# part 1. player randomly pick 2 cards every round until the game end
# part 2. player picks a pair that they never picked before otherwise part 1
# part 3. player picks a pair if they know it's a match otherwise part 2

#values = ["A", "B", "C", "D"]
# game = MemoryGame(values)
import random
class Card:
    def __init__(self, value):
        self.value = value
        self.flip = False

class Player:
    def __init__(self, deck):
        self.round = 0
        self.deck = deck

    
    def flip_two_cards(self):
        pick1 = self.pick_a_card()
        pick2 = self.pick_a_card()
        # get the same card
        while pick1 == pick2:
            pick1 = self.pick_a_card()
            pick2 = self.pick_a_card()
        
        # print(pick1.value, pick2.value)
        # get the pair, update
        if pick1.value == pick2.value:
            pick1.flip = True
            pick2.flip = True
        # print([v.value for v in self.deck])

    def all_cards_flip(self):
        return all([card.flip for card in self.deck])

    def pick_a_card(self):
        pick_card = random.choice(self.deck)
        return pick_card

        

class Game:
    def __init__(self, values: list):
        self.deck = []
        for value in values:
            self.deck.append(Card(value))
            self.deck.append(Card(value))
        random.shuffle(self.deck)
        self.player = Player(self.deck)
    
    def play_game(self):
        round = self.player.round
        while not self.player.all_cards_flip():
            self.player.flip_two_cards()
            round += 1
        return round
    


# player = Player(['A','B','C'])
# print([v.value for v in player.deck])
# player.flip_two_cards()
game = Game(['A','B','C'])
print(game.play_game())