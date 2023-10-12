import psycopg2
from flask import Flask, render_template

app = Flask('workapp')

@app.route("/workapp")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Candidati/')
def show_Candidati():
    return render_template('Candidati.html')

@app.route('/Companii/')
def show_Companii():
    return render_template('Companii.html')

@app.route('/Contact/')
def show_Contact():
    return render_template('Contact.html')

@app.route('/HRWORKPOWER/')
def show_HRWORKPOWER():
    return render_template('HRWORKPOWER.html')

@app.route('/OfertadeLucru/')
def show_OfertadeLucru():
    return render_template('OfertadeLucru.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
