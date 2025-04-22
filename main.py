
# # import streamlit as st
# # from resume_reader import Resume_reader
# # from skill_extractor import Skills
# # from scorer import Score
# # from suggestions import SuggestionGenerator
# # import pandas as pd

# # st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="centered")
# # st.title("📄 Smart Resume Analyzer")
# # st.markdown("Upload your resume in PDF format to receive:\n\n✅ Skills Extracted from Resume\n📊 Resume Optimization Score\n💡 Personalized Improvement Tips")

# # uploaded_file = st.file_uploader("📤 Upload Resume", type=["pdf"])

# # if uploaded_file:
# #     st.success(f"Uploaded: {uploaded_file.name}")

# #     # Extract resume text
# #     reader = Resume_reader(uploaded_file)
# #     resume_text = reader.extract_text()

# #     if resume_text:
# #         with st.expander("📘 Extracted Resume Text (Preview)"):
# #             st.write(resume_text[:2000])  # only show first 2000 chars

# #         # Load skills
# #         skills_df = pd.read_csv("data/skills.csv")
# #         all_skills = skills_df["skills"].tolist()

# #         # Extract skills
# #         extractor = Skills(resume_text)
# #         extractor.load_skills("data/skills.csv")
# #         found_skills = extractor.extracted_skills()

# #         # Score
# #         scorer = Score(found_skills, all_skills)
# #         score = scorer.calculate()
# #         feedback = scorer.display_feedback(score)

# #         # Suggestions
# #         suggestor = SuggestionGenerator(found_skills, all_skills)
# #         suggestions = suggestor.generate_suggestions()

# #         st.subheader("📊 Resume Score")
# #         st.progress(score / 100)
# #         st.write(f"**Score:** {score} / 100")
# #         st.info(feedback)

# #         st.subheader("✅ Skills Found")
# #         if found_skills:
# #             st.success(", ".join(found_skills))
# #         else:
# #             st.warning("No relevant skills found. Try improving your resume.")

# #         st.subheader("🔍 Suggestions for Improvement")
# #         for tip in suggestions["tips"]:
# #             st.markdown(tip)

# #         st.subheader("❌ Missing Skills")
# #         st.error(", ".join(suggestions["key_skills"]))
# #     else:
# #         st.error("❌ Could not extract text from PDF. Please upload a clear, text-based resume.")


# import streamlit as st
# from resume_reader import Resume_reader
# from skill_extractor import Skills
# from scorer import Score
# from suggestions import SuggestionGenerator
# import pandas as pd
# import plotly.graph_objects as go  # For the circular progress bar

# # Setting page config
# st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="wide")
# st.title("📄 Smart Resume Analyzer")
# st.markdown("Upload your resume in PDF format to receive:\n\n✅ Skills Extracted from Resume\n📊 Resume Optimization Score\n💡 Personalized Improvement Tips")

# uploaded_file = st.file_uploader("📤 Upload Resume", type=["pdf"])

# # Sidebar for extra tips and navigation
# with st.sidebar:
#     st.header("Welcome to Smart Resume Analyzer")
#     if uploaded_file:
#         st.info("Resume uploaded successfully! 🎉 Now we are analyzing your resume.")
        
#         # Display Resume Progress
#         st.markdown("### 📝 Resume Progress")
        
#         # Dynamic Circular Progress Bar (Improvement)
#         progress = 75  # This would be dynamically calculated
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=progress,
#             title={'text': f"Resume Score: {progress}"},
#             gauge={'axis': {'range': [None, 100]},
#                    'bar': {'color': "lightgreen"},
#                    'steps': [
#                        {'range': [0, 50], 'color': "red"},
#                        {'range': [50, 75], 'color': "yellow"},
#                        {'range': [75, 100], 'color': "green"}]}))
#         st.plotly_chart(fig, use_container_width=True)

#         # Resume Analysis Summary in Sidebar
#         st.markdown("### 📊 Resume Analysis Summary")
#         st.write(f"**Skills Identified**: 15 skills found!")
#         st.write(f"**Resume Score**: 75% (Great job!)")

