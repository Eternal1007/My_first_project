from app import create_app
from app.models import db
from flask import Flask
import os 

app = create_app()

if __name__ == '__main__':
    #Create DB tables if not exist.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    #if __name__ == '__main__': - перевіряє, чи запускається скрипт безпосередньо
    #with app.app_context(): - створює контекст додатка для роботи з базою даних
    #db.create_all() - створює всі таблиці в базі даних, визначені моделями SQLAlchemy
    #app.run(debug=True) - запускає Flask-додаток у режимі налагодження