from flask import Flask, render_template
from flask.json import dumps
from werkzeug.contrib.fixers import ProxyFix
from data.models import get_page

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['DEBUG'] = True


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/page/<int:page>')
def show_page(page):
    return dumps(get_page(page))

if __name__ == '__main__':
    app.run(debug=True)