#         # Learn More Section with a Dropdown
#         st.markdown("### 📚 Learn More")
#         with st.expander("Resume Writing Tips 📖"):
#             st.markdown("- Focus on **relevant skills**.")
#             st.markdown("- Use **action verbs** to describe your work.")
#             st.markdown("- Keep the **format clean** and easy to read.")
#             st.markdown("- Tailor your resume for **specific job roles**.")

#         # Suggestions with Actionable Tips
#         st.markdown("### 📝 Personalized Suggestions")
#         with st.expander("Suggestions for Improvement ✨"):
#             st.write("Here are some actionable tips to improve your resume:")
#             st.markdown("1. **Add measurable achievements** in your experience section.")
#             st.markdown("2. **Emphasize relevant technical skills** for the job you are targeting.")
#             st.markdown("3. **Highlight certifications or additional courses** you've completed.")
#             st.markdown("4. Ensure that your resume passes **ATS scanners** by including industry-related keywords.")

#     else:
#         st.info("Please upload your resume to get started.")
#         st.markdown("### 📝 Resume Progress")
#         st.progress(0)
#         st.write("Your Resume Progress: 0%")
    
# if uploaded_file:
#     st.success(f"Uploaded: {uploaded_file.name}")

#     # Extract resume text
#     reader = Resume_reader(uploaded_file)
#     resume_text = reader.extract_text()

#     if resume_text:
#         with st.expander("📘 Extracted Resume Text (Preview)"):
#             st.write(resume_text[:2000])  # Only show first 2000 chars for preview

#         # Load skills
#         skills_df = pd.read_csv("data/skills.csv")
#         all_skills = skills_df["skills"].tolist()

#         # Extract skills
#         extractor = Skills(resume_text)
#         extractor.load_skills("data/skills.csv")
#         found_skills = extractor.extracted_skills()

#         # Score calculation
#         scorer = Score(found_skills, all_skills)
#         score = scorer.calculate()
#         feedback = scorer.display_feedback(score)

#         # Suggestions
#         suggestor = SuggestionGenerator(found_skills, all_skills)
#         suggestions = suggestor.generate_suggestions()

#         # Circular Progress Bar
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=score,
#             title={'text': f"Resume Score: {score}"},
#             gauge={'axis': {'range': [None, 100]},
#                    'bar': {'color': "lightgreen"},
#                    'steps': [
#                        {'range': [0, 50], 'color': "red"},
#                        {'range': [50, 75], 'color': "yellow"},
#                        {'range': [75, 100], 'color': "green"}]}))
#         st.plotly_chart(fig, use_container_width=True)

#         # Resume feedback and suggestions
#         st.subheader("✅ Resume Feedback")
#         st.info(feedback)

#         st.subheader("✅ Skills Found")
#         if found_skills:
#             st.success(", ".join(found_skills))
#         else:
#             st.warning("No relevant skills found. Try improving your resume.")

#         st.subheader("🔍 Suggestions for Improvement")
#         for tip in suggestions["tips"]:
#             with st.expander(f"• {tip}"):
#                 st.write("Click to learn more about this tip and how to implement it in your resume.")
#                 st.markdown("For example, mention more specific details about your projects or experience.")

#         st.markdown("---")

#         # Interactive Section: Suggestions with collapsible sections for details
#         st.subheader("📋 Detailed Improvement Tips")
#         for tip in suggestions["tips"]:
#             with st.expander(f"**{tip}**"):
#                 st.write(f"This is an actionable step you can take to improve your resume. Here's how:")
#                 st.markdown("- Add more technical details about your recent projects.")
#                 st.markdown("- Ensure that your skills align with job requirements.")
#                 st.markdown("- Include measurable results wherever possible.")




# import streamlit as st
# from resume_reader import Resume_reader
# from skill_extractor import Skills
# from scorer import Score
# from suggestions import SuggestionGenerator
# import pandas as pd
# import plotly.graph_objects as go  # For the circular progress bar

# # Setting page config
# st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="centered")
# st.title("📄 Smart Resume Analyzer")
# st.markdown("Upload your resume in PDF format to receive:\n\n✅ Skills Extracted from Resume\n📊 Resume Optimization Score\n💡 Personalized Improvement Tips")

