import random

suits = ('\u2665', '\u2666', '\u2660', '\u2663') * 2
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 20, 'Three': 100, 'Four': 5, 'Five': 5, 'Six': 5, 'Seven': 5, 'Eight': 10, 'Nine': 10, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 20, 'Joker': 50}
joker_suits = ('\u2665', '\u2666', '\u2660', '\u2663')
joker_rank = 'Joker'


class Card:  # Card class

    def __init__(self, suit, rank):  # Card constructor
        self.suit = suit
        self.rank = rank
        self.value = values

    def __str__(self):  # Card string representation
        return self.rank + self.suit

    def __repr__(self):  # Card representation
        return f'{self.rank}{self.suit}'

    def __lt__(self, other):  # Card less than
        if self.rank[:3] == other.rank[:3]:
            return self.suit < other.suit
        else:
            return self.rank < other.rank

    def __eq__(self, other):  # Card equal
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return NotImplemented

    def __ne__(self, other):  # Card not equal
        return not self.__eq__(other)


class Deck:

    def __init__(self):  # Deck constructor

        self.deck = []  # start with an empty list

        for suit in suits:  # build Card objects and add them to the list
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)
        for joker_suit in joker_suits:
            created_jokers_card = Card(joker_suit, joker_rank)
            self.deck.append(created_jokers_card)

    def __str__(self):  # Deck string representation

        deck_comp = ""  # start with an empty string

        for card in self.deck:  # add each Card object's print string
            deck_comp += '\n' + card.__str__()  # add a space between each Card object's print string
        return "The deck has: " + deck_comp  # return the Deck string representation

    def shuffle(self):  # shuffle the deck

        random.shuffle(self.deck)

    def deal_one(self):  # deal one card from the deck

        return self.deck.pop()


