# AI-Powered Resume Screening & Candidate Ranking System

An intelligent, decision-support Machine Learning system built for HR teams and recruiters to automatically screen, score, and rank candidate resumes based on target job descriptions using Natural Language Processing (NLP).

## 🚀 Key Features Implemented
- **Text Preprocessing Pipeline:** Cleans unstructured resume text by removing URLs, emails, special characters, and non-informative stopwords.
- **NLP Skill Extraction Layer:** Utilizes `spaCy` to extract technical skills and industry keywords from unstructured profiles.
- **Vectorization & Similarity Model:** Transforms clean text documents into numerical vectors using **TF-IDF Vectorization** and calculates semantic alignment metrics using **Cosine Similarity**.
- **Skill Gap Analysis:** Computes structural skill differences mathematically, outputting explicitly what a candidate lacks relative to a job posting.
- **Interactive UI Dashboard:** Built an optional visual dashboard utilizing `Streamlit` to showcase rankings and performance charts cleanly for non-technical users.

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Libraries:** Scikit-learn, spaCy, NLTK, Pandas, NumPy
- **Framework:** Streamlit (UI Application)
- **Environment:** VS Code / Jupyter Notebook

## 📁 Repository Structure
```text
├── data/                  # Repository datasets (Resume.csv / Monster Job Descriptions)
├── notebooks/             # Experimental sandbox
│   └── exploration_and_modeling.ipynb
├── src/                   # Production-ready Python core modules
│   ├── __init__.py        # Exposes module architecture packages
│   ├── preprocessor.py    # Text cleaning script routines
│   ├── extractor.py       # Entity and skill extraction layer
│   └── scorer.py          # Similarity vector computation engines
├── app.py                 # Interactive Streamlit Web UI application Dashboard
└── requirements.txt       # Software and environment package dependencies