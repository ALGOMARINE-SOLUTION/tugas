from flask import Flask

app = Flask(__name__)

@app.route('/')
def halamanUtama():
    return "Selamat Datang di Halaman Utama"

if __name__ == '__main__':
    app.run()