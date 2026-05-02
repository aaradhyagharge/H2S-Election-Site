from flask import Blueprint, request, jsonify
from database.models import db, VoterSupportTicket

support_bp = Blueprint('support', __name__)

@support_bp.route('/api/support/ticket', methods=['POST'])
def create_ticket():
    data = request.json
    try:
        ticket = VoterSupportTicket(
            user_id=data.get('user_id'),
            full_name=data.get('full_name', 'Anonymous'),
            email=data.get('email', ''),
            phone=data.get('phone'),
            state=data.get('state'),
            issue_type=data.get('issue_type'),
            message=data.get('message', '')
        )
        db.session.add(ticket)
        db.session.commit()
        return jsonify({"message": "Ticket submitted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