class Hand:

    def __init__(self):  # Hand constructor
        self.all_cards = []  # start with an empty list
        self.value = 0  # start with zero value

    def __str__(self):  # Hand string representation

        hand_comp = ""  # start with an empty string

        for card in self.all_cards:  # add each Card object's print string
            self.all_cards += card.__str__()
        return "The Hand have: " + hand_comp

    def if_player_have_wild_card(self, cards_on_table):  # check if player have wild card, and ask where to put it

        for card in reversed(self.all_cards):
            if card.rank[:3] == 'Jok' or card.rank[:3] == 'Two':
                # ask if player want to put wild card on table
                x = input(f'Do you want to put {card} on table? Where? if nowhere (N/n): ')
                try:
                    match x:  # match x with cases
                        case '0':
                            self.all_cards.remove(card)  # remove card from hand
                            cards_on_table[0].append(card)  # add wild card to table
                            print(cards_on_table[0])  # print table[0]
                        case '1':
                            self.all_cards.remove(card)
                            cards_on_table[1].append(card)
                            print(cards_on_table[1])
                        case '2':
                            self.all_cards.remove(card)
                            cards_on_table[2].append(card)
                            print(cards_on_table[2])
                        case '3':
                            self.all_cards.remove(card)
                            cards_on_table[3].append(card)
                            print(cards_on_table[3])
                        case '4':
                            self.all_cards.remove(card)
                            cards_on_table[4].append(card)
                            print(cards_on_table[4])
                        case '5':
                            self.all_cards.remove(card)
                            cards_on_table[5].append(card)
                            print(cards_on_table[5])
                        case '6':
                            self.all_cards.remove(card)
                            cards_on_table[6].append(card)
                            print(cards_on_table[6])
                        case '7':
                            self.all_cards.remove(card)
                            cards_on_table[7].append(card)
                            print(cards_on_table[7])
                        case '8':
                            self.all_cards.remove(card)
                            cards_on_table[8].append(card)
                            print(cards_on_table[8])
                        case '9':
                            self.all_cards.remove(card)
                            cards_on_table[9].append(card)
                            print(cards_on_table[9])
                        case '10':
                            self.all_cards.remove(card)
                            cards_on_table[10].append(card)
                            print(cards_on_table[10])
                        case '11':
                            self.all_cards.remove(card)
                            cards_on_table[10].append(card)
                            print(cards_on_table[11])
                        case 'N':  #
                            pass  # if player don't want to put wild card on table
                        case 'n':  #
                            pass
                        case _:  # if x doesn't match any case
                            print('Wrong input')
                            self.if_player_have_wild_card(cards_on_table)  # repeat function
                            break
                except IndexError:
                    pass

    def calculate_value_of_hand(self):  # calculate value of hand

        self.value = 0  # start with zero value

        for card in self.all_cards:  # add each Card object's value
            # if player have three of clubs or three of spades in hand we must subtract 100 points.
            # it is like that because black three don't have any value, only red are for 100 points.
            if card.rank == 'Three' and card.suit == '\u2663' or card.rank == 'Three' and card.suit == '\u2660':
                self.value -= 100  # subtract 100 from value
            self.value += card.value[card.rank]

        return self.value

    def add_card(self, card):  # add card to hand
        self.all_cards.append(card)

    def add_cards(self, *args):  # add cards to hand
        self.all_cards.extend(*args)

    def remove_one(self, position):  # remove card from hand ( with position of card )

        with_one_card = self.all_cards.pop(position)
        return with_one_card

    def remove_cards(self, card):  # similar to remove_one but with card object
        self.all_cards.remove(card)

    def remove_few(self, list_of_cards, cards_to_remove):  # remove few cards from hand
        try:
            new_list = [cards for cards in list_of_cards if cards not in cards_to_remove]
            self.all_cards = new_list
            return self.all_cards
        except TypeError:
            pass

    def if_player_have_2cards_in_hand_and_wild_card(self, player):
        # check if player have 2 same cards in hand and wild card

        for card in reversed(self.all_cards):

            try:
                if card.rank[:3] == 'Jok' or card.rank[:3] == 'Two':
                    if self.all_cards[0].rank[:3] == self.all_cards[1].rank[:3]:
                        print(f'{player} you have {self.all_cards[0]}, {self.all_cards[1]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[0], self.all_cards[1], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[1].rank[:3] == self.all_cards[2].rank[:3]:
                        print(f'{player} you have {self.all_cards[1]}, {self.all_cards[2]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[1], self.all_cards[2], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[2].rank[:3] == self.all_cards[3].rank[:3]:
                        print(f'{player} you have {self.all_cards[2]}, {self.all_cards[3]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[2], self.all_cards[3], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[3].rank[:3] == self.all_cards[4].rank[:3]:
                        print(f'{player} you have {self.all_cards[3]}, {self.all_cards[4]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[3], self.all_cards[4], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[4].rank[:3] == self.all_cards[5].rank[:3]:
                        print(f'{player} you have {self.all_cards[4]}, {self.all_cards[5]} in hand and wild {card}')
                        put_on_table3(player, self.all_cards[4], self.all_cards[5], card)
                        answer = put_on_table3(player, self.all_cards[4], self.all_cards[5], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[5].rank[:3] == self.all_cards[6].rank[:3]:
                        print(f'{player} you have {self.all_cards[5]}, {self.all_cards[6]} in hand and wild {card}')
                        put_on_table3(player, self.all_cards[5], self.all_cards[6], card)
                        answer = put_on_table3(player, self.all_cards[5], self.all_cards[6], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[6].rank[:3] == self.all_cards[7].rank[:3]:
                        print(f'{player} you have {self.all_cards[6]}, {self.all_cards[7]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[6], self.all_cards[7], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[7].rank[:3] == self.all_cards[8].rank[:3]:
                        print(f'{player} you have {self.all_cards[7]}, {self.all_cards[8]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[7], self.all_cards[8], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[8].rank[:3] == self.all_cards[9].rank[:3]:
                        print(f'{player} you have {self.all_cards[8]}, {self.all_cards[9]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[8], self.all_cards[9], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[9].rank[:3] == self.all_cards[10].rank[:3]:
                        print(f'{player} you have {self.all_cards[9]}, {self.all_cards[10]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[9], self.all_cards[10], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[10].rank[:3] == self.all_cards[11].rank[:3]:
                        print(f'{player} you have {self.all_cards[10]}, {self.all_cards[11]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[10], self.all_cards[11], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[11].rank[:3] == self.all_cards[12].rank[:3]:
                        print(f'{player} you have {self.all_cards[11]}, {self.all_cards[12]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[11], self.all_cards[12], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
                    elif self.all_cards[12].rank[:3] == self.all_cards[13].rank[:3]:
                        print(f'{player} you have {self.all_cards[12]}, {self.all_cards[13]} in hand and wild {card}')
                        answer = put_on_table3(player, self.all_cards[12], self.all_cards[13], card)
                        if answer is None:
                            pass
                        else:
                            player.remove_few(player_one.all_cards, answer)
                            player_one_table.add_cards(answer)
                            print(player_one_table)
                            continue
            except IndexError:
                pass

    def sort_cards(self):  # sort cards in hand
        return sorted(self.all_cards)


class Player(Hand):  # Player class

    def __init__(self, player):  # Player constructor
        super().__init__()  # inherit from Hand class
        self.name = input(f"{player}, please enter your nickname: ")  # ask for player's nickname

    def __str__(self):  # Player string representation
        return f"{self.name}"  # return Player string representation


class Table:  # Table class

    def __init__(self):  # Table constructor

        self.cards_on_table = []  # start with empty list
        self.value = 0  # start with zero value

    def __getitem__(self, item):  # get item from list
        return self.cards_on_table[item]  # return item from list

    # TODO: There is many types of canasta:
    #       Mixed canasta - 4+ cards of the same rank + wild cards.
    #       Natural canasta - 7+ cards of the same rank.
    #       Golden canasta - 7+ wild cards.:


    def check_if_player_have_canasta(self, player):  # check if player have any canasta

        try:

            if len(self.cards_on_table[0]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[1]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[2]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[3]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[4]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[5]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[6]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[7]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[8]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[9]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
            elif len(self.cards_on_table[10]) == 7:
                print(f"{player} you have a canasta!")
                print("You can now end a game.")
        except IndexError:
            pass

    def calculate_value_of_table(self):  # calculate value of table

        self.value = 0  # start with zero value

        for list_of_cards in self.cards_on_table:  # add each Card object's value
            for card in list_of_cards:
                self.value += card.value[card.rank]  # add value of card to value of table
        return self.value  # return value of table

    def add_cards(self, *args):  # add cards to table

        self.cards_on_table.extend(args)

    def __str__(self):  # Table string representation

        output = ''  # start with empty string

        for index, card in enumerate(self.cards_on_table):  # add each Card object's string representation

            if card is not None:
                index += 0
                output += f'{index}: {card}\n'  # add index and card to output string

        return f"\n{output} "  # return Table string representation

    def check_for_duplicate_cards_on_table(self, list_of_cards):  # check if player have duplicate cards on table

        for cards_on_table in self.cards_on_table:  # check each cards on table
            for card_in_hand in reversed(list_of_cards):  # check each card in hand

                try:

                    if cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Fou':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Fiv':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Six':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Sev':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Eig':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Nin':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Ten':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Jac':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Que':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Kin':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                    elif cards_on_table[0].rank[:3] == card_in_hand.rank[:3] and cards_on_table[0].rank[:3] == 'Ace':
                        print(f"On the table u have:{self.__str__()}")
                        print(f"And you have a duplicate card {card_in_hand} on your hand.")
                        answer = put_on_table2(card_in_hand)
                        place = find_index_of_element(self.cards_on_table, card_in_hand)
                        if answer is None:
                            pass
                        else:
                            self.cards_on_table[place].append(answer)
                            list_of_cards.remove(card_in_hand)
                            print(self.__str__())
                            continue
                except IndexError:
                    pass
                except TypeError:
                    pass


class PileOfCards:  # class for pile of cards

    def __init__(self):  # Pile constructor
        self.pile = []  # list of cards in pile
        self.last_card = self.pile  # last card in pile

    def add_card(self, card):  # method for adding card to pile
        self.pile.append(card)

    def __str__(self):  # method for printing last card of pile
        try:
            return f"Last card on the pile: {self.last_card[-1]}"  # printing last card on pile
        except IndexError:  # if pile is empty
            return "There is nothing on the pile"  # printing that pile is empty

    def if_black_three(self):  # method for checking if last card on pile is black three
        try:
            if self.last_card[-1].rank[:3] == 'Thr' and self.last_card[-1].suit == '♠' \
                    or self.last_card[-1].rank[:3] == 'Thr' and self.last_card[-1].suit == '♣':
                print("Black three destroys pile of cards")
                self.pile.clear()
            else:
                pass
        except IndexError:
            pass

    def if_player_have_2cards_in_hand(self, player, table):
        """
        method that checks if a player can take a pile of cards
        if he has 2 same cards in hand, and last card on pile is the same
        :param player: player object
        :param table: table object
        """
        try:
            if self.last_card[-1].rank[:3] == player.all_cards[0].rank[:3] == player.all_cards[1].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[0]}, {player.all_cards[1]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[0], player.all_cards[1], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[0], player.all_cards[1]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[1].rank[:3] == player.all_cards[2].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[1]}, {player.all_cards[2]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[1], player.all_cards[2], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[1], player.all_cards[2]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[2].rank[:3] == player.all_cards[3].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[2]}, {player.all_cards[3]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[2], player.all_cards[3], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[2], player.all_cards[3]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[3].rank[:3] == player.all_cards[4].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[3]}, {player.all_cards[4]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[3], player.all_cards[4], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[3], player.all_cards[4]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[4].rank[:3] == player.all_cards[5].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[4]}, {player.all_cards[5]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[4], player.all_cards[5], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[4], player.all_cards[5]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[5].rank[:3] == player.all_cards[6].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[5]}, {player.all_cards[6]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[5], player.all_cards[6], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[5], player.all_cards[6]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[6].rank[:3] == player.all_cards[7].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[6]}, {player.all_cards[7]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[6], player.all_cards[7], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[6], player.all_cards[7]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[7].rank[:3] == player.all_cards[8].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[7]}, {player.all_cards[8]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[7], player.all_cards[8], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[7], player.all_cards[8]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[8].rank[:3] == player.all_cards[9].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[8]}, {player.all_cards[9]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[8], player.all_cards[9], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[8], player.all_cards[9]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[9].rank[:3] == player.all_cards[10].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[9]}, {player.all_cards[10]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[9], player.all_cards[10], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[9], player.all_cards[10]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[10].rank[:3] == player.all_cards[11].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[10]}, {player.all_cards[11]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[10], player.all_cards[11], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[10], player.all_cards[11]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[11].rank[:3] == player.all_cards[12].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[11]}, {player.all_cards[12]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[11], player.all_cards[12], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[11], player.all_cards[12]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player.all_cards[12].rank[:3] == player.all_cards[13].rank[:3]:
                print(f"You have two cards of the same rank in hand {player.all_cards[12]}, {player.all_cards[13]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    table.add_cards([player.all_cards[12], player.all_cards[13], self.last_card[-1]])
                    print(table)
                    self.pile.pop()
                    player.remove_few(player.all_cards, [player.all_cards[12], player.all_cards[13]])
                    player.all_cards.extend(self.pile)
                    player.all_cards = player.sort_cards()
                    self.pile.clear()
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
        except IndexError:
            pass

    def if_player_have_it_on_table(self, player, player_table):
        """
        method that checks if a player can take a pile of cards
        if he has them on the table and the last card on the pile is the same
        :param player: player object
        :param player_table: table object
        """
        try:
            if self.last_card[-1].rank[:3] == player_table[0][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[0]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[0].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[1][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[1]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[1].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[2][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[2]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[2].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[3][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[3]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[3].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[4][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[4]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[4].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[5][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[5]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[5].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[6][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[6]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[6].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[7][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[7]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[7].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[8][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[8]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[8].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[9][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[9]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[9].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
            elif self.last_card[-1].rank[:3] == player_table[10][0].rank[:3]:
                print(f"You have cards of the same rank on table: {player_table[10]}")
                print(f"And last card on the pile is the same: {self.last_card[-1]}")
                answer = input("Do you want take a pile? (Y/N)")
                if answer == 'Y' or answer == 'y':
                    player_table[10].append(self.last_card[-1])
                    self.pile.pop()
                    print(player_table)
                    player.add_cards(self.pile)
                    self.pile.clear()
                    print(player.all_cards)
                    return True
                elif answer == 'N' or answer == 'n':
                    player.add_cards(new_deck1.deal_one())
                    print(f"You are now drawing a card: {player.all_cards[-1]}")
                    return False
        except IndexError:
            pass


def position_choice(list_of_cards):  # function that chooses which card to discard.

    how_many_cards = len(list_of_cards)  # how many cards player has

    position = 15

    while position not in list(range(0, how_many_cards)):

        try:
            print(list_of_cards)
            position = int(input(f"Select which card you want to discard  ( 0 - {how_many_cards - 1} ): "))

            if position not in list(range(0, how_many_cards)):
                print("Sorry, but you did not choose valid position")
        except ValueError:
            print(f"Sorry, i dont understand. You can choose only position ( 0 - {how_many_cards - 1} )")

    return position


def find_index_of_element(mylist, element):  # function that finds index of element in list
    try:
        for sub_list in mylist:
            if element.rank[:3] in sub_list[0].rank[:3]:
                return mylist.index(sub_list)
    except ValueError:
        pass


def put_on_table(*args):  # function that puts cards on table

    choice_args = ''

    mixed_choice = ['Y', 'N', 'y', 'n']
    right_choice = ['Y', 'y']

    while choice_args not in mixed_choice:

        choice_args = input(f'Do you want put them on the table? {list(args)} (Y or N) ')

        if choice_args not in mixed_choice:
            print("Sorry, i dont understand please choose Y or N")

    if choice_args in right_choice:
        if round_counter % 2 == 0:
            lt = list(args)
            player_one_table.add_cards(lt)
            player_one.remove_few(player_one.all_cards, lt)
            print(player_one_table)
        else:
            lt = list(args)
            player_two_table.add_cards(lt)
            player_two.remove_few(player_two.all_cards, lt)
            print(player_two_table)


def put_on_table2(card):  # function that puts card on the table
    reply = ''

    mixed_choice = ['Y', 'N', 'y', 'n']
    right_choice = ['Y', 'y']

    while reply not in mixed_choice:

        reply = input(f'Do you want put {card} on the table?  (Y or N) ')

        if reply not in mixed_choice:
            print("Sorry, i dont understand please choose Y or N")

    if reply in right_choice:

        return card
    else:
        pass


def put_on_table3(player, *args):  # function that puts cards on table

    choice_args = ''

    mixed_choice = ['Y', 'N', 'y', 'n']
    right_choice = ['Y', 'y']

    while choice_args not in mixed_choice:

        choice_args = input(f'Do you want put them on the table? {list(args)} (Y or N) ')

        if choice_args not in mixed_choice:
            print("Sorry, i dont understand please choose Y or N")

    if choice_args in right_choice:
        lt = list(args)
        return lt


def check_duplicate_cards(list_of_cards):
    """
    Function that checks if player has duplicate cards in hand
    :param list_of_cards:
    """
    # FIXME: The player should not be able to put wildcards on the table
    # Checking possible permutation in a row from index 0 to index 7
    try:

        if list_of_cards[0].rank[:3] == list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == \
                list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3]:
            return put_on_table(list_of_cards[0], list_of_cards[1], list_of_cards[2], list_of_cards[3],
                                list_of_cards[4],
                                list_of_cards[5], list_of_cards[6], list_of_cards[7])

        elif list_of_cards[0].rank[:3] == list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == \
                list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3]:
            return put_on_table(list_of_cards[0], list_of_cards[1], list_of_cards[2], list_of_cards[3],
                                list_of_cards[4],
                                list_of_cards[5], list_of_cards[6])

        elif list_of_cards[0].rank[:3] == list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == \
                list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3]:
            return put_on_table(list_of_cards[0], list_of_cards[1], list_of_cards[2], list_of_cards[3],
                                list_of_cards[4],
                                list_of_cards[5])

        elif list_of_cards[0].rank[:3] == list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == \
                list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3]:
            return put_on_table(list_of_cards[0], list_of_cards[1], list_of_cards[2], list_of_cards[3],
                                list_of_cards[4])

        elif list_of_cards[0].rank[:3] == list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == \
                list_of_cards[3].rank[:3]:
            return put_on_table(list_of_cards[0], list_of_cards[1], list_of_cards[2], list_of_cards[3])

        elif list_of_cards[0].rank[:3] == list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3]:
            return put_on_table(list_of_cards[0], list_of_cards[1], list_of_cards[2])

        # Checking possible permutation in a row from index 1 to index 8

        elif list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == \
                list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3]:
            return put_on_table(list_of_cards[1], list_of_cards[2], list_of_cards[3], list_of_cards[4],
                                list_of_cards[5],
                                list_of_cards[6], list_of_cards[7], list_of_cards[8])

        elif list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == \
                list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3]:
            return put_on_table(list_of_cards[1], list_of_cards[2], list_of_cards[3], list_of_cards[4],
                                list_of_cards[5],
                                list_of_cards[6], list_of_cards[7])

        elif list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == \
                list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3]:
            return put_on_table(list_of_cards[1], list_of_cards[2], list_of_cards[3], list_of_cards[4],
                                list_of_cards[5],
                                list_of_cards[6])

        elif list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == \
                list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3]:
            return put_on_table(list_of_cards[1], list_of_cards[2], list_of_cards[3], list_of_cards[4],
                                list_of_cards[5])

        elif list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == \
                list_of_cards[4].rank[:3]:
            return put_on_table(list_of_cards[1], list_of_cards[2], list_of_cards[3], list_of_cards[4])

        elif list_of_cards[1].rank[:3] == list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3]:
            return put_on_table(list_of_cards[1], list_of_cards[2], list_of_cards[3])

        # Checking possible permutation in a row from index 2 to index 9

        elif list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == \
                list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3]:
            return put_on_table(list_of_cards[2], list_of_cards[3], list_of_cards[4], list_of_cards[5],
                                list_of_cards[6],
                                list_of_cards[7], list_of_cards[8], list_of_cards[9])

        elif list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == \
                list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3]:
            return put_on_table(list_of_cards[2], list_of_cards[3], list_of_cards[4], list_of_cards[5],
                                list_of_cards[6],
                                list_of_cards[7], list_of_cards[8])

        elif list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == \
                list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3]:
            return put_on_table(list_of_cards[2], list_of_cards[3], list_of_cards[4], list_of_cards[5],
                                list_of_cards[6],
                                list_of_cards[7])

        elif list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == \
                list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3]:
            return put_on_table(list_of_cards[2], list_of_cards[3], list_of_cards[4], list_of_cards[5],
                                list_of_cards[6])

        elif list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == \
                list_of_cards[5].rank[:3]:
            return put_on_table(list_of_cards[2], list_of_cards[3], list_of_cards[4], list_of_cards[5])

        elif list_of_cards[2].rank[:3] == list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3]:
            return put_on_table(list_of_cards[2], list_of_cards[3], list_of_cards[4])

        # Checking possible permutation in a row from index 3 to index 10

        elif list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == \
                list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3]:
            return put_on_table(list_of_cards[3], list_of_cards[4], list_of_cards[5], list_of_cards[6],
                                list_of_cards[7],
                                list_of_cards[8], list_of_cards[9], list_of_cards[10])

        elif list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == \
                list_of_cards[9].rank[:3]:
            return put_on_table(list_of_cards[3], list_of_cards[4], list_of_cards[5], list_of_cards[6],
                                list_of_cards[7],
                                list_of_cards[8], list_of_cards[9])

        elif list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3]:
            return put_on_table(list_of_cards[3], list_of_cards[4], list_of_cards[5], list_of_cards[6],
                                list_of_cards[7],
                                list_of_cards[8])

        elif list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3]:
            return put_on_table(list_of_cards[3], list_of_cards[4], list_of_cards[5], list_of_cards[6],
                                list_of_cards[7])

        elif list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == \
                list_of_cards[6].rank[:3]:
            return put_on_table(list_of_cards[3], list_of_cards[4], list_of_cards[5], list_of_cards[6])

        elif list_of_cards[3].rank[:3] == list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3]:
            return put_on_table(list_of_cards[3], list_of_cards[4], list_of_cards[5])

        # Checking possible permutation in a row from index 4 to index 11

        elif list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == \
                list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3]:
            return put_on_table(list_of_cards[4], list_of_cards[5], list_of_cards[6], list_of_cards[7],
                                list_of_cards[8],
                                list_of_cards[9], list_of_cards[10], list_of_cards[11])

        elif list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == \
                list_of_cards[10].rank[:3]:
            return put_on_table(list_of_cards[4], list_of_cards[5], list_of_cards[6], list_of_cards[7],
                                list_of_cards[8],
                                list_of_cards[9], list_of_cards[10])

        elif list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3]:
            return put_on_table(list_of_cards[4], list_of_cards[5], list_of_cards[6], list_of_cards[7],
                                list_of_cards[8],
                                list_of_cards[9])

        elif list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3]:
            return put_on_table(list_of_cards[4], list_of_cards[5], list_of_cards[6], list_of_cards[7],
                                list_of_cards[8])

        elif list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == \
                list_of_cards[7].rank[:3]:
            return put_on_table(list_of_cards[4], list_of_cards[5], list_of_cards[6], list_of_cards[7])

        elif list_of_cards[4].rank[:3] == list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3]:
            return put_on_table(list_of_cards[4], list_of_cards[5], list_of_cards[6])

        # Checking possible permutation in a row from index 5 to index 12

        elif list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == \
                list_of_cards[11].rank[:3] == list_of_cards[12].rank[:3]:
            return put_on_table(list_of_cards[5], list_of_cards[6], list_of_cards[7], list_of_cards[8],
                                list_of_cards[9],
                                list_of_cards[10], list_of_cards[11], list_of_cards[12])

        elif list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == \
                list_of_cards[11].rank[:3]:
            return put_on_table(list_of_cards[5], list_of_cards[6], list_of_cards[7], list_of_cards[8],
                                list_of_cards[9],
                                list_of_cards[10], list_of_cards[11])

        elif list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3]:
            return put_on_table(list_of_cards[5], list_of_cards[6], list_of_cards[7], list_of_cards[8],
                                list_of_cards[9],
                                list_of_cards[10])

        elif list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3]:
            return put_on_table(list_of_cards[5], list_of_cards[6], list_of_cards[7], list_of_cards[8],
                                list_of_cards[9])

        elif list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == \
                list_of_cards[8].rank[:3]:
            return put_on_table(list_of_cards[5], list_of_cards[6], list_of_cards[7], list_of_cards[8])

        elif list_of_cards[5].rank[:3] == list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3]:
            return put_on_table(list_of_cards[5], list_of_cards[6], list_of_cards[7])

        # Checking possible permutation in a row from index 6 to index 12

        elif list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == \
                list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3] == \
                list_of_cards[12].rank[:3]:
            return put_on_table(list_of_cards[6], list_of_cards[7], list_of_cards[8], list_of_cards[9],
                                list_of_cards[10],
                                list_of_cards[11], list_of_cards[12])

        elif list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == \
                list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3]:
            return put_on_table(list_of_cards[6], list_of_cards[7], list_of_cards[8], list_of_cards[9],
                                list_of_cards[10],
                                list_of_cards[11])

        elif list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == \
                list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3]:
            return put_on_table(list_of_cards[6], list_of_cards[7], list_of_cards[8], list_of_cards[9],
                                list_of_cards[10])

        elif list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == \
                list_of_cards[9].rank[:3]:
            return put_on_table(list_of_cards[6], list_of_cards[7], list_of_cards[8], list_of_cards[9])

        elif list_of_cards[6].rank[:3] == list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3]:
            return put_on_table(list_of_cards[6], list_of_cards[7], list_of_cards[8])

        # Checking possible permutation in a row from index 7 to index 12

        elif list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == \
                list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3] == list_of_cards[12].rank[:3]:
            return put_on_table(list_of_cards[7], list_of_cards[8], list_of_cards[9], list_of_cards[10],
                                list_of_cards[11],
                                list_of_cards[12])

        elif list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == \
                list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3]:
            return put_on_table(list_of_cards[7], list_of_cards[8], list_of_cards[9], list_of_cards[10],
                                list_of_cards[11])

        elif list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == \
                list_of_cards[10].rank[:3]:
            return put_on_table(list_of_cards[7], list_of_cards[8], list_of_cards[9], list_of_cards[10])

        elif list_of_cards[7].rank[:3] == list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3]:
            return put_on_table(list_of_cards[7], list_of_cards[8], list_of_cards[9])

        # Checking possible permutation in a row from index 8 to index 12

        elif list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == \
                list_of_cards[11].rank[:3] == list_of_cards[12].rank[:3]:
            return put_on_table(list_of_cards[8], list_of_cards[9], list_of_cards[10], list_of_cards[11],
                                list_of_cards[12])

        elif list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == \
                list_of_cards[11].rank[:3]:
            return put_on_table(list_of_cards[8], list_of_cards[9], list_of_cards[10], list_of_cards[11])

        elif list_of_cards[8].rank[:3] == list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3]:
            return put_on_table(list_of_cards[8], list_of_cards[9], list_of_cards[10])

        # Checking possible permutation in a row from index 9 to index 12

        elif list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3] == \
                list_of_cards[12].rank[:3]:
            return put_on_table(list_of_cards[9], list_of_cards[10], list_of_cards[11], list_of_cards[12])

        elif list_of_cards[9].rank[:3] == list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3]:
            return put_on_table(list_of_cards[9], list_of_cards[10], list_of_cards[11])

        # Checking possible permutation in a row from index 10 to index 12

        elif list_of_cards[10].rank[:3] == list_of_cards[11].rank[:3] == list_of_cards[12].rank[:3]:
            return put_on_table(list_of_cards[10], list_of_cards[11], list_of_cards[12])

    except IndexError:
        pass


