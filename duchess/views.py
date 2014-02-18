from flask import render_template
from duchess import duchess


def init_views():
    @duchess.route('/')
    def index():
        return render_template('index.html')
