from flask import Blueprint, render_template
#render_template використовується для рендерингу HTML-шаблонів  

bp=Blueprint('main', __name__)
#main - назва блупринта, __name__ - ім'я поточного модуля

@bp.route('/')
def index():
    return render_template('index.html')
#@bp.route('/') - визначає маршрут для головної сторінки
#Функція index() рендерить шаблон index.html при доступі до головної сторінки
#return render_template('index.html') - повертає відрендерений HTML-шаблон index.html