# uploaded_file = st.file_uploader("📤 Upload Resume", type=["pdf"])

# if uploaded_file:
#     st.success(f"Uploaded: {uploaded_file.name}")

#     # Extract resume text
#     reader = Resume_reader(uploaded_file)
#     resume_text = reader.extract_text()

#     if resume_text:
#         with st.expander("📘 Extracted Resume Text (Preview)"):
#             st.write(resume_text[:2000])  # Only show first 2000 chars for preview

#         # Load skills
#         skills_df = pd.read_csv("data/skills.csv")
#         all_skills = skills_df["skills"].tolist()

#         # Extract skills
#         extractor = Skills(resume_text)
#         extractor.load_skills("data/skills.csv")
#         found_skills = extractor.extracted_skills()

#         # Score calculation
#         scorer = Score(found_skills, all_skills)
#         score = scorer.calculate()
#         feedback = scorer.display_feedback(score)

#         # Suggestions
#         suggestor = SuggestionGenerator(found_skills, all_skills)
#         suggestions = suggestor.generate_suggestions()

#         # Circular Progress Bar
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=score,
#             title={'text': f"Resume Score: {score}"},
#             gauge={'axis': {'range': [None, 100]},
#                    'bar': {'color': "lightgreen"},
#                    'steps': [
#                        {'range': [0, 50], 'color': "red"},
#                        {'range': [50, 75], 'color': "yellow"},
#                        {'range': [75, 100], 'color': "green"}]}))
#         st.plotly_chart(fig, use_container_width=True)

#         # Resume feedback and suggestions
#         st.subheader("✅ Resume Feedback")
#         st.info(feedback)

#         st.subheader("✅ Skills Found")
#         if found_skills:
#             st.success(", ".join(found_skills))
#         else:
#             st.warning("No relevant skills found. Try improving your resume.")

#         st.subheader("🔍 Suggestions for Improvement")
#         for tip in suggestions["tips"]:
#             with st.expander(f"• {tip}"):
#                 st.write("Click to learn more about this tip and how to implement it in your resume.")
#                 st.markdown("For example, mention more specific details about your projects or experience.")

#         st.markdown("---")

#         # Interactive Section: Suggestions with collapsible sections for details
#         st.subheader("📋 Detailed Improvement Tips")
#         for tip in suggestions["tips"]:
#             with st.expander(f"**{tip}**"):
#                 st.write(f"This is an actionable step you can take to improve your resume. Here's how:")
#                 st.markdown("- Add more technical details about your recent projects.")
#                 st.markdown("- Ensure that your skills align with job requirements.")
#                 st.markdown("- Include measurable results wherever possible.")

# else:
#     st.info("Please upload your resume to get started.")
#     st.markdown("### 📝 Resume Progress")
#     st.progress(0)
#     st.write("Your Resume Progress: 0%")




# import streamlit as st
# from resume_reader import Resume_reader
# from skill_extractor import Skills
# from scorer import Score
# from suggestions import SuggestionGenerator
# import pandas as pd
# import plotly.graph_objects as go
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image

# # Set page config with a more polished theme
# st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="centered")
# st.title("📄 Smart Resume Analyzer")
# st.markdown("""
#     Upload your resume in PDF format to receive:\n
#     ✅ **Skills Extracted from Resume**\n
#     📊 **Resume Optimization Score**\n
#     💡 **Personalized Improvement Tips**
# """, unsafe_allow_html=True)

# # Add custom styles for the page
# st.markdown("""
#     <style>
#         .css-1v3fvcr { background-color: #F0F4F8; }
#         .css-1gh6xxp { font-family: 'Arial', sans-serif; }
#         .stButton > button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 8px; }
#         .stProgress > div { background-color: #4CAF50; }
#         h1 { color: #2C3E50; text-align: center; }
#         .stFileUploader { border: 1px solid #ddd; border-radius: 8px; padding: 10px; }
#         .st-expanderHeader { font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)

# # Uploading resume section
# uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])

