from app import app
from flask import render_template
from app.forms import user_info_form
from app.models import Entry
from app import db

@app.route('/') #when the browswer goes to / it will execute this function
def index():
    title = 'Home'
    return render_template('index.html', title=title)