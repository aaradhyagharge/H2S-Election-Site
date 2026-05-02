from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from config import Config
from database.models import db
import os

app = Flask(__name__, static_folder='.', static_url_path='')
app.config.from_object(Config)
CORS(app)

db.init_app(app)

# Register blueprints
from routes.auth import auth_bp
from routes.game import game_bp
from routes.chatbot import chatbot_bp
from routes.booth import booth_bp
from routes.news import news_bp
from routes.analytics import analytics_bp
from routes.parliament import parliament_bp
from routes.impact import impact_bp
from routes.support import support_bp
from routes.history import history_bp
from routes.glossary import glossary_bp

app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(booth_bp)
app.register_blueprint(news_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(parliament_bp)
app.register_blueprint(impact_bp)
app.register_blueprint(support_bp)
app.register_blueprint(history_bp)
app.register_blueprint(glossary_bp)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Operation Matdan API is running 🇮🇳"}), 200

@app.route('/api/countdown', methods=['GET'])
def countdown():
    from datetime import datetime
    target = datetime(2029, 5, 1)
    now    = datetime.utcnow()
    diff   = target - now
    total  = int(diff.total_seconds())
    if total < 0: total = 0
    return jsonify({
        "days":    total // 86400,
        "hours":   (total % 86400) // 3600,
        "minutes": (total % 3600) // 60,
        "seconds": total % 60
    })

@app.route('/translations/<path:filename>')
def serve_translations(filename):
    return send_from_directory('translations', filename)

# Serve HTML pages
@app.route('/')
@app.route('/index.html')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    if os.path.exists(os.path.join(app.static_folder, filename)):
        return send_from_directory('.', filename)
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Run seed if DB is empty
        try:
            from database.seed_data import seed_database
            seed_database()
        except Exception as e:
            print(f"Seed skipped: {e}")
    app.run(debug=True, port=5000, host='0.0.0.0')
