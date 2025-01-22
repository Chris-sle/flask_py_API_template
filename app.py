from flask import Flask
from routes.users import users as users_blueprint
from routes.products import products as products_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(products_blueprint, url_prefix='/products')

@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
