from flask import Blueprint, jsonify
from database.models import ElectionHistory

history_bp = Blueprint('history', __name__)

@history_bp.route('/api/history', methods=['GET'])
def get_history():
    history = ElectionHistory.query.order_by(ElectionHistory.year.asc()).all()
    result = []
    for h in history:
        result.append({
            "year": h.year,
            "name": h.election_name,
            "winning_party": h.winning_party,
            "prime_minister": h.prime_minister_elected,
            "events": h.notable_events
        })
    return jsonify(result), 200
