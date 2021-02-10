from superheroes import SUPER_HEROS
from random import shuffle


def get_players_decks(card_list: list):
    if len(card_list) % 2 != 0:
        return None

    shuffle(card_list)

    qtd_card_to_each_player = len(card_list) // 2

    cards_player_a = card_list[:qtd_card_to_each_player]
    cards_player_b = card_list[qtd_card_to_each_player:]

    return cards_player_a, cards_player_b


def compare_cards(cards_of_player_a, cards_of_player_b, score):
    turn_winners = []

    for index_card in range(len(cards_of_player_a)):
        card_of_player_a = cards_of_player_a[index_card]
        card_of_player_b = cards_of_player_b[index_card]

        card_winner = []
        for attributes in card_of_player_a.keys():
            if attributes != 'name':
                if card_of_player_a[attributes] > card_of_player_b[attributes]:
                    winner = 1
                elif card_of_player_a[attributes] < card_of_player_b[attributes]:
                    winner = 2
                card_winner.append(winner)

        turn_winners.append(1 if card_winner.count(1) > card_winner.count(2) else 2)

    return turn_winners.count(1), turn_winners.count(2)


def main():
    score = (0, 0,)
    cards_player_a, cards_player_b = get_players_decks(SUPER_HEROS)
    scores = compare_cards(cards_player_a[:1], cards_player_b[:1], score)
    print(scores)


if __name__ == '__main__':
    main()
