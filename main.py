from card import Card 
from deck import Deck 
from hand import Hand

card1 = Card("Ace", "Spades")
print(card1)
print(card1.rank)
print(card1.suit)
print(card1.get_rank_name())

# h = Hand()
# h.add_card(Card("Ten", "Hearts"))
# h.add_card(Card("Jack", "Clubs"))
# print(h)

# d = Deck()
# h = Hand()
# h.add_cards_from_deck(d, 5)
# print(h)

# d = Deck()
# h = Hand()
# h.add_cards_from_deck(d, 10)
# print(h)
# print(h.get_rank_dictionary())

h = Hand()
h.add_card(Card("Ten", "Hearts"))
h.add_card(Card("Jack", "Clubs"))
h.add_card(Card("Ten", "Spades"))
h.add_card(Card("Ace", "Clubs"))
h.add_card(Card("Ten", "Hearts"))
# s = h.check_for_three_of_a_kind()
# print(h)
# print(s)  #should print True
# print("-------")





