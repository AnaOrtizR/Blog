from flask import Blueprint, request, jsonify
from app.models import db, User

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    try:
        list_users  = User.query.all()
        return jsonify([{'id': users.id,
                         'username': users.username,
                         'email': users.email,
                         'passwd': users.passwd
                         }
                         for users in list_users ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route('/new', methods=['POST'])
def new_user():
    data = request.get_json()
    new_user = User(
        username = data['username'],
        email = data['email'],
        passwd = ['passwd']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'passwd': new_user.passwd
    }), 201

@users_bp.route('/editUsername/<int:id>', methods=['PUT'])
def edit_Username(id):
    data = request.get_json()
    username = User.query.get(id)

    if not username:
        return jsonify ({'error': 'Username not found'}), 404
    
    if 'username' in data:
        username.username=data['username']

    db.session.commit()
    return jsonify({
        'id': username.id,
        'username': username.username,
        'email': username.email,
    }), 200

@users_bp.route('/editEmail/<int:id>', methods=['PUT'])
def edit_email(id):
    data = request.get_json()
    email = User.query.get(id)

    if not email:
        return jsonify ({'error': 'Email not found'}), 404
    
    if 'email' in data:
        email.email=data['email']

    db.session.commit()
    return jsonify({
        'id': email.id,
        'username': email.username,
        'email': email.email,
    }), 200

@users_bp.route('/editPasswd/<int:id>', methods=['PUT'])
def edit_passwd(id):
    data = request.get_json()
    passwd = User.query.get(id)

    if not passwd:
        return jsonify ({'error': 'Password not found'}), 404
    
    if 'passwd' in data:
        passwd.passwd=data['passwd']

    db.session.commit()
    return jsonify({
        'id': passwd.id,
        'username': passwd.username,
        'email': passwd.email,
        'passwd': passwd.passwd
    }), 200

@users_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_users(id):
    users = User.query.get(id)
    if not users:
        return jsonify ({"error":"User not found"}), 404
    db.session.delete(users)
    db.session.commit()
    return jsonify ({"Message":"User deleted successfully"}),200



   