def red_three_check(list_of_cards, player):

    """This function checks if the player has a red three and if he does, it puts it on the table automatically"""

    three1 = Card('\u2665', 'Three')
    three2 = Card('\u2666', 'Three')

    list_of_three = []

    for element in reversed(list_of_cards):

        while element == three1:
            print(f"{player} you have a {three1} on your Hand, I'll put it on the table for you.")
            print('You are now drawing a card:')
            list_of_three.append(element)
            player.add_card(new_deck1.deal_one())
            player.remove_cards(element)
            print(player.all_cards[-1])
            player.all_cards = player.sort_cards()
            break
        while element == three2:
            print(f"{player} you have a {three2} on your Hand, I'll put it on the table for you.")
            print('You are now drawing a card:')
            list_of_three.append(element)
            player.add_card(new_deck1.deal_one())
            player.remove_cards(element)
            print(player.all_cards[-1])
            player.all_cards = player.sort_cards()
            break

    if len(list_of_three) == 0:
        pass
    else:
        if round_counter % 2 == 0:
            player_one_table.add_cards(list_of_three)
        else:
            player_two_table.add_cards(list_of_three)


def clear_screen():  # This function clears the screen
    print('\n' * 50)


# GAME SETUP

player_one = Player("Player one")  # Creating player one
player_two = Player("Player two")  # Creating player two

