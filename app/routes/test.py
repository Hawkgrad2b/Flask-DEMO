from flask import Blueprint, jsonify

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/')
def hello():
    return jsonify({'message': 'It works!'})
