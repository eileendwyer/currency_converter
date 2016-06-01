## see Drinks EX in online Lesson for Magic Methods

class Hand:
    def __init__(self, card_one, card_two):
        self.card_one = card_one
        self.card_two = card_two
# want to compare values of both cards
# making assumption the cards have value
    def hand_value(self):
        return self.card_one.value() + self.card_two.value()

    def __iter__(self):
        return self.cards.__iter__()  ## since not interable

    def __gt__(self, other):
        return self.hand_value() > other.hand_value

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
# these lines below - self, and other have to MAP UP - align L, R - positional args
## maintain L, R mentality when workig with binary operators
    def __add__(self, other):  # will add the two cards into a hand
        return Hand(self, other)  ##GO TO Line 30

    def __str__(self):
        return "{} of {}'s".format(self.rank, self.suit)  # go to line 46, 47

card_one = Card("Diamond", "A:)")
print(card_one)
#card_one.rank = "j"
#print(card_one.suit)
#card_two = Card("Club", 7)
"""
    @ property
    def value(self):  # if value not in rank []
                        # raise ValueError
        if self.rank == "A":
            return []
        elif self.rank in ["Q", "K", "J"]:
            return 10
        return self.rank

    @value.setter
    def value(self, value):
        if type(value) == str
            if value.upper()() not in [ A J ....]
                raise exception
        self.rank = value.upper()

"""

# hand_one = card_one + card_two # gives a unit - EX of overloading the "ADD OP"
#print(hand_one.hand_value
# card_three = Card("Diamond", 2))
# card_four = Card("Spade", "J")

# print(hand_one > hand_two)
#for card in hand_one:
#    print(card)  - # can interate here since we did the (+) op to join in hand


"""
In [1]: class test(object):
    def __init__(self):
        self.pants = 'pants'
    @property
    def p(self):
        return self.pants
    @p.setter
    def p(self, value):
        self.pants = value * 2
   ....:
In [2]: t = test()
In [3]: t.p
Out[3]: 'pants'
In [4]: t.p = 10
In [5]: t.p
Out[5]: 20
"""