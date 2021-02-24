from flask import Flask
from routing.home import app as home

from routing.yoas import app as yoas

app = Flask(__name__)
app.register_blueprint(home)

app.register_blueprint(yoas)

if __name__ == '__main__':
    app.run()