# if uploaded_file:
#     st.success(f"Successfully uploaded: {uploaded_file.name}")

#     # Resume extraction process
#     reader = Resume_reader(uploaded_file)
#     resume_text = reader.extract_text()

#     if resume_text:
#         with st.expander("📘 Extracted Resume Text (Preview)") :
#             st.write(resume_text[:2000])  # Show first 2000 chars for preview

#         # Load skills from CSV file and extract the resume skills
#         skills_df = pd.read_csv("data/skills.csv")
#         all_skills = skills_df["skills"].tolist()

#         # Extract skills from the resume text
#         extractor = Skills(resume_text)
#         extractor.load_skills("data/skills.csv")
#         found_skills = extractor.extracted_skills()

#         # Score calculation for resume optimization
#         scorer = Score(found_skills, all_skills)
#         score = scorer.calculate()
#         feedback = scorer.display_feedback(score)

#         # Suggestions for improvement
#         suggestor = SuggestionGenerator(found_skills, all_skills)
#         suggestions = suggestor.generate_suggestions()

#         # Create circular progress bar for Resume Score
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=score,
#             title={'text': f"Resume Score: {score}"},
#             gauge={'axis': {'range': [None, 100]},
#                    'bar': {'color': "lightgreen"},
#                    'steps': [
#                        {'range': [0, 50], 'color': "red"},
#                        {'range': [50, 75], 'color': "yellow"},
#                        {'range': [75, 100], 'color': "green"}]}))
#         st.plotly_chart(fig, use_container_width=True)

#         # Resume feedback and suggestions section
#         st.subheader("✅ Resume Feedback")
#         st.info(feedback)

#         # Section for extracted skills with word cloud visualization
#         st.subheader("✅ Skills Found in Resume")
#         if found_skills:
#             # Create a Word Cloud for the skills found in the resume
#             wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(found_skills))
#             plt.figure(figsize=(10, 5))
#             plt.imshow(wordcloud, interpolation="bilinear")
#             plt.axis("off")
#             st.pyplot(plt)

#         else:
#             st.warning("No relevant skills found. Consider adding more skills related to your field.")

#         # Suggestions for improvement section
#         st.subheader("🔍 Suggestions for Improvement")
#         for tip in suggestions["tips"]:
#             with st.expander(f"• {tip}"):
#                 st.write("Click to learn more about this tip and how to implement it in your resume.")
#                 st.markdown("For example, mention more specific details about your projects or experience.")

#         st.markdown("---")

#         # Detailed Analysis Section with subcategories
#         st.subheader("📋 Detailed Resume Analysis")
#         st.write("The following sections provide a breakdown of your resume, categorized by skills and experience level:")

#         # Technical Skills Analysis
#         st.subheader("🔧 Technical Skills")
#         technical_skills = [skill for skill in found_skills if skill in all_skills]  # Filter technical skills
#         if technical_skills:
#             st.success(", ".join(technical_skills))
#         else:
#             st.warning("No technical skills found. Try including programming languages or tools you are proficient in.")

#         # Soft Skills Analysis
#         st.subheader("💬 Soft Skills")
#         soft_skills = [skill for skill in found_skills if skill not in all_skills]  # Filter soft skills
#         if soft_skills:
#             st.success(", ".join(soft_skills))
#         else:
#             st.warning("No soft skills found. Try including interpersonal skills like communication, teamwork, etc.")

#         # Experience & Projects Analysis
#         st.subheader("🔍 Experience & Projects")
#         if "project" in resume_text.lower() or "experience" in resume_text.lower():
#             st.success("Your resume mentions projects and experiences. Make sure to elaborate on your achievements and results.")
#         else:
#             st.warning("No detailed projects or experience mentioned. Consider adding detailed descriptions of your work.")

#         # Optional Interactive Feature: Feedback on Experience Level
#         st.subheader("⚖️ Experience Level Feedback")
#         if score >= 80:
#             st.success("Your resume reflects a high level of expertise.")
#         elif 50 <= score < 80:
#             st.warning("Your resume shows good experience, but there is room for improvement.")
#         else:
#             st.error("Your resume lacks sufficient experience. Consider adding more relevant details.")

