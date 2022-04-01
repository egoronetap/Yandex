from flask import Flask

from data import db_session
from data.__all_models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sfvasefaf'

db_session.global_init("../db/blogs.db")
user = User()
user.name = "Пользователь 1"
user.about = "биография пользователя 1"
user.email = "email@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()


@app.route('/')
def index():
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
