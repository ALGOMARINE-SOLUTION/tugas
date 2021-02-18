from flask import Flask
from routing.home import app as home

app = Flask(__name__)
app.register_blueprint(home)

if __name__ == '__main__':
    app.run()