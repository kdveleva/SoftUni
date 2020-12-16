from project.card.card import Card


class CardRepository:
    count: int
    cards: list

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card.name in [x.name for x in self.cards]:
            raise ValueError(f"Card {str(card.name)} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        self.cards = [x for x in self.cards if x.name != card]
        self.count -= 1

    def find(self, name: str):
        card_to_return = [x for x in self.cards if x.name == name][0]
        return card_to_return

