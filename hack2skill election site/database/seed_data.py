from database.models import db, Badge, GlossaryTerm, QuizQuestion, PoliticalParty, ParliamentMember, PollingBooth, ElectionHistory

def seed_database():
    # This function should be called within a Flask app context
    # Create all tables if they don't exist
    db.create_all()

    print("Seeding database...")

    # 1. Seed Badges
    if not Badge.query.first():
        badges = [
            Badge(badge_name_en="Jagruk Nagarik", badge_name_hi="जागरूक नागरिक", badge_name_mr="जागरूक नागरिक", badge_description="Awarded for completing the first chapter.", points_required=100, chapter_required=1),
            Badge(badge_name_en="Matdan Mitra", badge_name_hi="मतदान मित्र", badge_name_mr="मतदान मित्र", badge_description="Awarded for helping others register.", points_required=200, chapter_required=2),
            Badge(badge_name_en="Loktantra Rakshak", badge_name_hi="लोकतंत्र रक्षक", badge_name_mr="लोकशाही रक्षक", badge_description="Awarded for understanding EVM security.", points_required=400, chapter_required=4)
        ]
        db.session.add_all(badges)

    # 2. Seed Glossary Terms
    if not GlossaryTerm.query.first():
        terms = [
            GlossaryTerm(
                term_english="EVM", term_hindi="ईवीएम", term_marathi="ईव्हीएम",
                definition_english="Electronic Voting Machine used in Indian elections.",
                definition_hindi="भारतीय चुनावों में प्रयुक्त इलेक्ट्रॉनिक वोटिंग मशीन।",
                definition_marathi="भारतीय निवडणुकांमध्ये वापरले जाणारे इलेक्ट्रॉनिक मतदान यंत्र."
            ),
            GlossaryTerm(
                term_english="VVPAT", term_hindi="वीवीपैट", term_marathi="व्हीव्हीपॅट",
                definition_english="Voter Verifiable Paper Audit Trail system attached to EVM.",
                definition_hindi="ईवीएम से जुड़ी मतदाता सत्यापन योग्य पेपर ऑडिट ट्रेल प्रणाली।",
                definition_marathi="ईव्हीएमशी जोडलेली मतदार पडताळणी योग्य पेपर ऑडिट ट्रेल प्रणाली."
            ),
            GlossaryTerm(
                term_english="EPIC", term_hindi="एपिक", term_marathi="एपिक",
                definition_english="Elector's Photo Identity Card, commonly known as Voter ID.",
                definition_hindi="मतदाता फोटो पहचान पत्र।",
                definition_marathi="मतदार छायाचित्र ओळखपत्र."
            )
        ]
        db.session.add_all(terms)

    # 3. Seed Quiz Questions
    if not QuizQuestion.query.first():
        questions = [
            QuizQuestion(
                chapter_number=1,
                question_text_english="Why is voting important?",
                option_a_english="To get a holiday",
                option_b_english="To shape the future of the country",
                option_c_english="Because it is compulsory by law",
                correct_option="b"
            ),
            QuizQuestion(
                chapter_number=2,
                question_text_english="Which form is used for new voter registration?",
                option_a_english="Form 6",
                option_b_english="Form 7",
                option_c_english="Form 8",
                correct_option="a"
            )
        ]
        db.session.add_all(questions)
        
    # 4. Seed Polling Booths
    if not PollingBooth.query.first():
        booths = [
            PollingBooth(
                booth_number="101", booth_name="Govt Primary School, Rampur", 
                address="Main Road, Rampur", pincode="400001", state="Maharashtra",
                latitude=18.9220, longitude=72.8347, has_wheelchair_access=True
            )
        ]
        db.session.add_all(booths)

    # 5. Seed Political Parties (Neutral, factual data)
    if not PoliticalParty.query.first():
        parties = [
            PoliticalParty(party_name="Bharatiya Janata Party", party_abbreviation="BJP", founded_year=1980, national_or_state="national"),
            PoliticalParty(party_name="Indian National Congress", party_abbreviation="INC", founded_year=1885, national_or_state="national")
        ]
        db.session.add_all(parties)

    db.session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    # If run directly, we might still need an app context. 
    # But when imported into app.py, it will use app.app_context().
    pass
