from flask import Flask, render_template, url_for, session, redirect, request
from get_info import *
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import re

BASE_FOLDER = os.getcwd()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, 'static'),
            template_folder=os.path.join(BASE_FOLDER, 'templates'))

app.config['SECRET_KEY'] = 'jhv;cd59-687fh;fd-1713erd!!r;gh-o8yh;gh:vjh-!-g67r:ff'

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.db'
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    surname = db.Column(db.String(50), unique=True, nullable=False)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


with app.app_context():
    db.create_all()


@app.route('/user/create/', methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        checked_name = check_name(request.form['name'])
        checked_surname = check_name(request.form['surname'])
        checked_login = check_login(request.form['login'])
        checked_password = check_password(request.form['password'])
        if checked_name and checked_surname and checked_login and checked_password is True:
            user = User(
                name=request.form['name'],
                surname=request.form['surname'],
                login=request.form['login'],
                password=request.form['password'],
                age=request.form['age'],
            )
            try:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("index", login=user.login))
            except:
                error1 = 'Пользователь с таким логином уже зарегистрирован'
                return render_template('user_create.html', error1=error1)
        else:
            error = 'Проверьте правильность введенных данных'
            print(request.form['name'])
            return render_template('user_create.html', error=error)
    else:
        return render_template("user_create.html")


def check_name(name):
    if re.match(r'^[а-яА-ЯёЁ\s]+$', name):
        return True


def check_login(login):
    if re.match(r'^[a-zA-Z][a-zA-Z0-9-_]{5,20}$', login):
        return True


def check_password(password):
    if re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,15}$', password):
        return True


# def check_email(email):
#     if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
#         return True


def find_login(login):
    with app.app_context():
        try:
            user = User.query.filter_by(login=login).first()
            return user
        except:
            print('Пользователь с таким логином не найден')


@app.route('/user/login/', methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        login = request.form.get('login'),
        password = request.form.get('password')
        user = find_login(login)
        if user.password == password:
            session['name'] = user.name
            session['user_id'] = user.id
        else:
            error3 = 'Неверный логин или пароль'
            return render_template('user_login.html', error3=error3)
        return redirect(url_for("index"))
    return render_template('user_login.html')


@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    session['num_1'] = 0
    session['num_2'] = 0
    return render_template('index.html')


@app.route('/duck/')
def rand_duck():
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    duck = get_duck()
    return render_template('duck.html', img=duck)


@app.route('/fox/<int:count>/')
def rand_fox(count):
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    if 1 <= count <= 10:
        fox_url = []
        for i in range(count):
            fox = get_fox()
            fox_url.append(fox)
        return render_template('fox.html', img=fox_url)
    else:
        return '<h1 style="color:red">такой страницы не существует</h1>'


@app.route('/weather-minsk/')
def weather_minsk():
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    city_m = 'Minsk'
    we_minsk = get_weather(city_m)
    weather_m = (f'Небо {we_minsk['weather'][0]['description']}, '
                 f'температура(K) {we_minsk['main']['temp']}, '
                 f'давление(кПа) {we_minsk['main']['pressure']}, '
                 f'влажность воздуха(%) {we_minsk['main']['humidity']}')
    return render_template('weather.html', city_m=city_m, weather_m=weather_m)


@app.route('/weather/<city>/')
def weather_city(city):
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    city = city.capitalize()
    we_city = get_weather(city)
    weather = (f'Небо {we_city['weather'][0]['description']}, '
               f'температура(K) {we_city['main']['temp']}, '
               f'давление(кПа) {we_city['main']['pressure']}, '
               f'влажность воздуха(%) {we_city['main']['humidity']}')
    return render_template('weather_city.html', city=city, weather=weather)


@app.route('/click/')
def click_picture():
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    url_1 = '/click/1/'
    url_2 = '/click/2/'
    return render_template('click.html',
                           url_1=url_1, url_2=url_2,
                           num_1=session['num_1'],
                           num_2=session['num_2'])


@app.route('/click/1/')
def click_1():
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    session['num_1'] += 1
    return redirect('/click/')


@app.route('/click/2/')
def click_2():
    if 'user_id' not in session:
        return redirect(url_for('/user/login/'))
    session['num_2'] += 1
    return redirect('/click/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
