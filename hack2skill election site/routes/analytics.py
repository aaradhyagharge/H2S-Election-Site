from flask import Blueprint, jsonify
from database.models import StateElectionData

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/api/analytics/states', methods=['GET'])
def get_state_analytics():
    data = StateElectionData.query.all()
    result = []
    for d in data:
        result.append({
            "state": d.state_name,
            "turnout": d.voter_turnout_percentage,
            "male_voters": d.total_male_voters,
            "female_voters": d.total_female_voters
        })
    return jsonify(result), 200
