"""
написать приложение-сервер используя модуль socket работающее в домашней
локальной сети.
Приложение должно принимать данные с любого устройства в сети отправленные
или через программу клиент или через браузер
    - если данные пришли по протоколу http создать возможность след.логики:
        - если путь содержит /test/<int>/ вывести сообщение - тест с номером int запущен

        - если путь содержит message/<login>/<text>/ вывести в консоль сообщение
            "{дата время} - сообщение от пользователя {login} - {text}"

        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные по HTTP - путь такой то"
"""
"""


    - если данные пришли НЕ по протоколу http создать возможность след.логики:
        - если пришла строка формата "command:reg; login:<login>; password:<pass>"
            - выполнить проверку:
                login - только латинские символы и цифры, минимум 6 символов
                password - минимум 8 символов, должны быть хоть 1 цифра
            - при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} зарегистрирован"
                2. добавить данные пользователя в список/словарь
            - если проверка не прошла вывести сообщение:
                "{дата время} - ошибка регистрации {login} - неверный пароль/логин"

        - если пришла строка формата "command:signin; login:<login>; password:<pass>"
            выполнить проверку зарегистрирован ли такой пользователь:

            при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} произведен вход"

            если проверка не прошла вывести сообщение
                "{дата время} - ошибка входа {login} - неверный пароль/логин"

        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные - <присланные данные>"


"""
import datetime

import socket

date_now = datetime.datetime.now()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ('127.0.0.1', 7777)

sock.bind(HOST)
sock.listen()

# path = ''
database = []


def pars_http(http_str: str):
    """Проверка введенных данных для http"""
    http_str = http_str.split('\n')[0].split()
    if len(http_str) == 3 and 'HTTP/1.1' in http_str[2]:
        path_http = http_str[1].strip('/').split('/')
        return path_http


def check_format_str(data_str: str):
    """
    Проверка формата введенной строки на наличие логина и пароля.
    Создание списка данных при успешной проверке.
    """
    try:
        data_str = data_str.split('; ')
        pars_data = list(map(lambda x: x.split(':'), data_str))
        if pars_data[0][0] == 'command' and pars_data[1][0] == 'login' and pars_data[2][0] == 'password':
            pars_data_reg = [pars_data[0][1], pars_data[1][1], pars_data[2][1]]
            return pars_data_reg
        else:
            print('Неверный формат строки')
    except Exception:
        print('Неверный формат строки')


def check_login(parsed_data: list):
    """Проверка правильности логина"""
    logg = parsed_data[1]
    if len(logg) >= 6 and all(x.isalnum() for x in logg):
        return logg
    else:
        raise ValueError(print(f'{date_now} - ошибка регистрации {logg} - неверный логин'))


def check_password(parsed_data: list):
    """Проверка правильности пароля"""
    passw = parsed_data[2]
    if len(passw) >= 8 and any(True for x in passw if x.isdigit()):
        return passw
    else:
        raise ValueError(print(f'{date_now} - ошибка регистрации {parsed_data[1]} - неверный пароль'))


def check_signin(datab: list, parsed_str: list):
    """Проверка наличия пользователя в базе данных"""
    for i in range(len(datab)):
        if datab[i]['login'] == parsed_str[1] and datab[i]['password'] == parsed_str[2]:
            print(f'{date_now} - пользователь {parsed_str[1]} произведен вход')
        elif datab[i]['login'] != parsed_str[1]:
            print(f'{date_now} - неверный логин')
        elif datab[i]['login'] == parsed_str[1] and datab[i]['password'] != parsed_str[2]:
            print(f'{date_now} - пользователь {parsed_str[1]} неверный пароль')
        else:
            print(f'{date_now} - пользователь login: {parsed_str[1]} не найден')
            return parsed_str[1]


while True:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()
    try:
        parsed_http = pars_http(data)
        if parsed_http[0] == 'test' and parsed_http[1].isdigit():
            print(f'Тест с номером {parsed_http[1]} запущен')
        elif parsed_http[0] == 'message' and len(parsed_http) == 3:
            print(f'{date_now} - сообщение от пользователя {parsed_http[0]} - {parsed_http[1]}')
        else:
            print(f'Пришли неизвестные данные по HTTP - путь /{'/'.join(parsed_http)}/')
    except Exception:
        res = 'Данные получены не по HTTP'
        print(res)

    if res:
        user = {}
        try:
            parsed_str_reg = check_format_str(data)
            if parsed_str_reg[0] == 'reg':
                str_login = check_login(parsed_str_reg)
                str_passw = check_password(parsed_str_reg)
                user['login'] = str_login
                user['password'] = str_passw
                database.append(user)
                print(database)
                print(f'{date_now} - пользователь {str_login} зарегистрирован')
            elif parsed_str_reg[0] == 'signin':
                signin = check_signin(database, parsed_str_reg)
        except Exception:
            print(f'пришли неизвестные  данные - {data}')
