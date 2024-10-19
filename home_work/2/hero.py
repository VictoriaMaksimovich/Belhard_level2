"""
создать класс Hero со след атрибутами:
    свойства:
        - name
        - health
        - armor
        - strong

    методы:
        - print_info - вывод информации о герое
        - kick - принимает параметр enemy:Hero и коэффициент силы удара  по дефолту равный 1,
                производит один удар - высчитывает и уменьшает броню и здоровье,
                выводит информацию в консоль
        - fight - принимает параметр enemy:Hero и производит обмен ударами (поочереди или случайно)
                пока здоровье одного героя не достигнет 0





Создать 2 героя, вывести информацию о них, произвести бой между ними, вывести информацию
о победителе.

"""
import random


class Hero:
    def __init__(self, name: str, health: int, armor: int, strong: int):
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong

    def print_info(self):
        print(f'Name:{self.name} Health:{self.health} Armor:{self.armor} Strong:{self.strong}')

    def kick(self, enemy: 'Hero', kick_k=1):
        print(f'{enemy.name} attacks!')
        if self.armor > 0:
            self.armor -= enemy.strong * kick_k
            if self.armor < 0:
                self.health += self.armor
        else:
            self.health -= enemy.strong * kick_k
        print(f'{self.name} was attacked. Health:{self.health}')

    def fight(self, enemy: 'Hero'):
        while self.health or enemy.health > 0:
            self.kick(enemy)
            enemy.kick(self)
            if self.health <= 0:
                print(f'{self.name} is dead')
                break
            elif enemy.health <= 0:
                print(f'{enemy.name} is dead')
                break

    
knight = Hero('Edmund', 150, 150, 70)
witch = Hero('Jara', 90, 30, 120)

knight.print_info()
witch.print_info()
knight.kick(witch, 2)
witch.fight(knight)

