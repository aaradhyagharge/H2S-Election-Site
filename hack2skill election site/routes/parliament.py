from flask import Blueprint, jsonify
from database.models import ParliamentMember, PoliticalParty

parliament_bp = Blueprint('parliament', __name__)

@parliament_bp.route('/api/parliament/parties', methods=['GET'])
def get_parties():
    parties = PoliticalParty.query.all()
    result = []
    for p in parties:
        result.append({
            "id": p.party_id,
            "name": p.party_name,
            "abbreviation": p.party_abbreviation,
            "founded_year": p.founded_year
        })
    return jsonify(result), 200

@parliament_bp.route('/api/parliament/members', methods=['GET'])
def get_members():
    # In a real app, you would add pagination and filtering
    members = ParliamentMember.query.limit(20).all()
    result = []
    for m in members:
        result.append({
            "id": m.member_id,
            "name": m.full_name,
            "party": m.party_name,
            "constituency": m.constituency
        })
    return jsonify(result), 200
