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


@bp.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted!')
    return redirect(url_for('routes.product'))

@bp.route('/update/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.description=request.form['description']
        product.stock=request.form['stock']
        product.is_active=request.form.get('is_active') == 'on'
        product.category=request.form['category']
        product.rating=request.form['rating']
        product.sale=request.form.get('sale') ==  'on'
        
        print (f'''name={product.name}, price={product.price}, description={product.description}''',)
        
        db.session.commit()
        flash('Product updated!')
        return redirect(url_for('routes.product'))
    return render_template('product_form.html', action='Update', product=product)