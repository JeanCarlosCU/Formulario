from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html', creador="Ceniceros Uribe Jean Carlos")

@app.route('/animales')
def animales():
    return render_template('Animales_E.html', creador="Ceniceros Uribe Jean Carlos")

@app.route('/vehiculos')
def vehiculos():
    return render_template('Vehiculos_A.html', creador="Ceniceros Uribe Jean Carlos")

@app.route('/maravillas')
def maravillas():
    return render_template('LMM.html', creador="Ceniceros Uribe Jean Carlos")

@app.route('/gustos')
def gustos():
    return render_template('LoQueMeGusta.html', creador="Ceniceros Uribe Jean Carlos")

@app.route('/crear_cuenta')
def creacion_de_cuenta():
    return render_template('crear_cuenta.html', creador="Ceniceros Uribe Jean Carlos")

@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('inicio_de_sesion.html', creador="Ceniceros Uribe Jean Carlos")

if __name__ == "__main__":
    app.run(debug=True)
