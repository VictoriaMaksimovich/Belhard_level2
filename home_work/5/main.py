from flask import Flask, render_template, url_for, session, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from get_info import *
import os
from user import *

BASE_FOLDER = os.getcwd()


app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, 'static'),
            template_folder=os.path.join(BASE_FOLDER, 'templates'))

app.config['SECRET_KEY'] = 'jhv;cd59-687fh;fd-1713erd!!r;gh-o8yh;gh:vjh-!-g67r:ff'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
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
    try:
        if request.method == "POST":
            user = User(
                name=check_name(),
                surname=check_surname(),
                login=check_login(),
                password=check_password(),
                age=request.form['age'],
            )
            db.session.add(user)
            db.session.commit()
            print('Пользователь добавлен в базу')
            return redirect(url_for("index", login=user.login))
    except:
        print('Пользователь не добавлен в базу')
        return render_template('user/user_create.html', error=error)
    return render_template('user/user_create.html')


@app.route('/user/login/', methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        user = db.query(User).filter(User.login == login)
        if user.password == password:
            session['name'] = user.name
            session['user_id'] = user.id
        else:
            print('Неверный логин или пароль')
            return render_template('user/user_login.html')
        return redirect(url_for("index"))
    return render_template('user/user_login.html')


@app.route('/')
def index():
    # if 'user_id' not in session:
    #     return redirect('user/user_login.html')
    session['num_1'] = 0
    session['num_2'] = 0
    return render_template('index.html')


@app.route('/duck/')
def rand_duck():
    if 'user_id' not in session:
        return redirect('user/user_login.html')
    duck = get_duck()
    return render_template('duck.html', img=duck)


@app.route('/fox/<int:count>/')
def rand_fox(count):
    if 'user_id' not in session:
        return redirect('user/user_login.html')
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
        return redirect('user/user_login.html')
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
        return redirect('user/user_login.html')
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
        return redirect('user/user_login.html')
    url_1 = '/click/1/'
    url_2 = '/click/2/'
    return render_template('click.html',
                           url_1=url_1, url_2=url_2,
                           num_1=session['num_1'],
                           num_2=session['num_2'])


@app.route('/click/1/')
def click_1():
    if 'user_id' not in session:
        return redirect('user/user_login.html')
    session['num_1'] += 1
    return redirect('/click/')


@app.route('/click/2/')
def click_2():
    if 'user_id' not in session:
        return redirect('user/user_login.html')
    session['num_2'] += 1
    return redirect('/click/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
