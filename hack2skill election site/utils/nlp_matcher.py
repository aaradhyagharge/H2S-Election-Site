from rapidfuzz import process, fuzz
from database.models import GlossaryTerm

def get_best_match(query, choices):
    # Extracts the best match above a certain score
    result = process.extractOne(query, choices, scorer=fuzz.token_set_ratio)
    if result and result[1] > 60:
        return result[0], result[1]
    return None, 0

def find_chatbot_response(user_message, lang='en'):
    # A simple knowledge base matching system for the hackathon
    # Ideally, this would query the DB for glossary terms or parliament members
    
    # Example logic: checking if it's a glossary term query
    terms = GlossaryTerm.query.all()
    if lang == 'en':
        choices = [t.term_english for t in terms]
    elif lang == 'hi':
        choices = [t.term_hindi for t in terms]
    else:
        choices = [t.term_marathi for t in terms]
        
    best_match, score = get_best_match(user_message, choices)
    
    if best_match:
        if lang == 'en':
            term = GlossaryTerm.query.filter_by(term_english=best_match).first()
            return f"{term.term_english}: {term.definition_english}"
        elif lang == 'hi':
            term = GlossaryTerm.query.filter_by(term_hindi=best_match).first()
            return f"{term.term_hindi}: {term.definition_hindi}"
        else:
            term = GlossaryTerm.query.filter_by(term_marathi=best_match).first()
            return f"{term.term_marathi}: {term.definition_marathi}"
            
    # Generic fallback
    if lang == 'en':
        return "I am Bharat Bot, your election assistant. I can answer questions about the Indian election process. Try asking me about EVMs, VVPAT, or how to register to vote!"
    elif lang == 'hi':
        return "मैं भारत बॉट हूँ, आपका चुनाव सहायक। मैं भारतीय चुनाव प्रक्रिया के बारे में आपके सवालों के जवाब दे सकता हूँ। मुझसे ईवीएम, वीवीपैट या मतदान के लिए पंजीकरण करने के तरीके के बारे में पूछें!"
    else:
        return "मी भारत बॉट आहे, तुमचा निवडणूक सहाय्यक. मी भारतीय निवडणूक प्रक्रियेबद्दलच्या तुमच्या प्रश्नांची उत्तरे देऊ शकतो. मला ईव्हीएम, व्हीव्हीपॅट किंवा मतदान करण्यासाठी नोंदणी कशी करावी याबद्दल विचारा!"
