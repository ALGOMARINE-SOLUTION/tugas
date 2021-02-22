from flask import Flask, request, render_template, Response, Blueprint
from heru import buat_windrose
from bangkit import diffusion_FTCS
from agri import OlahDataAdveksi1D

app = Blueprint('salmaa',__name__)

@app.route('/moduldifusi1d', methods=['GET', 'POST'])
def moduldifusi1d():
    if request.method == 'GET':
        return render_template('Difusi.html')

    if request.method == 'POST':
        dt = request.form['dt']
        dx = request.form['dx']
        T = request.form['T']
        L = request.form['L']
        Ad = request.form['Ad']
        F0 = request.form['F0']
        beh = diffusion_FTCS(float(dt), float(dx), float(T), float(L), float(Ad), float(F0))
        return render_template('Difusi.html', jeruk=str(beh))

@app.route('/windrose', methods=['GET', 'POST'])
def windrose():
    if request.method == 'GET':
        return render_template('Windrose.html')

    if request.method == 'POST':
        uploaded = request.files["heuh"]
        lokasi = request.form['lokasi']
        bln = request.form['bln']
        thn = request.form['thn']
        meh = buat_windrose(str(lokasi), str(bln), float(thn), uploaded)
        return render_template('Windrose.html', apel=str(meh))
    
@app.route('/modeladveksi1d', methods=['GET', 'POST'])
def modeladveksi1d():    
    if request.method == 'GET':
        return render_template('Adveksi.html')

    if request.method == 'POST':
        try:
            L = request.form['L']
            T = request.form['T']
            dt = request.form['dt']
            u = request.form['u']
            dx = request.form['dx']
            angkaindices0 = request.form['angkaindices0']
            angkaindices1 = request.form['angkaindices1']
            heuh = OlahDataAdveksi1D(float(L), float(T), float(dt), float(u), float(dx), float(angkaindices0), float(angkaindices1))
        except:
            return "punten kak ada masalah script"
        else:
            return render_template('Adveksi.html', naga=str(heuh))

        
if __name__ == '__main__':
    app.run()