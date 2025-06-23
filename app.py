from flask import Flask
from routes.ong_routes import ong_bp
from routes.doacao_routes import doacao_bp

app = Flask(__name__)
app.register_blueprint(ong_bp)
app.register_blueprint(doacao_bp)

@app.route('/')
def home():
    return 'API Green Save funcionando!'

if __name__ == '__main__':
    app.run(debug=True)
