from flask import Blueprint, request, jsonify
from database.models import db, GameProgress, GameLeaderboard, QuizQuestion, Badge, UserBadge

game_bp = Blueprint('game', __name__)

@game_bp.route('/api/game/questions', methods=['GET'])
def get_questions():
    questions = QuizQuestion.query.all()
    q_list = []
    for q in questions:
        q_list.append({
            "id": q.question_id,
            "chapter": q.chapter_number,
            "text": {
                "en": q.question_text_english,
                "hi": q.question_text_hindi,
                "mr": q.question_text_marathi
            },
            "options": {
                "a": {"en": q.option_a_english, "hi": q.option_a_hindi, "mr": q.option_a_marathi},
                "b": {"en": q.option_b_english, "hi": q.option_b_hindi, "mr": q.option_b_marathi},
                "c": {"en": q.option_c_english, "hi": q.option_c_hindi, "mr": q.option_c_marathi}
            },
            "correct_option": q.correct_option,
            "explanation": {
                "en": q.explanation_english,
                "hi": q.explanation_hindi,
                "mr": q.explanation_marathi
            }
        })
    return jsonify(q_list), 200

@game_bp.route('/api/game/save', methods=['POST'])
def save_progress():
    data = request.json
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({"message": "Progress not saved for guest"}), 200
        
    try:
        progress = GameProgress(
            user_id=user_id,
            chapter_number=data.get('chapter', 1),
            score_earned=data.get('score', 0),
            language_played=data.get('language', 'en')
        )
        db.session.add(progress)
        
        # Update leaderboard
        leaderboard = GameLeaderboard.query.filter_by(user_id=user_id).first()
        if not leaderboard:
            leaderboard = GameLeaderboard(user_id=user_id, total_score=0)
            db.session.add(leaderboard)
            
        leaderboard.total_score += data.get('score', 0)
        
        # Simple badge check
        if progress.chapter_number == 1 and leaderboard.total_score >= 100:
            badge = Badge.query.filter_by(chapter_required=1).first()
            if badge:
                has_badge = UserBadge.query.filter_by(user_id=user_id, badge_id=badge.badge_id).first()
                if not has_badge:
                    db.session.add(UserBadge(user_id=user_id, badge_id=badge.badge_id))
                    
        db.session.commit()
        return jsonify({"message": "Progress saved"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@game_bp.route('/api/game/leaderboard', methods=['GET'])
def get_leaderboard():
    leaders = GameLeaderboard.query.order_by(GameLeaderboard.total_score.desc()).limit(10).all()
    # Need to join with User to get names, but keeping it simple for now
    result = []
    for l in leaders:
        result.append({
            "user_id": l.user_id,
            "score": l.total_score
        })
    return jsonify(result), 200
