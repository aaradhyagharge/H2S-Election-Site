from flask import Blueprint, jsonify
from database.models import NewsArticle

news_bp = Blueprint('news', __name__)

@news_bp.route('/api/news', methods=['GET'])
def get_news():
    news = NewsArticle.query.limit(10).all()
    result = []
    for n in news:
        result.append({
            "id": n.article_id,
            "headline": {
                "en": n.headline_english,
                "hi": n.headline_hindi,
                "mr": n.headline_marathi
            },
            "summary": n.summary,
            "source": n.source_name,
            "url": n.source_url
        })
    return jsonify(result), 200
