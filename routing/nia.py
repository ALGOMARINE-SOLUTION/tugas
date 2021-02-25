from flask import Flask, request, render_template, Response, Blueprint
from application.rachel6 import process
from flask.helpers import send_file

app = Blueprint('nia',__name__)

@app.route('/excel_pengolahan')
def file_():
    temp = "static/untukalgo.xlsx"
    return send_file(temp, as_attachment=True)

@app.route('/niapatrick', methods=['POST', 'GET'])
def proyek():
    if request.method == 'GET':
        return render_template('tugas_patricknia2.html')
    if request.method == 'POST':
        grafik =request.files['inputkedalaman']
        tampilan = process((grafik))
        return render_template('tugas_patricknia2.html', datasuhu=str(tampilan))

@app.route('/martabak', methods=['POST', 'GET'])
def semangka():
    if request.method == 'GET':
        return render_template('tugas_patricknia1.html')

if __name__=="__main__":
    app.run()

