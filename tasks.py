import os

from invoke import task, run
from csscompressor import compress as css_minify
from slimit import minify as js_minify


@task
def build():
    for filename in os.listdir('duchess/assets/css'):
        if filename.endswith('.sass') and not filename.startswith('_'):
            sass_file_path = os.path.join('duchess/assets/css/', filename)
            css_file_path = sass_file_path + '.css'

            run('isass %s --output %s' % (sass_file_path, css_file_path))

    for filename in os.listdir('duchess/assets/css'):
        if filename.endswith('.sass.css'):
            css_file_path = os.path.join('duchess/assets/css/', filename)
            min_css_file_path = css_file_path.replace('.sass.css', '.min.css')
            with open(css_file_path) as css_file:
                with open(min_css_file_path, 'w') as min_css_file:
                    min_css_file.write(css_minify(css_file.read()))
            os.remove(css_file_path)

    for filename in os.listdir('duchess/assets/js'):
        if filename.endswith('.js') and '.min.js' not in filename:
            js_file_path = os.path.join('duchess/assets/js/', filename)
            min_js_file_path = js_file_path.replace('.js', '.min.js')
            js_file = open(js_file_path)
            min_js_file = open(min_js_file_path, 'w')

            min_js_file.write(
                js_minify(js_file.read(), mangle=True, mangle_toplevel=True)
            )


@task(pre=[build])
def start():  # nocov
    run('./run.py')


@task(pre=[build])
def test():  # nocov
    run('export DUCHESS_ENV=Testing; nosetests test.py --with-coverage')
