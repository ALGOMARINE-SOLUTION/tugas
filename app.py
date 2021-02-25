from flask import Flask
from routing.home import app as home
from routing.salmaa import app as salmaa
from routing.yoas import app as yoas
from routing.nia import app as nia
from routing.farhan import app as farhan

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(salmaa)
app.register_blueprint(yoas)
app.register_blueprint(nia)
app.register_blueprint(farhan)

if __name__ == '__main__':
    app.run()