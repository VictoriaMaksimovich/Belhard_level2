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


class Hero:
    def __init__(self, name: str, health: int, armor: int, strong: int):
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong

    def print_info(self):
        print(f'Name:{self.name} Health:{self.health} Armor:{self.armor} Strong:{self.strong}')

    def kick(self, enemy: 'Hero', kick_k=1):
        print(f'{self.name} атакует с силой {self.strong * kick_k}')
        if enemy.armor > 0:
            enemy.armor -= self.strong * kick_k
            if enemy.armor < 0:
                enemy.health += enemy.armor
        else:
            enemy.health -= self.strong * kick_k
        print(f'Герой {enemy.name} был атакован. Здоровье:{enemy.health}')

    def fight(self, enemy: 'Hero'):
        while self.health or enemy.health > 0:
            self.kick(enemy)
            enemy.kick(self)
            if self.health <= 0:
                print(f'Герой {self.name} пал в бою')
                break
            elif enemy.health <= 0:
                print(f'Герой {enemy.name} пал в бою')
                break

    
knight = Hero('Edmund', 150, 100, 70)
witch = Hero('Jara', 90, 30, 120)

# knight.print_info()
# witch.print_info()
# knight.kick(witch, 2)
# witch.fight(knight)

