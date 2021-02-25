from flask import Flask
from routing.home import app as home
from routing.farhan import app as farhan

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(farhan)

if __name__ == '__main__':
    app.run()