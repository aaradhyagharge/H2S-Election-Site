from flask import Blueprint, jsonify
from database.models import ImpactVisualizerData

impact_bp = Blueprint('impact', __name__)

@impact_bp.route('/api/impact/data', methods=['GET'])
def get_impact_data():
    data = ImpactVisualizerData.query.all()
    result = []
    for d in data:
        result.append({
            "year": d.election_year,
            "constituency": d.constituency_name,
            "state": d.state,
            "margin": d.winning_margin,
            "story": d.impact_story
        })
    return jsonify(result), 200
