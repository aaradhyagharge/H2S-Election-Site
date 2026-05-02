from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    password_hash = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(100))
    epic_number = db.Column(db.String(100)) # Encrypted ideally
    language_preference = db.Column(db.String(50), default='english')
    profile_picture_url = db.Column(db.String(500))
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

class UserSession(db.Model):
    __tablename__ = 'user_sessions'
    session_id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    token = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    ip_address = db.Column(db.String(50))
    device_info = db.Column(db.String(255))

class GameProgress(db.Model):
    __tablename__ = 'game_progress'
    progress_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    chapter_number = db.Column(db.Integer, nullable=False)
    chapter_name = db.Column(db.String(255))
    is_completed = db.Column(db.Boolean, default=False)
    score_earned = db.Column(db.Integer, default=0)
    choices_made = db.Column(db.Text) # JSON string
    time_taken = db.Column(db.Integer) # in seconds
    language_played = db.Column(db.String(50))
    completed_at = db.Column(db.DateTime)

class GameLeaderboard(db.Model):
    __tablename__ = 'game_leaderboard'
    leaderboard_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_score = db.Column(db.Integer, default=0)
    chapters_completed = db.Column(db.Integer, default=0)
    badges_earned = db.Column(db.Text) # JSON array
    state = db.Column(db.String(100))
    rank = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Badge(db.Model):
    __tablename__ = 'badges'
    badge_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    badge_name_en = db.Column(db.String(255), nullable=False)
    badge_name_hi = db.Column(db.String(255))
    badge_name_mr = db.Column(db.String(255))
    badge_description = db.Column(db.Text)
    badge_icon_url = db.Column(db.String(500))
    points_required = db.Column(db.Integer, default=0)
    chapter_required = db.Column(db.Integer)

class UserBadge(db.Model):
    __tablename__ = 'user_badges'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.badge_id'), nullable=False)
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)

class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chapter_number = db.Column(db.Integer, nullable=False)
    question_text_english = db.Column(db.Text, nullable=False)
    question_text_hindi = db.Column(db.Text)
    question_text_marathi = db.Column(db.Text)
    option_a_english = db.Column(db.String(255))
    option_a_hindi = db.Column(db.String(255))
    option_a_marathi = db.Column(db.String(255))
    option_b_english = db.Column(db.String(255))
    option_b_hindi = db.Column(db.String(255))
    option_b_marathi = db.Column(db.String(255))
    option_c_english = db.Column(db.String(255))
    option_c_hindi = db.Column(db.String(255))
    option_c_marathi = db.Column(db.String(255))
    correct_option = db.Column(db.String(1), nullable=False) # 'a', 'b', or 'c'
    explanation_english = db.Column(db.Text)
    explanation_hindi = db.Column(db.Text)
    explanation_marathi = db.Column(db.Text)
    context_story_english = db.Column(db.Text)
    context_story_hindi = db.Column(db.Text)
    context_story_marathi = db.Column(db.Text)
    points_value = db.Column(db.Integer, default=100)
    difficulty_level = db.Column(db.String(50))

class PollingBooth(db.Model):
    __tablename__ = 'polling_booths'
    booth_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booth_number = db.Column(db.String(100), nullable=False)
    booth_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text)
    pincode = db.Column(db.String(20))
    district = db.Column(db.String(100))
    state = db.Column(db.String(100))
    assembly_constituency = db.Column(db.String(255))
    parliamentary_constituency = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    blo_name = db.Column(db.String(255))
    blo_contact = db.Column(db.String(100))
    has_wheelchair_access = db.Column(db.Boolean, default=False)
    has_water_facility = db.Column(db.Boolean, default=False)
    has_shade_facility = db.Column(db.Boolean, default=False)
    total_registered_voters = db.Column(db.Integer)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class ParliamentMember(db.Model):
    __tablename__ = 'parliament_members'
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(255), nullable=False)
    member_type = db.Column(db.String(50)) # MP / MLA
    house = db.Column(db.String(100)) # Lok Sabha / Rajya Sabha / State Assembly
    party_name = db.Column(db.String(255))
    constituency = db.Column(db.String(255))
    state = db.Column(db.String(100))
    profile_photo_url = db.Column(db.String(500))
    education_qualification = db.Column(db.String(255))
    date_of_birth = db.Column(db.Date)
    contact_office = db.Column(db.String(255))
    official_email = db.Column(db.String(255))
    term_start_date = db.Column(db.Date)
    term_end_date = db.Column(db.Date)
    is_current_member = db.Column(db.Boolean, default=True)
    total_terms_served = db.Column(db.Integer)
    committee_memberships = db.Column(db.Text) # JSON array
    notable_contributions = db.Column(db.Text)
    asset_declaration_link = db.Column(db.String(500))
    criminal_record_count = db.Column(db.Integer, default=0)
    source_url = db.Column(db.String(500))

