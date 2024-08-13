from flask import Blueprint, request, jsonify
from app.models import db, Article
from datetime import datetime, timezone

articles_bp = Blueprint('articles_bp', __name__)

@articles_bp.route('/', methods=['GET'])
def get_articles():
    listArticles = Article.query.all()
    return jsonify([{'id':article.id,
                     'artTitle':article.artTitle,
                     'artContent':article.artContent,
                     'artDatePosted': article.artDatePosted,
                     'artDateUpdate':article.artDateUpdate,
                     'user_id':article.user_id,
                     'category_id':article.category_id}
                     for article in listArticles])

@articles_bp.route('/new', methods=['POST'])
def create_article():
    data = request.get_json()
    current_time = datetime.now(timezone.utc)
    new_article = Article(
        artTitle=data['artTitle'],
        artContent=data['artContent'],
        artDatePosted=current_time,
        artDateUpdate=current_time,
        user_id=data['user_id'],
        category_id=data['category_id']
    )
    db.session.add(new_article)
    db.session.commit()
    return jsonify({
        'id': new_article.id,
        'artTitle': new_article.artTitle,
        'artContent':new_article.artContent,
        'artDatePosted': new_article.artDatePosted,
        'artDateUpdate': new_article.artDateUpdate,
        'user_id': new_article.user_id,
        'category_id': new_article.category_id
    }), 201

@articles_bp.route('/editArticle/<int:id>', methods=['PUT'])
def edit_Article(id):
    data = request.get_json()
    article = Article.query.get(id)

    if not article:
        return jsonify ({'error': 'Article not found'}), 404
    
    if 'artTitle' in data:
        article.artTitle=data['artTitle']
    if 'artContent' in data:
        article.artContent=data['artContent']
    
    article.artDateUpdate = datetime.now(timezone.utc)

    db.session.commit()
    return jsonify({
        'id': article.id,
        'artTitle': article.artTitle,
        'artContent':article.artContent,
        'artDatePosted': article.artDatePosted,
        'artDateUpdate': article.artDateUpdate,
        'user_id': article.user_id,
        'category_id': article.category_id
    }), 200

@articles_bp.route('/searchByWord', methods=['POST'])
def search_Article():
    data = request.get_json()
    if 'word' in data:
        palabra_like = f"%{data['word']}%"
        articles = Article.query.filter(Article.artTitle.like(palabra_like)).all()
        
        if articles:
            results = []
            for article in articles:
                results.append({
                    'id': article.id,
                    'artTitle': article.artTitle,
                    'artContent': article.artContent,
                    'artDatePosted': article.artDatePosted,
                    'artDateUpdate': article.artDateUpdate,
                    'user_id': article.user_id,
                    'category_id': article.category_id
                })
            return jsonify(results), 200
        else:
            return jsonify({"message": "No hay coincidencias"}), 404
    return jsonify({"message": "No se proporcionó una palabra"}), 400

@articles_bp.route('/searchByCategory', methods=['POST'])
def searchCatArticle():
    data = request.get_json()
    if 'word' in data:
        palabra_like = f"%{data['word']}%"
        if 'artCategory' in data:
            category_like =f"%{data['artCategory']}%"
            articles = Article.query.filter(
                Article.artTitle.like(palabra_like), 
                Article.category_id.like(category_like)
                ).all()

            if articles:
                results = []
                for article in articles:
                    results.append({
                        'id': article.id,
                        'artTitle': article.artTitle,
                        'artContent': article.artContent,
                        'artDatePosted': article.artDatePosted,
                        'artDateUpdate': article.artDateUpdate,
                        'user_id': article.user_id,
                        'category_id': article.category_id
                    })
                return jsonify(results), 200
            else:
                return jsonify({"message": "No hay coincidencias"}), 404
        return jsonify({"message":"No se proporcionó una categoría"}),400
    return jsonify({"message": "No se proporcionó una palabra"}), 400
