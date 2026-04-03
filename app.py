# app.py
import streamlit as st
from fpdf import FPDF

# --- Page Config ---
st.set_page_config(page_title="CV Generator", page_icon="📝", layout="centered")
st.title("📝 Simple CV Generator")
st.write("Fill in your details and generate a PDF CV!")

# --- Input Fields ---
st.header("Personal Information")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile URL")
github = st.text_input("GitHub Profile URL")
summary = st.text_area("Professional Summary", height=100)

st.header("Education")
education = st.text_area("List your education (e.g., degree, university, year)", height=100)

st.header("Work Experience")
experience = st.text_area("List your work experience (e.g., company, role, duration)", height=100)

st.header("Skills")
skills = st.text_area("List your skills (comma separated)")

# --- Generate PDF ---
if st.button("Generate CV PDF"):
    if not name:
        st.warning("Please enter your name!")
    else:
        pdf = FPDF()
        pdf.add_page()
        
        # Personal Info
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, name, ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Email: {email}", ln=True)
        pdf.cell(0, 10, f"Phone: {phone}", ln=True)
        pdf.cell(0, 10, f"LinkedIn: {linkedin}", ln=True)
        pdf.cell(0, 10, f"GitHub: {github}", ln=True)
        pdf.ln(5)
        
        # Professional Summary
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Professional Summary", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 8, summary)
        pdf.ln(2)
        
        # Education
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Education", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 8, education)
        pdf.ln(2)
        
        # Work Experience
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Work Experience", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 8, experience)
        pdf.ln(2)
        
        # Skills
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Skills", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 8, skills)
        
        # Save PDF
        pdf_file = f"{name.replace(' ', '_')}_CV.pdf"
        pdf.output(pdf_file)
        
        # Download Button
        with open(pdf_file, "rb") as f:
            st.download_button("Download CV PDF", f, file_name=pdf_file, mime="application/pdf")
        st.success("CV generated successfully!")

# --- Footer ---
st.markdown(
    """
    <div style="margin-top: 50px; padding: 20px; text-align: center; border-top: 1px solid #ccc;">
        <p style="color: #e8000d; font-family: sans-serif; letter-spacing: 1px; font-size: 14px;">
            Created by Wesly Jeyananthan Abisha ❤️
        </p>
        <div style="display: flex; gap: 24px; justify-content: center; flex-wrap: wrap;">
            <a href="https://github.com/Abisha71" target="_blank" style="text-decoration: none; color: #000;">GitHub</a>
            <a href="https://www.linkedin.com/in/abisha-wesly-jeyananthan-2a05a32b8" target="_blank" style="text-decoration: none; color: #0077b5;">LinkedIn</a>
            <a href="https://www.facebook.com/share/18DbpQMBMf/" target="_blank" style="text-decoration: none; color: #4267B2;">Facebook</a>
            <a href="https://youtube.com/@shaabi-u5k?feature=shared" target="_blank" style="text-decoration: none; color: #FF0000;">YouTube</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
