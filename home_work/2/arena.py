import random

from hero_class import Special, Mage, Knight, Ork


class Arena:
    def __init__(self, warriors=None):
        if warriors is None:
            warriors = [None] * 3
        self.warriors = warriors

    def add_warrior(self, warrior):
        if warrior not in self.warriors:
            self.warriors.append(warrior)
            print(f'{warrior} участвует в битве')
        else:
            print(f'Воин {warrior} уже на арене')

    def battle(self):
        if len(self.warriors) <= 1:
            print('Количество воинов на арене должно быть больше 1')
        else:
            while True:
                defense = random.choice(self.warriors)
                attacks = random.choice(self.warriors)
                
