import streamlit as st
import pandas as pd
from src import clean_text, extract_skills, calculate_similarity, analyze_skill_gap

st.set_page_config(page_title="AI Candidate Screening Framework", layout="wide")

st.title("🤖 AI Resume Screening & Skill-Gap Analysis System")
st.write("Upload candidate details and analyze role fitment instantly.")

# Sidebar Controls
st.sidebar.header("📋 Job Requirements")
job_title = st.sidebar.text_input("Target Job Profile", "Data Scientist")
jd_input = st.sidebar.text_area(
    "Paste Job Description Here", 
    "We are looking for a Data Scientist proficient in Python, SQL, Machine Learning, and Docker. Experience with AWS is a major plus."
)

# Mock Applicant Repository Data
mock_candidates = [
    {"Name": "John Doe", "Resume": "Data Scientist with 3 years experience. Skilled in Python, SQL, Machine Learning, and AWS cloud deployment."},
    {"Name": "Jane Smith", "Resume": "Frontend Web Developer. Expert in JavaScript, HTML, CSS, Git, and React framework."},
    {"Name": "Alice Johnson", "Resume": "HR Specialist. Experienced in talent acquisition, recruitment, employee onboarding, and Agile."}
]

st.header("👥 Candidate Evaluation")

if st.button("🚀 Run Screening Algorithm"):
    if jd_input:
        cleaned_jd = clean_text(jd_input)
        jd_skills = extract_skills(cleaned_jd)
        
        results = []
        for cand in mock_candidates:
            cleaned_resume = clean_text(cand["Resume"])
            cand_skills = extract_skills(cleaned_resume)
            
            # Run calculations
            score = calculate_similarity(cleaned_resume, cleaned_jd)
            matched, missing = analyze_skill_gap(cand_skills, jd_skills)
            
            results.append({
                "Candidate Name": cand["Name"],
                "Match Score (%)": round(score * 100, 2),
                "Matched Skills": ", ".join(matched) if matched else "None",
                "Missing Skills": ", ".join(missing) if missing else "None"
            })
            
        df_results = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        
        st.success("Analysis Complete! Candidates ranked below:")
        st.dataframe(df_results, use_container_width=True)
        st.bar_chart(df_results.set_index("Candidate Name")["Match Score (%)"])
    else:
        st.error("Please insert a job description configuration before processing.")