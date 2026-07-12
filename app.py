# app.py
# ------
# This is the main file for our Streamlit web application.
# It handles drawing the text inputs, selection boxes, buttons, and display cards 
# right in the browser, and connects them with our email generator logic.
#
# Enhanced with elegant custom CSS, a beautiful header, cards, and professional layout.

import streamlit as st
import os
from email_generator import generate_email_with_gemini

# Step 1: Set the title and layout of the page.
# This gives the browser tab a name and configures a clean, user-friendly layout.
st.set_page_config(
    page_title="Smart Email Generator",
    page_icon="✉️",
    layout="centered"
)

# Step 2: Inject Custom CSS for beautiful UI styling
st.markdown("""
<style>
  /* Import elegant typography */
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  /* Global style overrides */
  html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) !important;
  }

  /* Beautiful Custom Gradient Header */
  .custom-header {
    background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
    padding: 3rem 2rem;
    border-radius: 20px;
    color: white;
    box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.15);
    margin-bottom: 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  
  .custom-header::after {
    content: '';
    position: absolute;
    top: -30%;
    right: -20%;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
  }

  .custom-header h1 {
    font-size: 2.5rem !important;
    font-weight: 800 !important;
    margin: 0 0 0.5rem 0 !important;
    color: white !important;
    letter-spacing: -0.03em !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .custom-header p {
    font-size: 1.05rem !important;
    color: #e0e7ff !important;
    margin: 0 !important;
    max-width: 600px;
    margin-left: auto !important;
    margin-right: auto !important;
    font-weight: 400 !important;
    line-height: 1.5 !important;
  }

  /* Style st.container(border=True) as attractive modern cards */
  div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 20px !important;
    padding: 2.25rem !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.02), 0 4px 6px -4px rgba(0, 0, 0, 0.02), 0 1px 3px 0 rgba(0, 0, 0, 0.01) !important;
    margin-bottom: 2rem !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
  }

  div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.04), 0 10px 10px -5px rgba(0, 0, 0, 0.02) !important;
  }

  /* Custom Section Headings */
  .card-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  /* Widget labels style customization */
  label[data-testid="stWidgetLabel"] p {
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    color: #475569 !important;
    margin-bottom: 6px !important;
  }

  /* Inputs, Textareas, Selectboxes customization */
  .stTextInput input, .stTextArea textarea, .stSelectbox select {
    border-radius: 12px !important;
    border: 1px solid #cbd5e1 !important;
    padding: 0.7rem 0.95rem !important;
    background-color: #f8fafc !important;
    color: #0f172a !important;
    transition: all 0.2s ease-in-out !important;
    font-size: 0.92rem !important;
  }

  .stTextInput input:hover, .stTextArea textarea:hover, .stSelectbox select:hover {
    border-color: #94a3b8 !important;
    background-color: #ffffff !important;
  }

  .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus {
    border-color: #4f46e5 !important;
    background-color: #ffffff !important;
    box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.12) !important;
  }

  /* Button common styling */
  div.stButton > button {
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: 0.75rem 2rem !important;
    font-size: 0.95rem !important;
    letter-spacing: -0.01em !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    height: auto !important;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    width: 100% !important;
  }

  /* Generate Button (Primary) */
  div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25) !important;
  }

  div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #4338ca 0%, #2563eb 100%) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(79, 70, 229, 0.35) !important;
  }

  div.stButton > button[kind="primary"]:active {
    transform: translateY(1px) !important;
  }

  /* Clear Button (Secondary) */
  div.stButton > button[kind="secondary"], div.stButton > button:not([kind="primary"]) {
    background-color: #ffffff !important;
    color: #64748b !important;
    border: 1px solid #e2e8f0 !important;
  }

  div.stButton > button[kind="secondary"]:hover, div.stButton > button:not([kind="primary"]):hover {
    color: #0f172a !important;
    background-color: #f8fafc !important;
    border-color: #cbd5e1 !important;
  }

  /* Generated Subject Highlight box */
  .subject-highlight {
    background-color: #f8fafc;
    border-left: 4px solid #4f46e5;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    font-weight: 600;
    color: #0f172a;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.02);
  }

  /* Footer Styling */
  .custom-footer {
    text-align: center;
    padding: 2.5rem 0;
    color: #64748b;
    font-size: 0.875rem;
    border-top: 1px solid #e2e8f0;
    margin-top: 4rem;
    line-height: 1.6;
  }
  
  .custom-footer a {
    color: #4f46e5;
    text-decoration: none;
    font-weight: 600;
  }
  
  .custom-footer a:hover {
    text-decoration: underline;
  }

  /* Responsive Spacing & Page layout fixes */
  .block-container {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }
</style>
""", unsafe_allow_html=True)

# Step 3: Initialize Session State variables if they don't exist yet.
# Streamlit reruns the whole file from top to bottom on every user action.
# Session State helps us "remember" values between runs, like the generated email.
if "subject" not in st.session_state:
    st.session_state.subject = ""
if "body" not in st.session_state:
    st.session_state.body = ""

# Step 4: Define a helper function to clear all input fields.
# We reset our input keys in st.session_state and empty the generated email.
def clear_all_inputs():
    st.session_state.recipient = ""
    st.session_state.sender = ""
    st.session_state.purpose = ""
    st.session_state.details = ""
    st.session_state.subject = ""
    st.session_state.body = ""

