import re

from flask import render_template, url_for, session, redirect, request
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


def find_login(login):
    user = db.get_or_404(User, login)
    return user


# @app.route('/user/login/', methods=["GET", "POST"])
def user_log():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        user = find_login(login)
        if user.password == password:
            session['name'] = user.name
            session['user_id'] = user.id
        else:
            error3 = 'Неверный логин или пароль'
            return render_template('user/user_login.html', error3=error3)
        return redirect(url_for("index"))
    return render_template('user/user_login.html')

