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
        print(f'{'Name:'}{self.name} {'Health:'}{self.health} {'Armor:'}{self.armor} {'Strong:'}{self.strong}')

    def kick(self, enemy, kick_k=1):
        self.health -= kick_k
        self.armor = self.armor - enemy.strong + kick_k
        if self.armor < 0:
            self.armor = 0
        if self.health <= 0:
            print(f'Hero {self.name} is dead')
        else:
            print(f'Hero after kick: {'Name:'}{self.name} {'Health:'}{self.health} {'Armor:'}{self.armor} {'Strong:'}{self.strong}')

    def fight(self, enemy):
        while True:
            random_kick = random.choice([1, 2])
            if random_kick == 1:
                print(f'{enemy.name} attacks')
                if self.armor > 0:
                    self.armor -= (enemy.strong * 0.75)
                    if self.armor > 0:
                        self.health -= (enemy.strong * 0.25)
                    else:
                        self.health -= (enemy.strong * 0.25 - self.armor)
                else:
                    self.health -= enemy.strong
                print(f'{self.name} health {round(self.health)}')
            if random_kick == 2:
                print(f'{self.name} attacks')
                if enemy.armor > 0:
                    enemy.armor -= (self.strong * 0.75)
                    if enemy.armor > 0:
                        enemy.health -= (self.strong * 0.25)
                    else:
                        enemy.health -= (self.strong * 0.25 - enemy.strong)
                else:
                    enemy.health -= self.strong
                print(f'{enemy.name} health {round(enemy.health)}')
            if self.health <= 0:
                print(f'Hero {self.name} is dead')
                break
            elif enemy.health <= 0:
                print(f'Hero {enemy.name} is dead')
                break

    
knight = Hero('Edmund', 150, 150, 70)
witch = Hero('Jara', 90, 30, 120)

knight.print_info()
witch.print_info()
knight.kick(witch, 2)
witch.fight(knight)
