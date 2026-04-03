import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="CV Generator", page_icon="📝", layout="centered")

st.title("📝 Simple CV Generator")
st.write("Fill in your details and generate a professional PDF CV instantly!")

# --- Input Fields ---
st.header("Personal Information")
name = st.text_input("Full Name *", placeholder="John Doe")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile URL")
github = st.text_input("GitHub Profile URL")
summary = st.text_area("Professional Summary", height=120, placeholder="Write a short professional summary...")

st.header("Education")
education = st.text_area("Education", height=100, placeholder="BSc Computer Science, University of XYZ, 2024")

st.header("Work Experience")
experience = st.text_area("Work Experience", height=120, placeholder="Software Engineer, ABC Company, 2023 - Present")

st.header("Skills")
skills = st.text_area("Skills (comma separated)",
                      placeholder="Python, Streamlit, SQL, Git, Problem Solving, Team Leadership",
                      height=100)

# --- Generate PDF ---
if st.button("🚀 Generate CV PDF", type="primary", use_container_width=True):
    if not name or not name.strip():
        st.error("❌ Please enter your Full Name!")
    else:
        pdf = FPDF()
        pdf.add_page()
        
        # === Improved Unicode Support ===
        # Add a built-in font that works better, or fall back safely
        pdf.set_font("Helvetica", 'B', 20)   # Helvetica is more reliable than Arial in fpdf2
        pdf.cell(0, 15, name.strip(), ln=True, align='C')
        pdf.ln(8)
        
        pdf.set_font("Helvetica", '', 11)
        contacts = []
        if email: contacts.append(f"Email: {email}")
        if phone: contacts.append(f"Phone: {phone}")
        if linkedin: contacts.append(f"LinkedIn: {linkedin}")
        if github: contacts.append(f"GitHub: {github}")
        
        pdf.multi_cell(0, 8, " | ".join(contacts))
        pdf.ln(10)
        
        # Sections
        sections = [
            ("Professional Summary", summary),
            ("Education", education),
            ("Work Experience", experience),
            ("Skills", skills)
        ]
        
        for title, content in sections:
            pdf.set_font("Helvetica", 'B', 14)
            pdf.cell(0, 10, title, ln=True)
            pdf.set_font("Helvetica", '', 11)
            
            text = content.strip() if content and content.strip() else f"No {title.lower()} provided."
            
            # Clean text for safety (replace problematic characters)
            text = text.replace('–', '-').replace('—', '-').replace('’', "'").replace('‘', "'")
            
            pdf.multi_cell(0, 8, text)
            pdf.ln(8)
        
        pdf_file = f"{name.strip().replace(' ', '_')}_CV.pdf"
        pdf.output(pdf_file)
        
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📥 Download Your CV PDF",
                data=f,
                file_name=pdf_file,
                mime="application/pdf",
                use_container_width=True
            )
        
        st.success("✅ CV generated successfully!")

# --- Footer ---
st.markdown("---")
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
