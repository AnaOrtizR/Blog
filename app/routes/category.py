from flask import Blueprint, request, jsonify
from app.models import db, Category


categories_bp = Blueprint('categories_bp', __name__)

@categories_bp.route('/', methods=['GET'])
def get_category():
    categories  = Category.query.all()
    return jsonify([{'id':category.id,
                     'category':category.category
                     }
                     for category in categories ])

@categories_bp.route('/new', methods=['POST'])
def new_category():
    data = request.get_json()
    new_category = Category(
        category=data['category']
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({
        'id': new_category.id,
        'category': new_category.category
    }), 201