"""
создать классы Mage, Knight, Ork унаследовав его от Hero
    новые свойства:
        - special_points - количество спец очков
        - special_points_name - мана, доблесть, ярость
        - special_points_k - коэффициент (множитель ) увеличивающий обычную атаку

    новые методы:
        - hello - приветственное сообщение с выводом информации
        - special_attack - этот удар производится с использованием коэффициента.
                При спец атаке вычитать из спец.очков 1. Невозможен если очков нет.
        - attack - с вероятностью 25% будет использовать спец.способность героя
                если у него остались спец.очки. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку.
                Вывести сообщение в консоль о типе и результате атаки.



добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод battle, который не принимает аргументов и симулирует битву. Сперва
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.


Создать несколько воинов используя разные классы, добавить их на арену и запустить битву.
Выжить должен только один.
"""

import random

from hero import Hero


class Special(Hero):
    """ Данный класс описывает специальные свойства героев """
    def __init__(self,
                 name: str,
                 health: int,
                 armor: int,
                 strong: int,
                 special_points: int,
                 special_points_name: str,
                 special_points_k: int,
                 ):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = special_points_name
        self.special_points_k = special_points_k

    def hello(self):
        print(f'I am {self.name}. My health: {self.health}, armor: {self.armor}, strong: {self.strong}')

    def special_attack(self):
        if self.special_points > 0:
            special_kick = self.strong * self.special_points_k
            self.special_points -= 1
        return special_kick

    def attack(self):
        att = self.strong
        special_att = self.special_attack()
        attack_choise = att if random.random() < 1/4 else special_att
        if attack_choise == att:
            print(f'{self.name} attacks')
        else:
            print(f'{self.name} attacks. SPECIAL ATTACK!')


class Mage(Special):
    def __init__(self,
                 name: str,
                 health: int,
                 armor: int,
                 strong: int,
                 special_points: int,
                 special_points_name: str,
                 special_points_k: int,
                 ):
        super().__init__(name, health, armor, strong, special_points, special_points_name, special_points_k)

    def get_sp_name(self):
        return self.special_points_name

    def set_sp_name(self):
        self.special_points_name = 'mana'


class Knight(Special):
    def __init__(self,
                 name: str,
                 health: int,
                 armor: int,
                 strong: int,
                 special_points: int,
                 special_points_name: str,
                 special_points_k: int,
                 ):
        super().__init__(name, health, armor, strong, special_points, special_points_name, special_points_k)

    def get_sp_name(self):
        return self.special_points_name

    def set_sp_name(self):
        self.special_points_name = 'valor'


class Ork(Special):
    def __init__(self,
                 name: str,
                 health: int,
                 armor: int,
                 strong: int,
                 special_points: int,
                 special_points_name: str,
                 special_points_k: int,
                 ):
        super().__init__(name, health, armor, strong, special_points, special_points_name, special_points_k)

    def get_sp_name(self):
        return self.special_points_name

    def set_sp_name(self):
        self.special_points_name = 'fury'
