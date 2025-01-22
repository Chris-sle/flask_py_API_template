from flask import Blueprint, jsonify

products = Blueprint('products', __name__)

@products.route('/', methods=['GET'])
def get_products():
    return jsonify({"products": ["product1", "product2", "product3"]})