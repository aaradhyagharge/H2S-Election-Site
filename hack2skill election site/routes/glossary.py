from flask import Blueprint, jsonify
from database.models import GlossaryTerm

glossary_bp = Blueprint('glossary', __name__)

@glossary_bp.route('/api/glossary', methods=['GET'])
def get_glossary():
    terms = GlossaryTerm.query.order_by(GlossaryTerm.term_english.asc()).all()
    result = []
    for t in terms:
        result.append({
            "term": {
                "en": t.term_english,
                "hi": t.term_hindi,
                "mr": t.term_marathi
            },
            "definition": {
                "en": t.definition_english,
                "hi": t.definition_hindi,
                "mr": t.definition_marathi
            },
            "category": t.category
        })
    return jsonify(result), 200
