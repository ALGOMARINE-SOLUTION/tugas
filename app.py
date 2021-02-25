from flask import Flask
from routing.home import app as home
<<<<<<< HEAD
from routing.farhan import app as farhan

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(farhan)
=======

from routing.yoas import app as yoas

app = Flask(__name__)
app.register_blueprint(home)

app.register_blueprint(yoas)
>>>>>>> 7cf20f264a1585597ca90af5bef621ec91d8aeab

if __name__ == '__main__':
    app.run()