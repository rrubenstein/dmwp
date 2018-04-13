import matplotlib.pyplot as plt
from sympy import FiniteSet
import random
import time

def draw_venn(sets):

    plt.show()

def make_set(lenth, range):
    s = []
    for i in range(0, lenth+1):
        x = random.randint(0, range)
        s.append(x)

def trial(num, min, max, prob):
    outcome = []
    expec = 0.0
    for i in range(0, num):
        x = random.randint(min, max)
        outcome.append(x)
    for i in range(min, max + 1):
        expec += float(i*prob)
    mean = float(sum(outcome))/float(len(outcome))
    final = [expec, mean, num]
    return final
def test1():
    z = float(1)/float(6)
    t1 = trial(100, 1, 6, z)
    t2 = trial(1000, 1, 6, z)
    t3 = trial(10000, 1, 6, z)
    t4 = trial(100000, 1, 6, z)
    t5 = trial(500000, 1, 6, z)
    tests = [t1, t2, t3, t4, t5]
    print('Expected value: {0}'.format(t1[0]))
    for test in range(0, len(tests)):
        print('Trials: {0} Trial average: {1}'.format(tests[test][2], tests[test][1]))

def money_game():
    start = raw_input('Starting amount: ')
    start = float(int(start))
    a = 0
    while start > 0.0:
        r = random.random()
        if r >= 0.5:
            x = 'Heads!'
            start += 1.0
        elif r <= 0.51:
            x = 'Tails!'
            start -= 1.5
        print('{0} Current amount: {1}'.format(x, start))
        a += 1
        time.sleep(0.3)
    print('Game over! Current amount: {0}. Coin tosses: {1}'.format(start, a))

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def make_deck():
    deck = {}
    counter = 1
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    for suit in range(0, 4):
        for rank in range(0, 13):
            deck[counter] = Card(suits[suit], ranks[rank])
            counter += 1
    return deck

def shuffle():
    ids = []
    for x in range(1, 53):
        ids.append(x)
    random.shuffle(ids)
    deck = make_deck()
    for x in ids:
        print('{0} of {1}'.format(deck[x].rank, deck[x].suit))
