from flask import Flask, render_template# llamar al frameworck

app= Flask(__name__)# guarda en una variable la ruta de inicio de la app

#ruta de procesamiento




@app.route('/') # metodo que crea una url
def home():     #funcion que devuelve la informacion
    return render_template("home.html")#retornamos el archivo dentro de la carpeta templeate 

@app.route('/') # metodo que crea una url
def nav():     #funcion que devuelve la informacion
    return render_template("nav.html")#retornamos el archivo dentro de la carpeta templeate 

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/producto')
def producto():
    return render_template("producto.html")

@app.route('/') # metodo que crea una url
def ayuda():     #funcion que devuelve la informacion
    return render_template("ayuda.html")#retornamos el archivo dentro de la carpeta templeate 

@app.route('/put')
def put():
    return render_template("put.html")

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/delet')
def delet():
    return render_template("delet.html")

@app.route('/about')
def about():
    return render_template("about.html")


#validamos si estamos en el archivo principal para que siempre se quede
#escuchando una peticion del usuario y si se cumple ejecuta el app.run

if __name__=='__main__':
    app.run(debug=True ) #avisamos que estamos en un entorno de prueba 
                         #y se actualiza el servidor automaticamente
