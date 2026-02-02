import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile ")

# Collect basic information
name = "Mr. Raji Wasiu Adeyinka"
field = "Computer Science"
institution = "University of Kwazulu-Nata"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.markdown('<h3 style="color: #87CEEB;">Contact Information</h3>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Email:** rajiwasiu49@gamil.com")  
with col2:
    st.write("**Cell:** 0653546725")  
with col3:
    st.write("**Location:** Durban")
st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg" "https://pixabay.com/images/download/x-5279536_1920.png",
    caption="Nature (Pixabay)"
)



st.markdown('<h3 style="color: #87CEEB;">Professional Summary</h3>', unsafe_allow_html=True)

st.write("""
Computer scientist with expertise in image processing using deep learning, research-driven decision skills and data analysis. Experienced in developing predictive models, conducting research, and collaborating on interdisciplinary projects. Committed to advancing scientific knowledge through data-driven insights.
""")

st.markdown('<h3 style="color: #87CEEB;">Education</h3>', unsafe_allow_html=True)
st.write("""
- **Master of Science in Computer Science**  
  University of Ibadan, (2021)  

- **Bachelor of Science Hounours(Ed) in Computer Science**  
  Ekiti State University, (2015) 

""")

st.markdown('<h3 style="color: #87CEEB;">Professional experience</h3>', unsafe_allow_html=True)
#st.markdown("### Professional Experience")
st.write("""
 **Student Assistant**  
  University of Ibadan, (2020)  
  
""")

# Skills
st.markdown('<h3 style="color: #87CEEB;">Skills</h3>', unsafe_allow_html=True)
#st.markdown("### Skills")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    - Python, SQL, Bash, Latex
    - Machine Learning 
    - Data Visualization
    - Image processing
    """)
with col2:
    st.write("""
    - Data analysis
    - Research skills
    """)

st.markdown('<h3 style="color: #87CEEB;">Languages</h3>', unsafe_allow_html=True)
st.write("""
 English: Fluent
""")

# Interests
st.markdown('<h3 style="color: #87CEEB;">Interests</h3>', unsafe_allow_html=True)
#st.markdown("### Interests")
st.write("""
- Research in AI and Machine Learning
- Open-source contributions
- Scientific literature and conferences
""")



st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")