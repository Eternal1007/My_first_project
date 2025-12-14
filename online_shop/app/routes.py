from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product
#render_template використовується для рендерингу HTML-шаблонів  

bp=Blueprint('routes', __name__)
#main - назва блупринта, __name__ - ім'я поточного модуля

@bp.route('/')
def index():
    return render_template('index.html')
#@bp.route('/') - визначає маршрут для головної сторінки
#Функція index() рендерить шаблон index.html при доступі до головної сторінки
#return render_template('index.html') - повертає відрендерений HTML-шаблон index.html

@bp.route('/products')
def product():
    products = Product.query.all()
    return render_template('product_list.html',
                           products=products)
    
    
@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name=request.form['name']
        price=request.form['price']
        description=request.form['description']
        stock=request.form['stock']
        is_active=request.form.get('is_active') == 'on'
        category=request.form['category']
        rating=request.form['rating']
        sale=request.form.get('sale') ==  'on'
        product=Product(name=name, price=float(price))
        db.session.add(product)
        db.session.commit()
        flash('Product added')
        return redirect(url_for('routes.product'))
    return render_template('product_form.html', action='Add', product=None)