#         # Suggestions for Improvement with personalized feedback
#         st.subheader("💡 Personalized Improvement Suggestions")
#         for tip in suggestions["tips"]:
#             with st.expander(f"• {tip}"):
#                 st.write(f"Here’s how you can improve your resume:")
#                 st.markdown("- Add more specific achievements to your job experience.")
#                 st.markdown("- Ensure your skills align with the job roles you're targeting.")
#                 st.markdown("- Quantify your achievements with metrics wherever possible.")




# import streamlit as st
# from resume_reader import Resume_reader
# from skill_extractor import Skills
# from scorer import Score
# from suggestions import SuggestionGenerator
# import pandas as pd
# import plotly.graph_objects as go
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image
# from collections import Counter

# # Set page config with a more polished theme
# st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="centered")
# st.title("📄 Smart Resume Analyzer")
# st.markdown("""
#     Upload your resume in PDF format to receive:\n
#     ✅ **Skills Extracted from Resume**\n
#     📊 **Resume Optimization Score**\n
#     💡 **Personalized Improvement Tips**
# """, unsafe_allow_html=True)

# # Add custom styles for the page
# st.markdown("""
#     <style>
#         .css-1v3fvcr { background-color: #F0F4F8; }
#         .css-1gh6xxp { font-family: 'Arial', sans-serif; }
#         .stButton > button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 8px; }
#         .stProgress > div { background-color: #4CAF50; }
#         h1 { color: #2C3E50; text-align: center; }
#         .stFileUploader { border: 1px solid #ddd; border-radius: 8px; padding: 10px; }
#         .st-expanderHeader { font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)

# # Uploading resume section
# uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])

# if uploaded_file:
#     st.success(f"Successfully uploaded: {uploaded_file.name}")

#     # Resume extraction process
#     reader = Resume_reader(uploaded_file)
#     resume_text = reader.extract_text()

#     if resume_text:
#         with st.expander("📘 Extracted Resume Text (Preview)") :
#             st.write(resume_text[:2000])  # Show first 2000 chars for preview

#         # Load skills from CSV file and extract the resume skills
#         skills_df = pd.read_csv("data/skills.csv")
#         all_skills = skills_df["skills"].tolist()

#         # Extract skills from the resume text
#         extractor = Skills(resume_text)
#         extractor.load_skills("data/skills.csv")
#         found_skills = extractor.extracted_skills()

#         # Count the frequency of skills
#         skill_counts = Counter(found_skills)

#         # Score calculation for resume optimization
#         scorer = Score(found_skills, all_skills)
#         score = scorer.calculate()
#         feedback = scorer.display_feedback(score)

#         # Suggestions for improvement
#         suggestor = SuggestionGenerator(found_skills, all_skills)
#         suggestions = suggestor.generate_suggestions()

#         # Create circular progress bar for Resume Score
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=score,
#             title={'text': f"Resume Score: {score}"},
#             gauge={'axis': {'range': [None, 100]},
#                    'bar': {'color': "lightgreen"},
#                    'steps': [
#                        {'range': [0, 50], 'color': "red"},
#                        {'range': [50, 75], 'color': "yellow"},
#                        {'range': [75, 100], 'color': "green"}]}))
#         st.plotly_chart(fig, use_container_width=True)

#         # Resume feedback and suggestions section
#         st.subheader("✅ Resume Feedback")
#         st.info(feedback)

#         # Section for extracted skills with word cloud visualization
#         st.subheader("✅ Skills Found in Resume")
#         if found_skills:
#             # Create a Word Cloud for the skills found in the resume
#             wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(found_skills))
#             plt.figure(figsize=(10, 5))
#             plt.imshow(wordcloud, interpolation="bilinear")
#             plt.axis("off")
#             st.pyplot(plt)

#         else:
#             st.warning("No relevant skills found. Consider adding more skills related to your field.")

#         # Create dropdown to display skills and their frequencies
#         st.subheader("📊 Skills Frequency")
#         selected_skill = st.selectbox(
#             "Select a Skill to See Frequency",
#             list(skill_counts.keys())
#         )

