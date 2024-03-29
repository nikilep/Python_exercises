# File:         poker
# Author:       Niki Leppänen
# Description:  Game of poker with working best hand indicator and 4 players

from Exercise_work.player import Player
from Exercise_work.deck import Deck
from Exercise_work.cards import Card
from Exercise_work import exercise_work


def game():

    # sorting function
    def highest(list):
        for step in range(1, len(list)):
            key = list[step]
            j = step - 1

            while j >= 0 and key.get_value() > list[j].get_value():
                list[j + 1] = list[j]
                j = j - 1

            list[j + 1] = key

    # finds player with best hand/score
    def winner(list):
        for step in range(1, len(list)):
            key = list[step]
            j = step - 1

            while j >= 0 and key.get_score() > list[j].get_score():
                list[j + 1] = list[j]
                j = j - 1

            list[j + 1] = key

    # Scoring of hands:
    # Straight flush = 120 - 134
    # Four of a kind = 105 - 119
    # Full house = 90 - 104
    # Flush = 75 - 89
    # Straight = 60 - 74
    # Three of a kind = 45 - 59
    # Two pair = 30 - 44
    # Pair = 15 - 29
    # High Card = 2 - 14

    # Checks for pair
    def check_pair(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if len(hand) < 2:
            return 0
        elif hand[0].get_value() == hand[1].get_value():
            score = 15 + hand[0].get_value()

            return score
        else:
            return check_pair(hand[1:])

    # Checks for three of a kind
    def check_triple(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if len(hand) < 3:
            return 0
        elif hand[0].get_value() == hand[1].get_value() == hand[2].get_value():
            score = 45 + hand[0].get_value()

            return score
        else:
            return check_triple(hand[1:])

    # Checks for fours of a kind
    def check_four(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if len(hand) < 4:
            return 0
        elif hand[0].get_value() == hand[1].get_value() == hand[2].get_value() == hand[3].get_value():
            score = 105 + hand[0].get_value()

            return score
        else:
            return check_four(hand[1:])

    # Checks for two pairs
    def check_two_pairs(hand):
        # puts cards in order from highest to lowest value
        highest(hand)
        pairs = []

        # adds pairs to pairs list
        if hand[0].get_value() == hand[1].get_value() and hand[2].get_value() == hand[3].get_value():
            pairs.append(hand[0].get_value())
            pairs.append(hand[1].get_value())
            pairs.append(hand[2].get_value())
            pairs.append(hand[3].get_value())

        elif hand[0].get_value() == hand[1].get_value() and hand[3].get_value() == hand[4].get_value():
            pairs.append(hand[0].get_value())
            pairs.append(hand[1].get_value())
            pairs.append(hand[3].get_value())
            pairs.append(hand[4].get_value())

        elif hand[1].get_value() == hand[2].get_value() and hand[3].get_value() == hand[4].get_value():
            pairs.append(hand[1].get_value())
            pairs.append(hand[2].get_value())
            pairs.append(hand[3].get_value())
            pairs.append(hand[4].get_value())

        # checks if there is two pairs in pairs list and gives score depending on both pair values
        if len(pairs) == 4:
            score = 0
            for i in pairs:
                score += i

            score = score / 4 + 30

            return score

        else:
            return 0

    # Checks for straight
    def check_straight(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if (hand[0].get_value() - 1 == hand[1].get_value() and hand[1].get_value() - 1 == hand[2].get_value() and
                hand[2].get_value() - 1 == hand[3].get_value() and hand[3].get_value() - 1 == hand[4].get_value()):

            score = 60 + hand[0].get_value()

            return score

        else:
            return 0

    # checks for flush
    def check_flush(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        if (hand[0].get_suit() == hand[1].get_suit() and hand[1].get_suit() == hand[2].get_suit() and
                hand[2].get_suit() == hand[3].get_suit() and hand[3].get_suit() == hand[4].get_suit()):

            score = 75 + hand[0].get_value()

            return score

        else:
            return 0

    # Checks for straight flush
    def check_straight_flush(hand):

        if check_flush(hand) > 75 and check_straight(hand) > 60:
            # puts cards in order from highest to lowest value
            highest(hand)

            score = 120 + hand[0].get_value()

            return score

        else:
            return 0

    # Checks for full house
    def check_full_house(hand):
        # puts cards in order from highest to lowest value
        highest(hand)

        score = 0

        # checks for possible ways to get full house with five cards
        if (hand[0].get_value() == hand[1].get_value()
                and hand[2].get_value() == hand[3].get_value() == hand[4].get_value()):

            for i in hand:
                score += i.get_value()

            score /= 5
            score += 90

        elif (hand[0].get_value() == hand[1].get_value() == hand[2].get_value()
              and hand[3].get_value() == hand[4].get_value()):

            for i in hand:
                score += i.get_value()

            score /= 5
            score += 90

        else:
            return 0

    # function to check what is the best possible hand that player can get from his five cards and returns the score
    def check_best_hand(hand):

        score = 0

        if check_straight_flush(hand) != 0:
            score = check_straight_flush(hand)

        elif check_four(hand) != 0 and score == 0:
            score = check_four(hand)

        elif check_full_house(hand) != 0 and score == 0:
            score = check_full_house(hand)

        elif check_flush(hand) != 0 and score == 0:
            score = check_flush(hand)

        elif check_straight(hand) != 0 and score == 0:
            score = check_straight(hand)

        elif check_triple(hand) != 0 and score == 0:
            score = check_triple(hand)

        elif check_two_pairs(hand) != 0 and score == 0:
            score = check_two_pairs(hand)

        elif check_pair(hand) != 0 and score == 0:
            score = check_pair(hand)

        else:
            highest(hand)
            score = hand[0].get_value()

        print()
        print(score)

        return score

    # Builds deck and creates all the players
    deck = Deck()
    player = exercise_work.player
    computer1 = Player("C1")
    computer2 = Player("C2")
    computer3 = Player("C3")

    players = [computer1, computer2, computer3, player]

    # create hands for all the players
    comp_c1 = []
    comp_c2 = []
    comp_c3 = []
    player_c = []
    players_cards = [comp_c1, comp_c2, comp_c3, player_c]

    # shuffles the deck
    deck.shuffle_deck()

    # Gives everyone 5 cards at the beginning
    for n in range(5):
        for i in players_cards:
            i.append(deck.draw_card())

    print()

    # prints player name and his cards
    for i in players_cards:
        print()
        pos = players_cards.index(i)
        print(players[pos].get_name(), ":")
        for c in i:
            c.show_card()

    print()

    # checks every players best hand and gives them score from it
    computer1.set_score(check_best_hand(comp_c1))
    computer2.set_score(check_best_hand(comp_c2))
    computer3.set_score(check_best_hand(comp_c3))
    player.set_score(check_best_hand(player_c))

    # tells who is the winner
    winner(players)

    print("Winner is ", players[0].get_name())


