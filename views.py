from run import app


@app.route('/')
def home():
    return '<h1>Servidor esta Arriba!</h1>'
