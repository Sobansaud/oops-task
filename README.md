STREAMLIT LINK : ["  "]




(Smart Resume Analyzer)

Overview:-

The Smart Resume Analyzer is an AI-powered web tool built using Object-Oriented Programming (OOP) techniques to optimize resumes for job seekers. By analyzing resumes in PDF format, the tool extracts essential skills, calculates a resume score, and provides personalized feedback to improve the chances of securing top job opportunities. The use of OOP ensures modularity, scalability, and ease of maintenance, making the tool highly efficient.

1) Features:-

Resume Upload and Extraction:

Users can upload their resume in PDF format.

The tool extracts the text from the resume using an OOP-based approach, where the ResumeReader class handles the PDF extraction logic.

2) Skills Extraction:

The tool uses the Skills class to extract and identify relevant skills mentioned in the resume.

Skills are categorized into Technical Skills and Soft Skills with the help of object-oriented methods.

3) Resume Score:

The Score class calculates a Resume Score based on how well the uploaded resume aligns with industry standards and job requirements.

The score is visualized using a gauge chart and categorized into different levels using OOP principles to keep the logic modular.

4) Personalized Feedback:

Using the SuggestionGenerator class, detailed feedback and advice are provided based on the resume content.

Actionable tips for improving design, content, and formatting are generated in an object-oriented manner.

5) Improvement Suggestions:

The tool generates a list of suggestions using the SuggestionGenerator class to enhance the resume, such as:

Tailoring the resume for specific roles.

Adding relevant certifications.

Quantifying achievements where possible.

6) Skills Visualization:

The use of OOP allows easy integration of visualization tools like Plotly for charts and WordCloud for visualizing skills.

Skills Frequency and Skills Classification are dynamically generated from the Skills class.

7) Experience and Projects Check:

The resume is analyzed for relevant work experience or projects using the ExperienceChecker class, which checks if the resume includes key experience or project-related data.


How It Works (Using OOP Principles)

*) File Upload:
Users upload a resume in PDF format through the front end.

*) Text Extraction:
The ResumeReader class extracts text from the PDF. This class handles PDF parsing, ensuring that the resume content is retrieved accurately and efficiently.

*)Skills Detection:
The Skills class analyzes the extracted resume content and identifies key skills. It compares the skills with predefined industry standards and categorizes them into Technical Skills and Soft Skills.

*) Scoring:
The Score class calculates the resume score based on the match between the identified skills and job market expectations. This class uses object-oriented methods to evaluate various components of the resume, from keywords to structure.

*) Feedback Generation:
The SuggestionGenerator class is responsible for providing personalized feedback based on the score, skill extraction, and overall resume content. This class generates suggestions for improving the resume, helping users make data-driven adjustments.

*) Data Visualization:
Visualization tools like Plotly (for charts) and WordCloud (for skill frequency visualization) are used to display data clearly and effectively, all managed through OOP principles for easy updates and modifications.

*) Results Display:
The results are presented through a structured, OOP-designed interface, allowing users to navigate through:

*) Resume Preview: Displays the extracted content of the resume.

*) Score & Summary: Shows the resume score and categorization.

*) Feedback: Offers actionable feedback and suggestions.

*) Skills & Analysis: Shows a detailed breakdown of extracted skills.

*) Experience Check: Verifies the inclusion of relevant work experience or projects.

(Technologies Used)

Streamlit: For building the web app and displaying the user interface.

Python: The core programming language, leveraging OOP to ensure clean, modular, and scalable code.

Pandas: For handling and analyzing skill data.

Plotly: For creating interactive charts and graphs, visualizing the resume score and skills.

WordCloud: For generating a visual representation of the most common skills found in the resume.

Matplotlib: For visualizing data, such as the word cloud.

(Custom OOP Modules:)

ResumeReader: A class for extracting text from PDF resumes using OOP techniques.

Skills: A class for detecting and categorizing skills.

Score: A class for calculating the resume score based on predefined metrics.

SuggestionGenerator: A class for generating feedback and improvement suggestions.

ExperienceChecker: A class to check and validate work experience listed in the resume.

(How to Use)


1) Upload your resume:
Click on the "📤 Upload Your Resume (PDF)" button and choose your resume file in PDF format.

2) Analyze your resume:
The tool automatically processes the resume and extracts the relevant information, all handled via the OOP-based structure of the backend.

3) Explore the results:
Navigate through the results using the user-friendly interface to view:

Resume Preview

Resume Score & Summary

Personalized Feedback

Improvement Suggestions

Skill Breakdown and Analysis

4) Improve your resume:
Follow the provided tips and suggestions to enhance your resume and align it better with industry standards.