class PoliticalParty(db.Model):
    __tablename__ = 'political_parties'
    party_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    party_name = db.Column(db.String(255), nullable=False)
    party_abbreviation = db.Column(db.String(50))
    party_symbol = db.Column(db.String(100))
    party_symbol_image_url = db.Column(db.String(500))
    founded_year = db.Column(db.Integer)
    headquarters = db.Column(db.String(500))
    national_or_state = db.Column(db.String(50)) # national / state
    election_commission_registration_number = db.Column(db.String(100))
    party_president = db.Column(db.String(255))
    ideology = db.Column(db.Text)
    official_website = db.Column(db.String(500))
    total_lok_sabha_seats_current = db.Column(db.Integer, default=0)
    total_rajya_sabha_seats_current = db.Column(db.Integer, default=0)
    alliance_name = db.Column(db.String(100)) # NDA / UPA / others / none
    recognized_states = db.Column(db.Text) # JSON array

class ElectionHistory(db.Model):
    __tablename__ = 'election_history'
    election_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    election_name = db.Column(db.String(255), nullable=False)
    election_type = db.Column(db.String(100)) # General / State / By-election
    year = db.Column(db.Integer)
    election_date_start = db.Column(db.Date)
    election_date_end = db.Column(db.Date)
    total_constituencies = db.Column(db.Integer)
    total_votes_cast = db.Column(db.Integer)
    total_registered_voters = db.Column(db.Integer)
    voter_turnout_percentage = db.Column(db.Float)
    winning_party = db.Column(db.String(255))
    winning_alliance = db.Column(db.String(100))
    seats_won_by_winner = db.Column(db.Integer)
    total_seats = db.Column(db.Integer)
    prime_minister_elected = db.Column(db.String(255))
    notable_events = db.Column(db.Text)
    result_summary = db.Column(db.Text)
    source_link = db.Column(db.String(500))

class StateElectionData(db.Model):
    __tablename__ = 'state_election_data'
    data_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(100), nullable=False)
    election_year = db.Column(db.Integer)
    total_registered_voters = db.Column(db.Integer)
    total_male_voters = db.Column(db.Integer)
    total_female_voters = db.Column(db.Integer)
    total_third_gender_voters = db.Column(db.Integer)
    votes_cast_total = db.Column(db.Integer)
    votes_cast_male = db.Column(db.Integer)
    votes_cast_female = db.Column(db.Integer)
    voter_turnout_percentage = db.Column(db.Float)
    total_constituencies = db.Column(db.Integer)
    total_polling_booths = db.Column(db.Integer)
    source = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class GlossaryTerm(db.Model):
    __tablename__ = 'glossary_terms'
    term_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    term_english = db.Column(db.String(255), nullable=False)
    term_hindi = db.Column(db.String(255))
    term_marathi = db.Column(db.String(255))
    definition_english = db.Column(db.Text)
    definition_hindi = db.Column(db.Text)
    definition_marathi = db.Column(db.Text)
    example_english = db.Column(db.Text)
    example_hindi = db.Column(db.Text)
    example_marathi = db.Column(db.Text)
    related_terms = db.Column(db.Text) # JSON array of term_ids
    category = db.Column(db.String(100))

class NewsArticle(db.Model):
    __tablename__ = 'news_articles'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    headline_english = db.Column(db.String(500), nullable=False)
    headline_hindi = db.Column(db.String(500))
    headline_marathi = db.Column(db.String(500))
    summary = db.Column(db.Text)
    full_content_url = db.Column(db.String(500))
    source_name = db.Column(db.String(255))
    source_url = db.Column(db.String(500))
    category = db.Column(db.String(100))
    published_at = db.Column(db.DateTime)
    scraped_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_verified = db.Column(db.Boolean, default=True)
    thumbnail_url = db.Column(db.String(500))

class ChatbotHistory(db.Model):
    __tablename__ = 'chatbot_history'
    chat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    session_identifier = db.Column(db.String(255))
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    language_detected = db.Column(db.String(50))
    topic_category = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    was_helpful = db.Column(db.Boolean)

class VoterSupportTicket(db.Model):
    __tablename__ = 'voter_support_tickets'
    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    state = db.Column(db.String(100))
    issue_type = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='open')
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)

class ImpactVisualizerData(db.Model):
    __tablename__ = 'impact_visualizer_data'
    impact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    election_year = db.Column(db.Integer, nullable=False)
    constituency_name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(100))
    winner_name = db.Column(db.String(255))
    winner_party = db.Column(db.String(255))
    runner_up_name = db.Column(db.String(255))
    runner_up_party = db.Column(db.String(255))
    winning_margin = db.Column(db.Integer)
    total_votes_cast = db.Column(db.Integer)
    registered_voters = db.Column(db.Integer)
    turnout_percentage = db.Column(db.Float)
    impact_story = db.Column(db.Text)
