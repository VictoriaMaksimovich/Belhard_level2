from flask import Flask, render_template
from get_info import *
import re

'''
Написать веб-приложение на Flask со след ендпоинтами:
    - главная страница
    - /duck/ - отображает заголовок рандомная утка №ххх и картинка утки 
                которую получает по API https://random-d.uk/

    - /fox/<int>/ - аналогично утке только с лисой (- https://randomfox.ca), 
                    но количество разных картинок определено int. 
                    если int больше 10 или меньше 1 - вывести сообщение об ошибке

    - /weather-minsk/ - показывает погоду в минске

    - /weather/<city>/ - показывает погоду в городе указанного в city

    - по желанию добавить еще один ендпоинт на любую тему 


Добавить обработчик ошибки 404. (есть в example)


'''

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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


@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'


if __name__ == "__main__":
    app.run(port=8000)
