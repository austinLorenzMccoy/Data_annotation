import re
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def clean_text(text):
    """Cleans the input text by removing unwanted characters and normalizing whitespace."""
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing whitespace
    return text

def tokenize(text):
    """Tokenizes the input text using spaCy."""
    doc = nlp(text)
    return [token.text for token in doc]

def extract_medical_entities(text):
    """Extract medical entities using spaCy."""
    doc = nlp(text)
    medical_ents = [ent for ent in doc.ents if ent.label_ in ['DISEASE', 'CHEMICAL', 'PROCEDURE']]
    return medical_ents

def segment_sentences(text):
    """Segment text into sentences."""
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]

# Additional preprocessing functions can be added here as needed.