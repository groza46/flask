from flask import Flask, render_template,redirect,request
from tinydb import TinyDB
import datetime

app = Flask(__name__)
baza = TinyDB('db.json')


@app.route("/")
def zacentnaStran():
    return render_template('home.html')

@app.route("/zbirka")
def zbirka():
    igralci = baza.all()
    return render_template('zbirka.html',igralci=igralci)

@app.route("/dodaj_igralca", methods=['GET','POST'])
def dodajanje():
   if request.method == 'POST':
       ime = request.form['ime']
       priimek = request.form['priimek']
       pozicija = request.form['pozicija']

       dan_rojstva = request.form['dan_rojstva']
       mesec_rojstva = request.form['mesec_rojstva']
       leto_rojstva = request.form['leto_rojstva']

       rojstni_datum = f"{dan_rojstva}-{mesec_rojstva}-{leto_rojstva}"

       goli = int(request.form['goli'])
       asistence = int(request.form['asistence'])

       tocke = goli + asistence

       plus_minus = int(request.form['plus_minus'])
       kazenske_minute = int(request.form['kazenske_minute'])

       baza.insert({
           'ime': ime,
           'priimek': priimek,
           'pozicija': pozicija,
           'rojstni_datum': rojstni_datum,
           'goli': goli,
           'asistence': asistence,
           'tocke': tocke,
           'plus_minus': plus_minus,
           'kazenske_minute': kazenske_minute
       })
       return redirect("/zbirka")
   return render_template("dodaj_igralca.html") 


if __name__ == "__main__":
    app.run(debug=True)