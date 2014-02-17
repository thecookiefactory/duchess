from flask import render_template
from duchess import duchess

@duchess.route('/')
def index():
    return render_template('index.html')