#         if selected_skill:
#             st.write(f"The skill '{selected_skill}' appears {skill_counts[selected_skill]} time(s) in the resume.")

#         # Detailed Analysis Section with subcategories
#         st.subheader("📋 Detailed Resume Analysis")
#         st.write("The following sections provide a breakdown of your resume, categorized by skills and experience level:")

#         # Technical Skills Analysis
#         st.subheader("🔧 Technical Skills")
#         technical_skills = [skill for skill in found_skills if skill in all_skills]  # Filter technical skills
#         if technical_skills:
#             st.success(", ".join(technical_skills))
#         else:
#             st.warning("No technical skills found. Try including programming languages or tools you are proficient in.")

#         # Soft Skills Analysis
#         st.subheader("💬 Soft Skills")
#         soft_skills = [skill for skill in found_skills if skill not in all_skills]  # Filter soft skills
#         if soft_skills:
#             st.success(", ".join(soft_skills))
#         else:
#             st.warning("No soft skills found. Try including interpersonal skills like communication, teamwork, etc.")

#         # Experience & Projects Analysis
#         st.subheader("🔍 Experience & Projects")
#         if "project" in resume_text.lower() or "experience" in resume_text.lower():
#             st.success("Your resume mentions projects and experiences. Make sure to elaborate on your achievements and results.")
#         else:
#             st.warning("No detailed projects or experience mentioned. Consider adding detailed descriptions of your work.")

#         # Optional Interactive Feature: Feedback on Experience Level
#         st.subheader("⚖️ Experience Level Feedback")
#         if score >= 80:
#             st.success("Your resume reflects a high level of expertise.")
#         elif 50 <= score < 80:
#             st.warning("Your resume shows good experience, but there is room for improvement.")
#         else:
#             st.error("Your resume lacks sufficient experience. Consider adding more relevant details.")

#         # Suggestions for Improvement with personalized feedback
#         st.subheader("💡 Personalized Improvement Suggestions")
#         for tip in suggestions["tips"]:
#             with st.expander(f"• {tip}"):
#                 st.write(f"Here’s how you can improve your resume:")
#                 st.markdown("- Add more specific achievements to your job experience.")
#                 st.markdown("- Ensure your skills align with the job roles you're targeting.")
#                 st.markdown("- Quantify your achievements with metrics wherever possible.")




import streamlit as st
from resume_reader import Resume_reader
from skill_extractor import Skills
from scorer import Score
from suggestions import SuggestionGenerator
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter

# Set page config with a more polished theme
st.set_page_config(page_title="📄 Smart Resume Analyzer", layout="centered")
st.title("📄 Smart Resume Analyzer")
st.markdown("""
    Upload your resume in PDF format to receive:\n
    ✅ **Skills Extracted from Resume**\n
    📊 **Resume Optimization Score**\n
    💡 **Personalized Improvement Tips**
""", unsafe_allow_html=True)

