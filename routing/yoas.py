from flask import Flask, request, render_template, Response, Blueprint
from application.hidrodinamika1d import OlahDataHD1D
from application.PetaBatimetri import semangat

app = Blueprint('yoas',__name__)

    
@app.route('/tim6batimetri', methods = ["GET","POST"])
def halamanterus():
    if request.method == "GET":
        return render_template ('Tugas_MarthinYoas.html')

    if request.method == 'POST':
        semongko = request.files['boongbanget']
        nanas = semangat(semongko)
        return render_template ('Tugas_MarthinYoas.html', boongbeneran= str(nanas))

@app.route('/tim6hidro', methods = ["GET", "POST"])
def halamanlagi():
    if request.method == "GET":
        return render_template ('Tugas_MarthinYoas.html')

    if request.method == 'POST':
        try:
            p = request.form['p']
            T = request.form['T']
            A = request.form['A']
            D = request.form['D']
            dt = request.form['dt']
            To = request.form['To']
            dx = request.form['dx']
            indices0 = request.form['1']
            indices1 = request.form['2']
            gilacuy = OlahDataHD1D(int(p), int(T), int(A), int(D), int(dt), int(To), int(dx), int(1), int(2))
        except:
            return "maaf script bermasalah"
        else:
            return render_template('Tugas_MarthinYoas.html', boonglagi= str(gilacuy))

if __name__ == '__main__':
    app.run()