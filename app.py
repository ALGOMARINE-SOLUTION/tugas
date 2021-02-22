from flask import Flask
from routing.home import app as home
from routing.salmaa import app as salmaa

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(salmaa)

if __name__ == '__main__':
    app.run()