# Add custom styles for the page
st.markdown("""
    <style>
        .css-1v3fvcr { background-color: #F9F9F9; padding: 20px; border-radius: 12px; }
        .css-1gh6xxp { font-family: 'Roboto', sans-serif; color: #333; }
        .stButton > button { 
            background-color: #4CAF50; 
            color: white; 
            font-size: 16px; 
            border-radius: 8px; 
            padding: 10px 20px; 
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover { background-color: #45a049; }
        .stProgress > div { background-color: #4CAF50; }
        h1 { color: #2C3E50; text-align: center; font-weight: 600; }
        .stFileUploader { border: 2px solid #ddd; border-radius: 8px; padding: 12px; background-color: #f4f4f4; }
        .st-expanderHeader { font-weight: bold; color: #2C3E50; }
        .st-selectbox, .st-textarea { width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #ddd; }
        .stRadio { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

# Uploading resume section
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success(f"Successfully uploaded: {uploaded_file.name}")

    # Resume extraction process
    reader = Resume_reader(uploaded_file)
    resume_text = reader.extract_text()

    if resume_text:
        with st.expander("📘 Extracted Resume Text (Preview)") :
            st.write(resume_text[:2000])  # Show first 2000 chars for preview

        # Load skills from CSV file and extract the resume skills
        skills_df = pd.read_csv("data/skills.csv")
        all_skills = skills_df["skills"].tolist()

        # Extract skills from the resume text
        extractor = Skills(resume_text)
        extractor.load_skills("data/skills.csv")
        found_skills = extractor.extracted_skills()

        # Count the frequency of skills
        skill_counts = Counter(found_skills)

        # Score calculation for resume optimization
        scorer = Score(found_skills, all_skills)
        score = scorer.calculate()
        feedback = scorer.display_feedback(score)

        # Suggestions for improvement
        suggestor = SuggestionGenerator(found_skills, all_skills)
        suggestions = suggestor.generate_suggestions()

        # Create circular progress bar for Resume Score
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': f"Resume Score: {score}"},
            gauge={'axis': {'range': [None, 100]},
                   'bar': {'color': "lightgreen"},
                   'steps': [
                       {'range': [0, 50], 'color': "red"},
                       {'range': [50, 75], 'color': "yellow"},
                       {'range': [75, 100], 'color': "green"}]}))
        st.plotly_chart(fig, use_container_width=True)

        # Resume feedback and suggestions section
        st.subheader("✅ Resume Feedback")
        st.info(feedback)

        # Section for extracted skills with word cloud visualization
        st.subheader("✅ Skills Found in Resume")
        if found_skills:
            # Create a Word Cloud for the skills found in the resume
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(found_skills))
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)

        else:
            st.warning("No relevant skills found. Consider adding more skills related to your field.")

        # Create dropdown to display skills and their frequencies
        st.subheader("📊 Skills Frequency")
        selected_skill = st.selectbox(
            "Select a Skill to See Frequency",
            list(skill_counts.keys())
        )

        if selected_skill:
            st.write(f"The skill '{selected_skill}' appears {skill_counts[selected_skill]} time(s) in the resume.")

        # Detailed Analysis Section with subcategories
        st.subheader("📋 Detailed Resume Analysis")
        st.write("The following sections provide a breakdown of your resume, categorized by skills and experience level:")

        # Technical Skills Analysis
        st.subheader("🔧 Technical Skills")
        technical_skills = [skill for skill in found_skills if skill in all_skills]  # Filter technical skills
        if technical_skills:
            st.success(", ".join(technical_skills))
        else:
            st.warning("No technical skills found. Try including programming languages or tools you are proficient in.")

        # Soft Skills Analysis
        st.subheader("💬 Soft Skills")
        soft_skills = [skill for skill in found_skills if skill not in all_skills]  # Filter soft skills
        if soft_skills:
            st.success(", ".join(soft_skills))
        else:
            st.warning("No soft skills found. Try including interpersonal skills like communication, teamwork, etc.")

        # Experience & Projects Analysis
        st.subheader("🔍 Experience & Projects")
        if "project" in resume_text.lower() or "experience" in resume_text.lower():
            st.success("Your resume mentions projects and experiences. Make sure to elaborate on your achievements and results.")
        else:
            st.warning("No detailed projects or experience mentioned. Consider adding detailed descriptions of your work.")

        # Optional Interactive Feature: Feedback on Experience Level
        st.subheader("⚖️ Experience Level Feedback")
        if score >= 80:
            st.success("Your resume reflects a high level of expertise.")
        elif 50 <= score < 80:
            st.warning("Your resume shows good experience, but there is room for improvement.")
        else:
            st.error("Your resume lacks sufficient experience. Consider adding more relevant details.")

        # Suggestions for Improvement with personalized feedback
        st.subheader("💡 Personalized Improvement Suggestions")
        for tip in suggestions["tips"]:
            with st.expander(f"• {tip}") :
                st.write(f"Here’s how you can improve your resume:")
                st.markdown("- Add more specific achievements to your job experience.")
                st.markdown("- Ensure your skills align with the job roles you're targeting.")
                st.markdown("- Quantify your achievements with metrics wherever possible.")
