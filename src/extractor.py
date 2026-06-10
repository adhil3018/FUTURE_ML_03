import spacy
from spacy.matcher import PhraseMatcher
import os

# Safe cloud-deployment loading trick
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If the cloud platform missed the download, force-pull it right now!
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Define our search parameters
SKILL_DATABASE = [
    'python', 'sql', 'java', 'c++', 'javascript', 'tableau', 'power bi', 
    'excel', 'machine learning', 'deep learning', 'aws', 'azure', 'git', 
    'docker', 'kubernetes', 'project management', 'agile', 'scrum', 
    'html', 'css', 'react', 'recruitment', 'onboarding'
]

def extract_skills(text):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in SKILL_DATABASE]
    matcher.add("SkillPatterns", patterns)
    
    doc = nlp(text)
    matches = matcher(doc)
    
    extracted = set()
    for match_id, start, end in matches:
        extracted.add(doc[start:end].text.lower())
    return list(extracted)
