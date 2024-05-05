from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint

# Cargamos los datos
conexion = sqlite3.connect("web2.sqlite3")
# Guarda la información en un diccionario
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()
cursor.execute("""
SELECT * FROM productos;
""")
productos = [producto for producto in cursor.fetchall()]
cursor.close()
conexion.close()

# aplicacion

app = Flask(__name__)

# rustas
@app.route('/')
def ruta_raiz():
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
   for producto in productos:
      if pid == producto['id']:
         return render_template('producto.html', producto=producto)
   return redirect('/')
         
# Programa principal
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)