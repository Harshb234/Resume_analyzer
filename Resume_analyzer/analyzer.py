import spacy

nlp = spacy.load("en_core_web_sm")
KEYWORDS = ["Python", "Flask", "API", "NLP", "Machine Learning", "Data Analysis"]

def analyze_resume(text):
    doc = nlp(text)
    found_keywords = [kw for kw in KEYWORDS if kw.lower() in text.lower()]
    return {
        "keyword_count": len(found_keywords),
        "found_keywords": found_keywords,
        "total_keywords": len(KEYWORDS)
    }
