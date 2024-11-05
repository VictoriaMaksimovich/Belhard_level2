from flask import Flask, render_template, url_for, session, request, redirect
from get_info import *
import re
import os


BASE_FOLDER = os.getcwd()


app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, 'static'),
            template_folder=os.path.join(BASE_FOLDER, 'templates'))

app.config['SECRET_KEY'] = 'jhv;cd59-687fh;fd-1713erd!!r;gh-o8yh;gh:vjh-!-g67r:ff'


@app.route('/')
def index():
    session['num_1'] = 0
    session['num_2'] = 0
    return render_template('index.html')


@app.route('/form/')
def log_form():
    render_template('form.html')


@app.route('/duck/')
def rand_duck():
    duck = get_duck()
    duck_numb = re.findall(r'\d+', duck)
    duck_numb = [int(i) for i in duck_numb]
    return render_template('duck.html', img=duck, numb=duck_numb)


@app.route('/fox/<int:count>/')
def rand_fox(count):
    if 1 <= count <= 10:
        fox_url = []
        fox_numb = ''
        for i in range(count):
            fox = get_fox()
            fox_n = re.findall(r'\d+', fox)
            fox_n = str(fox_n[0])
            fox_url.append(fox)
            fox_numb = fox_numb + ' * ' + fox_n
        return render_template('fox.html', img=fox_url, numb=fox_numb)
    else:
        return '<h1 style="color:red">такой страницы не существует</h1>'


@app.route('/weather-minsk/')
def weather_minsk():
    city_m = 'Minsk'
    we_minsk = get_weather(city_m)
    weather_m = (f'Небо {we_minsk['weather'][0]['description']}, '
                 f'температура(K) {we_minsk['main']['temp']}, '
                 f'давление(кПа) {we_minsk['main']['pressure']}, '
                 f'влажность воздуха(%) {we_minsk['main']['humidity']}')
    return render_template('weather.html', city_m=city_m, weather_m=weather_m)


@app.route('/weather/<city>/')
def weather_city(city):
    city = city.capitalize()
    we_city = get_weather(city)
    weather = (f'Небо {we_city['weather'][0]['description']}, '
               f'температура(K) {we_city['main']['temp']}, '
               f'давление(кПа) {we_city['main']['pressure']}, '
               f'влажность воздуха(%) {we_city['main']['humidity']}')
    return render_template('weather_city.html', city=city, weather=weather)


@app.route('/click/')
def click_picture():
    url_1 = '/click/1/'
    url_2 = '/click/2/'
    return render_template('click.html', url_1=url_1, url_2=url_2, num_1=num_1, num_2=num_2)


@app.route('/click/1/')
def click_1():
    session['num_1'] += 1
    return redirect('/click/')


@app.route('/click/2/')
def click_2():
    session['num_2'] += 1
    return redirect('/click/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(port=8000)
