from flask import Blueprint, request, jsonify
from database.models import db, ChatbotHistory
from utils.nlp_matcher import find_chatbot_response
from utils.translator import get_language_code

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/api/chatbot', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    user_id = data.get('user_id') # Can be null for guests
    session_id = data.get('session_id', 'guest_session')
    lang_str = data.get('language', 'en')
    
    lang_code = get_language_code(lang_str)
    
    # 1. Get response using NLP matcher
    bot_response = find_chatbot_response(user_message, lang=lang_code)
    
    # 2. Save history
    try:
        history_entry = ChatbotHistory(
            user_id=user_id,
            session_identifier=session_id,
            user_message=user_message,
            bot_response=bot_response,
            language_detected=lang_code,
            topic_category="general" # Could be extracted from NLP
        )
        db.session.add(history_entry)
        db.session.commit()
    except Exception as e:
        print(f"Error saving chatbot history: {e}")
        # Continue even if history saving fails
        
    return jsonify({
        "response": bot_response,
        "language": lang_code
    }), 200
