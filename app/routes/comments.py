from flask import Blueprint, request, jsonify
from app import db
from app.models import Comment

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/', methods=['GET'])
def get_comments():
    getCommets = Comment.query.all()
    return  jsonify([{
        'id': comments.id,
        'body': comments.body,
        'datePosted':comments.datePosted,
        'user_id': comments.user_id,
        'article_id': comments.article_id}
        for comments in getCommets])

@comments_bp.route('/new', methods=['POST'])
def create_comment():
    data = request.get_json()
    new_comment = Comment(body=data['body'], user_id=data['user_id'], article_id=data['article_id'])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'id':new_comment.id,
                    'body':new_comment.body,
                    'datePosted':new_comment.datePosted,
                    'user_id':new_comment.user_id,
                    'article_id':new_comment.article_id}), 201

@comments_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_users(id):
    comments = Comment.query.get(id)
    if not comments:
        return jsonify ({"error":"Comment not found"}), 404
    db.session.delete(comments)
    db.session.commit()
    return jsonify ({"Message":"Comment deleted successfully"}),200