# Step 5: Draw the Application Header.
# We use modern HTML/CSS with gradient backing for a stunning user experience.
st.markdown("""
    <div class="custom-header">
        <div style="font-size: 2.75rem; margin-bottom: 0.75rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.15));">✉️</div>
        <h1>Smart Email Generator</h1>
        <p>A beginner-friendly playground powered by the Google Gemini API to write perfect, customized emails in seconds.</p>
    </div>
""", unsafe_allow_html=True)

# Step 6: Create the Input Details Form inside an attractive card container.
with st.container(border=True):
    st.markdown('<div class="card-title">📝 Configure Your Email</div>', unsafe_allow_html=True)
    
    # We use columns to align fields elegantly.
    col1, col2 = st.columns(2)
    
    with col1:
        recipient_name = st.text_input(
            "Recipient Name", 
            key="recipient", 
            placeholder="e.g., Jane Smith, HR Team, Professor Oak"
        )
        
    with col2:
        sender_name = st.text_input(
            "Sender Name", 
            key="sender", 
            placeholder="e.g., Alex Johnson, Your Student"
        )

    # Email Type selector using selectbox
    email_type = st.selectbox(
        "Select Email Type",
        ["Formal", "Leave Request", "Job Application", "Thank You", "Complaint", "Meeting Request"]
    )

    # Text area for the core purpose of the email
    email_purpose = st.text_area(
        "What is the main purpose of this email?",
        key="purpose",
        placeholder="e.g., Requesting 2 days off starting Tuesday due to personal family matters, or thanking them for the interview last Friday."
    )

    # Text area for optional details
    additional_details = st.text_area(
        "Additional Details or Specific Bullet Points (Optional)",
        key="details",
        placeholder="e.g., Include dates, attach my resume references, mention I am available anytime on Wednesday afternoons."
    )

    # Let the user choose Tone and Length in a side-by-side split
    col3, col4 = st.columns(2)

    with col3:
        tone = st.selectbox(
            "Select Tone",
            ["Professional", "Friendly", "Polite"]
        )
        
    with col4:
        length = st.selectbox(
            "Select Length",
            ["Short", "Medium", "Long"]
        )

# Step 7: Create the Action Buttons.
# We arrange the buttons beautifully inside a column grid layout.
btn_col1, btn_col2 = st.columns([1, 4])

# We keep track of whether the user clicked the generate button
generate_clicked = False

with btn_col1:
    # A clear button to wipe all fields
    st.button("🧹 Clear All", on_click=clear_all_inputs)

with btn_col2:
    # The primary styled button to trigger email generation
    if st.button("🚀 Generate Email", type="primary"):
        # Ensure mandatory fields are filled out first
        if not recipient_name or not sender_name or not email_purpose:
            st.error("⚠️ Please fill in Recipient Name, Sender Name, and Email Purpose!")
        else:
            generate_clicked = True

# Step 8: Generate the Email using our Gemini model backend helper.
if generate_clicked:
    # We use st.spinner to display a professional loading screen while generating
    with st.spinner("🧠 Gemini is crafting your perfect email... please wait."):
        try:
            # We call the function from email_generator.py to query Gemini
            subject, body = generate_email_with_gemini(
                recipient_name=recipient_name,
                sender_name=sender_name,
                email_purpose=email_purpose,
                additional_details=additional_details,
                email_type=email_type,
                tone=tone,
                length=length
            )
            
            # Save the results into Session State so they don't vanish on page reruns
            st.session_state.subject = subject
            st.session_state.body = body
            st.success("🎉 Email generated successfully!")
            
        except Exception as error:
            # Show a friendly, helpful error message to the beginner developer
            st.error(f"❌ An error occurred: {str(error)}")
            st.info("💡 Hint: Please make sure you have set your GEMINI_API_KEY environment variable correctly.")

# Step 9: Display the generated Subject and Email Body in a beautiful Output Card.
if st.session_state.subject or st.session_state.body:
    with st.container(border=True):
        st.markdown('<div class="card-title">📝 Your Generated Email</div>', unsafe_allow_html=True)
        
        # Render the subject inside a styled accent block
        st.markdown(f'<div class="subject-highlight"><strong>Subject:</strong> {st.session_state.subject}</div>', unsafe_allow_html=True)
        
        # Render the email body in a clean text box container
        st.text_area(
            label="Email Body", 
            value=st.session_state.body, 
            height=300,
            disabled=False, # Lets users select and copy text directly
            help="You can copy this text directly or edit it!"
        )
        
        # Build the exact plain text payload for downloading
        full_email_text = f"Subject: {st.session_state.subject}\n\n{st.session_state.body}"
        
        # Provide a premium download button
        st.download_button(
            label="📥 Download Email (.txt)",
            data=full_email_text,
            file_name="generated_email.txt",
            mime="text/plain"
        )

# Step 10: Create a professional and clean Footer
st.markdown("""
    <div class="custom-footer">
        <p>Smart Email Generator • Developed with 🐍 Python, ⚡ Streamlit & 🧠 Google Gemini API</p>
        <p style="font-size: 0.75rem; margin-top: 0.5rem; color: #94a3b8;">Created with love for beginner developers. Connect to the Google AI Studio to request edits!</p>
    </div>
""", unsafe_allow_html=True)

