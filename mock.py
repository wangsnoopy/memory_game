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
        self.flipped = False

class Player:
    def __init__(self, deck):
        self.round = 0
        self.deck = deck

    
    def flip_two_cards(self):
        # random pick two el from the list
        first_card, second_card = self.picked_two_card()
        
        # get the pair, update
        if first_card.value == second_card.value:
            first_card.flipped = True
            second_card.flipped = True
        # print([v.value for v in self.deck])

    def picked_two_card(self):
        picked_two = random.sample(self.deck, 2)
        return picked_two

        

class Game:
    def __init__(self, values: list):
        self.deck = []
        for value in values:
            self.deck.append(Card(value))
            self.deck.append(Card(value))
        random.shuffle(self.deck)
        self.player = Player(self.deck)
    
    def play_game(self):
        while not self.all_cards_flipped():
            self.player.flip_two_cards()
            self.player.round += 1
        return self.player.round

    def all_cards_flipped(self):
        return all([card.flipped for card in self.deck])
    


# player = Player(['A','B','C'])
# print([v.value for v in player.deck])
# player.flip_two_cards()
game = Game(['A','B','C'])
print(game.play_game())