new_deck1 = Deck()  # Creating a new deck
new_deck1.shuffle()  # Shuffling the deck

new_pile = PileOfCards()  # Creating a new pile

player_one_table = Table()  # Creating a table for player one
player_two_table = Table()  # Creating a table for player two


for _ in range(13):  # Dealing 13 cards to each player
    player_one.add_card(new_deck1.deal_one())  # Dealing a card to player one
    player_two.add_card(new_deck1.deal_one())  # Dealing a card to player two

game_on = True  # This variable will be used to check if the game is still on or not

while game_on:  # Main game loop

    print(f"Hello {player_one.name}, {player_two.name}. Welcome to Canasta by Paul ")  # Greeting the players

    round_counter = 1  # This variable will be used to check if it's player one or player two turn

    while game_on:  # Round loop
        if round_counter % 2 == 0:  # Checking if it's player one turn
            new_pile.if_black_three()  # Checking if the pile has a black three
            player_one.all_cards = player_one.sort_cards()  # Sorting player one cards
            print(f"{player_one.name} it's your turn. Turn: {round_counter}")  # Printing player name and number of turn
            print(f"{player_one}, here are your cards:")
            print(player_one.all_cards)  # Printing player one cards
            # Checking if function new_pile.if_player_have_it_on_table() returns True
            if new_pile.if_player_have_it_on_table(player_one, player_one_table) is True:
                pass
            # Checking if function new_pile.if_player_have_2cards_in_hand() returns True
            elif new_pile.if_player_have_2cards_in_hand(player_one, player_one_table) is True:
                pass
            # if not, then the player will have to draw a card
            else:
                player_one.add_card(new_deck1.deal_one())
                print(f"{player_one.name} draw a {player_one.all_cards[-1]}")
                player_one.all_cards = player_one.sort_cards()
                print(player_one.all_cards)
            print(new_pile)  # Printing the pile
            print(f'Your table: {player_one_table}')  # Printing player table
            red_three_check(player_one.all_cards, player_one)  # Checking if player has a red three
            check_duplicate_cards(player_one.all_cards)  # Checking if player has duplicate cards on table
            # Checking if player has duplicate cards on table
            player_one_table.check_for_duplicate_cards_on_table(player_one.all_cards)
            print(player_one.all_cards)  # Printing player cards
            check_duplicate_cards(player_one.all_cards)  # Checking if player has duplicate cards on table
            player_one.if_player_have_2cards_in_hand_and_wild_card(player_one)
            # Checking if player has 2 cards in hand and a wild card to put in on table
            player_one.if_player_have_wild_card(player_one_table.cards_on_table)  # Checking if player has a wild card
            player_one_table.check_if_player_have_canasta(player_one)  # Checking if player has a canasta
            print(f'This is enemy table:' + player_two_table.__str__())  # Printing enemy table
            next_move = ''
            while next_move not in ['y', 'Y', 'n', 'N']:

                next_move = input("Do you want end of turn? (Y/N)")  # Asking player if he wants to end of turn

                if next_move == 'y' or next_move == 'Y':  # if yes then the turn will end, and he will throw a card.
                    choice = position_choice(player_one.all_cards)  # Asking player to choose a card to throw
                    # Removing the card from player hand and adding it to the pile
                    new_pile.add_card(player_one.remove_one(choice))
                    round_counter += 1  # Increasing the round counter
                    clear_screen()  # Clearing the screen
                    continue  # Going back to the round loop
                elif next_move == 'n' or next_move == 'N':  # if no then ask about end of game
                    end_of_game = input("Do you want to end the game? (Y/N)")
                    if end_of_game == 'y' or end_of_game == 'Y':  # if yes then the game will end
                        print('Thanks for playing!')
                        quit()
                    else:  # if no then the turn will continue
                        choice = position_choice(player_one.all_cards)
                        new_pile.add_card(player_one.remove_one(choice))
                        round_counter += 1
                        clear_screen()
                        continue
        if len(player_one.all_cards) == 0:  # Checking if player one has no cards left
            print(f"{player_one.name} you have no cards left, you win!")  # Printing player one win message
            game_on = False  # Ending the game
            break  # Ending the round loop
        elif round_counter % 2 == 1:  # Checking if it's player two turn
            new_pile.if_black_three()  # Checking if the pile has a black three
            player_two.all_cards = player_two.sort_cards()  # Sorting player two cards
            print(f"{player_two.name} it's your turn. Turn: {round_counter}")  # Printing player name and number of turn
            print(f"{player_two}, here are your cards:")
            print(player_two.all_cards)  # Printing player two cards
            if new_pile.if_player_have_it_on_table(player_two, player_two_table) is True:
                # Checking if function new_pile.if_player_have_it_on_table() returns True
                pass
            elif new_pile.if_player_have_2cards_in_hand(player_two, player_two_table) is True:
                # Checking if function new_pile.if_player_have_2cards_in_hand() returns True
                pass
                # if not, then the player will have to draw a card
            else:
                player_two.add_card(new_deck1.deal_one())
                print(f"{player_two.name} draw a {player_two.all_cards[-1]}")
                player_two.all_cards = player_two.sort_cards()
                print(player_two.all_cards)
            print(new_pile)  # Printing the pile
            print(f'Your table: {player_two_table}')  # Printing player table
            red_three_check(player_two.all_cards, player_two)  # Checking if player has a red three
            check_duplicate_cards(player_two.all_cards)  # Checking if player has duplicate cards on table
            red_three_check(player_two.all_cards, player_two)  # Checking if player has a red three
            player_two_table.check_for_duplicate_cards_on_table(player_two.all_cards)
            # Checking if player has duplicate cards on table
            print(player_two.all_cards)  # Printing player cards
            check_duplicate_cards(player_two.all_cards)  # Checking if player has duplicate cards on table
            player_two.if_player_have_2cards_in_hand_and_wild_card(player_two)
            # Checking if player has 2 cards in hand and a wild card to put in on table
            player_two.if_player_have_wild_card(player_two_table.cards_on_table)  # Checking if player has a wild card
            player_two_table.check_if_player_have_canasta(player_two)  # Checking if player has a canasta
            print(f'This is enemy table:' + player_one_table.__str__())  # Printing enemy table
            next_move = ''
            while next_move not in ['y', 'Y', 'n', 'N']:
                next_move = input("Do you want end of turn? (Y/N)")  # Asking player if he wants to end of turn
                if next_move == 'y' or next_move == 'Y':  # if yes then the turn will end, and he will throw a card.
                    choice = position_choice(player_two.all_cards)  # Asking player to choose a card to throw
                    new_pile.add_card(player_two.remove_one(choice))
                    #  Removing the card from player hand and adding it to the pile
                    round_counter += 1  # Increasing the round counter
                    clear_screen()  # Clearing the screen
                    continue  # Going back to the round loop
                elif next_move == 'n' or next_move == 'N':  # if no then ask about end of game
                    end_of_game = input("Do you want to end the game? (Y/N)")
                    if end_of_game == 'y' or end_of_game == 'Y':  # if yes then the game will end
                        print('Thanks for playing!')
                        quit()
                    else:  # if no then the turn will continue
                        choice = position_choice(player_two.all_cards)
                        new_pile.add_card(player_two.remove_one(choice))
                        round_counter += 1
                        clear_screen()
                        continue
        # FIXME: When player have last two cards and enemy will throw exactly the same card,
        #        list of cards in hand is empty and you can't throw a card and win game.
        if len(player_two.all_cards) == 0:  # Checking if player two has no cards left
            print(f"{player_two.name} you have no cards left, you win!")  # Printing player two win message
            game_on = False  # Ending the game
            break  # Ending the round loop
