import re
import nltk
from nltk.corpus import stopwords

# Safeguard stopword downloading
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r'http\S+\s*', ' ', text)  # Remove URLs
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', ' ', text)  # Remove emails
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # Remove special characters & numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Collapse extra spaces
    
    return " ".join([word for word in text.split() if word not in stop_words])