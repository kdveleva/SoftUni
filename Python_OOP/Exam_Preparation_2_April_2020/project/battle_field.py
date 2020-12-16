from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def fight(attacker: Player, enemy: Player):

        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if isinstance(enemy, Beginner):
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker.health += sum([x.health_points for x in attacker.card_repository.cards])
        enemy.health += sum([x.health_points for x in enemy.card_repository.cards])

        # counter = 0
        #
        # while len(attacker.card_repository.cards) > counter:
        #
        #     attacker_attack = [x.damage_points for x in attacker.card_repository.cards][counter]
        #     enemy.take_damage(attacker_attack)
        #     if enemy.health <= 0:
        #         enemy.health = 0
        #         break
        #     enemy_attack = [x.damage_points for x in attacker.card_repository.cards][counter]
        #     attacker.take_damage(enemy_attack)
        #     if attacker.health <= 0:
        #         attacker.health = 0
        #         break
        #     counter +=

        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(c.damage_points)
