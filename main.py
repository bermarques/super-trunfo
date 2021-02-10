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


if __name__ == '__main__':
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards_player_a, cards_player_b = get_players_decks(cards)
    print(cards_player_a, cards_player_b)
