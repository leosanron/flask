from flask import Flask , request , make_response , redirect, render_template

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
todos = ["escribir","sacar al perro","programar","TODO3","TODO3","TODO3"]

@app.errorhandler(404)
def not_found(error): 
    return render_template("404.html", error=error)



@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)
    return response


# Definir una ruta para la página principal
@app.route('/hello')
def hello_world():

    user_ip = request.cookies.get("user_ip")
    context = {
        "user_ip" : user_ip,
        "todos" : todos,
    }

    return render_template("hello.html", context=context )

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)