from flask import Blueprint, render_template

address = Blueprint('address', __name__)

@address.route('/')
def index():
    return render_template('index.html')
