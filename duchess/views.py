from flask import render_template


def init_views():
    from duchess import duchess

    @duchess.route('/')
    def index():
        return render_template('index.html')
