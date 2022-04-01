from flask import Flask

from datetime import datetime

from data import db_session
from data.__all_models import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sfvasefaf'

db_session.global_init("db/users.db")
job = Jobs()

job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.start_date = datetime.now()
job.is_finished = False

db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()


# @app.route('/')
# def index():
#     db_sess = db_session.create_session()
#     user = db_sess.query(User).all()
