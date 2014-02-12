from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
#from helpers import get_environment

#settings = get_environment()

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/')
def main():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)