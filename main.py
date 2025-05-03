import streamlit as st
import time
from resume_reader import Resume_reader
from skill_extractor import Skills
from scorer import Score
from suggestions import SuggestionGenerator
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="centered")

# Welcome message
if 'welcome_shown' not in st.session_state:
    st.session_state['welcome_shown'] = True
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""
            <style>
                .welcome-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .welcome-box {
                    background-color: #ffffff;
                    padding: 40px 50px;
                    border-radius: 20px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    animation: fadeIn 1s ease-in-out;
                }
                .welcome-box h2 {
                    font-size: 2.5rem;
                    color: #1f77b4;
                    margin-bottom: 10px;
                }
                .welcome-box p {
                    font-size: 1.1rem;
                    color: #333333;
                }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
            </style>
            <div class="welcome-container">
                <div class="welcome-box">
                    <h2>👋 Welcome to Smart Resume Analyzer</h2>
                    <p>This AI-powered tool helps you improve your resume for top job opportunities.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(1.5)
    placeholder.empty()

# Title and Description
st.title("📝 Smart Resume Analyzer")
st.markdown("""
    Upload your resume in PDF format to receive:
    ✅ **Skills Extracted from Resume**  
    📊 **Resume Optimization Score**  
    💡 **Personalized Improvement Tips**
""", unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success(f"Successfully uploaded: {uploaded_file.name}")
    reader = Resume_reader(uploaded_file)
    resume_text = reader.extract_text()

    if resume_text:
        skills_df = pd.read_csv("data/skills.csv")
        all_skills = skills_df["skills"].tolist()

        extractor = Skills(resume_text)
        extractor.load_skills("data/skills.csv")
        found_skills = extractor.extracted_skills()
        skill_counts = Counter(found_skills)

        scorer = Score(found_skills, all_skills)
        score = scorer.calculate()
        feedback = scorer.display_feedback(score)

        suggestor = SuggestionGenerator(found_skills, all_skills)
        suggestions = suggestor.generate_suggestions()

        # Tabs for organized content
        tabs = st.tabs([
            "📘 Resume Preview",
            "📊 Score & Summary",
            "✅ Feedback",
            "💡 Suggestions",
            "📌 Skills & Analysis",
            "🔍 Experience Check"
        ])

        with tabs[0]:
            st.subheader("📘 Extracted Resume Text (Preview)")
            st.write(resume_text[:2000])

        with tabs[1]:
            st.subheader("📊 Resume Score")
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': f"Resume Score: {score}"},
                gauge={'axis': {'range': [None, 100]},
                       'bar': {'color': "lightgreen"},
                       'steps': [
                           {'range': [0, 50], 'color': "red"},
                           {'range': [50, 75], 'color': "orange"},
                           {'range': [75, 100], 'color': "green"}]}))
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("🏆 Resume Rank Simulation")
            if score >= 90:
                st.success("🌟 Top Tier Resume: Likely to stand out to recruiters.")
            elif score >= 75:
                st.info("👍 Competitive Resume: Consider small enhancements.")
            elif score >= 50:
                st.warning("⚠️ Moderate Resume: Room for significant improvement.")
            else:
                st.error("❌ Weak Resume: Needs major revision.")

            st.subheader("🧠 Resume Summary")
            st.write(f"Your resume highlights **{len(found_skills)}** relevant skills. You're experienced in: **{', '.join(found_skills[:5])}...**")

        with tabs[2]:
            st.subheader("🎨 Resume Style Advice")
            st.markdown("""
                - Keep it under **2 pages**
                - Use consistent font and spacing
                - Avoid large blocks of text
                - Use bullet points for clarity
                - Reverse-chronological order for experience
            """)
            st.subheader("✅ Resume Feedback")
            st.info(feedback)

        with tabs[3]:
            st.subheader("💡 Personalized Improvement Suggestions")
            for tip in suggestions["tips"]:
                with st.expander(f"• {tip}"):
                    st.markdown("- Tailor your resume for specific roles.")
                    st.markdown("- Quantify your impact (e.g., 'increased sales by 20%').")
                    st.markdown("- Add certifications/tools where relevant.")

        with tabs[4]:
            st.subheader("📌 Skills Found ")
            if found_skills:
                wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(found_skills))
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                st.pyplot(plt)
            else:
                st.warning("No skills detected. Try adding job-relevant terms.")

            st.subheader("📊 Skills Frequency")
            selected_skill = st.selectbox("Select a Skill to See Frequency", list(skill_counts.keys()))
            if selected_skill:
                st.write(f"The skill **{selected_skill}** appears **{skill_counts[selected_skill]}** time(s) in your resume.")

            st.subheader("📋 Skills Classification")
            st.markdown("**🔧 Technical Skills**")
            tech_skills = [s for s in found_skills if s in all_skills]
            st.success(", ".join(tech_skills) if tech_skills else "No technical skills detected.")

            st.markdown("**💬 Soft Skills**")
            soft_skills = [s for s in found_skills if s not in all_skills]
            st.success(", ".join(soft_skills) if soft_skills else "No soft skills detected.")

        with tabs[5]:
            st.subheader("🔍 Experience & Projects")
            if "project" in resume_text.lower() or "experience" in resume_text.lower():
                st.success("Relevant projects/experience found.")
            else:
                st.warning("Consider adding detailed project/experience descriptions.")

            st.subheader("⚖️ Experience Level Feedback")
            if score >= 80:
                st.success("Your resume reflects a high level of expertise.")
            elif 50 <= score < 80:
                st.warning("Resume shows good experience, but has room to grow.")
            else:
                st.error("Resume lacks depth in experience.")

    else:
        st.error("The uploaded resume seems to be either empty or unreadable. Please check the file and try again.")

