from flask import Flask, request, render_template, Response, Blueprint
from application.last import TSdiagram
from application.sst_2_wilayah import process1
from application.grafik_pasang_surut import process

app = Blueprint('farhan',__name__)

@app.route('/aksidiagramts', methods =['GET','POST'])
def novembermantap():
    if request.method == 'GET':
        return render_template ('index.html')
    if request.method == 'POST':
        desembersudahdekat = request.files['fileawal']
        lusaminggu = TSdiagram(desembersudahdekat)
        print(lusaminggu)
        return render_template ('halaman2.html', hasildiagramts = lusaminggu)

@app.route('/aksisst', methods =['POST'])
def besoksabtu():
    akupusingosfis = request.files['sst1']
    osfisituasik = request.files['sst2']
    marikitalibur = process1(akupusingosfis, osfisituasik)
    return render_template ('halaman2.html', hasilsst = marikitalibur)

@app.route('/aksipasut', methods = ['POST'])
def uassudahdekat():
    semoganilaibagus = request.files['pasut']
    aamiindeh = process(semoganilaibagus)
    return render_template ('halaman2.html', hasilpasut = aamiindeh)
    
if __name__ == "__main__":
    app.run()
