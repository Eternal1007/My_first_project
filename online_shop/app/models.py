from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#db = SQLAlchemy() - створює екземпляр SQLAlchemy для роботи з базою даних

class Product(db.Model):
#class Product(db.Model): - визначає модель Product для таблиці "products"
    __tablename__ = "products"
#__tablename__ = "products" - вказує назву таблиці в базі даних
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
#id=db.Column(db.Integer, primary_key=True, autoincrement=True) - визначає стовпець id як ціле число, первинний ключ з автоінкрементом
    name=db.Column(db.String(100), nullable=False)
#name=db.Column(db.String(100), nullable=False) - визначає стовпець name як рядок довжиною до 100 символів, не може бути порожнім
    price=db.Column(db.Float, nullable=False)
#price=db.Column(db.Float, nullable=False) - визначає стовпець price як число з плаваючою комою, не може бути порожнім