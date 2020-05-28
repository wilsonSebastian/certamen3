from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'DESKTOP-A9IUIUM'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Ventas'
mysql = MySQL(app)

app.secret_key = "mysecretkey"


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pedido')
    data = cur.fetchall()
    cur.close()
    return render_template('Index.html', pedido = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        contacto = request.form['contacto']
        pago = request.form['pago']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pedido (Nombre, Apellido, Direccion, Contacto, Pago) VALUES (%s,%s,%s)", (nombre, apellido, direccion, contacto, pago))
        mysql.connection.commit()
        flash('Pedido realizado con extio!!')
        return redirect(url_for('exito'))  


@app.route('/exito')
def exito():
    return render_template('Success.html')


    


if __name__ == "__main__":
    app.run(port=3000, debug=True)