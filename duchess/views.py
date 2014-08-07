from flask import render_template, current_app
from uuid import uuid4

def init_views(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/admin')
    def admin_panel():
        return render_template('admin/home.html')

    @app.route('/admin/slides')
    def slides_admin():
        slide_keys = {
            key.split(':')[1]
            for key in current_app.redis.keys('slide:*')
        }

        slides = (
            {
                'id': key,
                'text': current_app.redis.get('slide:' + key + ':text'),
                'image': current_app.redis.get('slide:' + key + ':image'),
            }
            for key in slide_keys
        )

        return render_template('admin/slides.html', slides=slides, random_id=str(uuid4())[4:13])
