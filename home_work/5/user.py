import re
from flask import request
from main import *

error = []


def check_name():
    name = request.form['name']
    if re.match(r'^[а-яА-ЯёЁ\s]+$', name):
        return name
    else:
        error1 = 'Имя должно содержать только русские буквы'
        global error
        error.append(error1)
        return error


def check_surname():
    surname = request.form['surname']
    if re.match(r'^[а-яА-ЯёЁ\s]+$', surname):
        return surname
    else:
        error2 = 'Фамилия должна содержать только русские буквы'
        global error
        error.append(error2)
        return error


def check_login():
    login = request.form['login']
    if re.match(r'^[a-zA-Z][a-zA-Z0-9-_]{5,20}$', login):
        return login
    else:
        error3 = 'Логин должен содержать только латинские буквы, цифры и символ "_"'
        global error
        error.append(error3)
        return error


def check_password():
    password = request.form['password']
    if re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,15}$', password):
        return password
    else:
        error4 = ('Пароль должен содержать от 8 до 15 символов, '
                  'хотя бы одну латинскую строчную и заглавную буквы и одну цифру')
        global error
        error.append(error4)
        return error


# def check_email():
#     email = request.form['email']
#     if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
#         return email
#     else:
#         error5 = 'Проверьте правильность введенного электронного адреса'
#         global error
#         error.append(error5)
#         return error




