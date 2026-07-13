# email_generator.py
# -----------------
# This file handles the communication with the Google Gemini API.
# It takes user details (sender, recipient, purpose, details, tone, etc.) 
# and builds a prompt, then sends it to the Gemini API to get a response.

import os
from dotenv import load_dotenv
import google.generativeai as genai

def generate_email_with_gemini(recipient_name, sender_name, email_purpose, additional_details, email_type, tone, length):
    """
    This function connects to the Google Gemini API and generates an email
    based on the inputs provided by the user.
    """
    
    # Step 1: Retrieve the API Key from the environment variables.
    # We store the API key in an environment variable named GEMINI_API_KEY for security.
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Step 2: Validate that the API key exists.
    # If the API key is missing, we raise an error to inform the user.
    if not api_key:
        api_key=st.secrets["GEMINI_API_KEY"]
    # Step 3: Configure the Gemini SDK with our API key.
    genai.configure(api_key=api_key)
    
    # Step 4: Define the prompt that we will send to Gemini.
    # We carefully format this string to give clear instructions to the AI model.
    prompt = f"""
You are an expert email assistant. Please write a high-quality email using the following instructions:

Recipient Name: {recipient_name}
Sender Name: {sender_name}
Email Type: {email_type} (e.g., Leave Request, Job Application, Complaint, etc.)
Purpose: {email_purpose}
Additional Details/Context: {additional_details}
Tone: {tone} (e.g., Professional, Friendly, Polite)
Length: {length} (Short, Medium, or Long)

Strict Output Format:
Your output MUST follow this exact format. Do not write any introduction or conclusion lines outside of this format:

[SUBJECT]
(Write a compelling, appropriate email subject line here)

[BODY]
(Write the complete, highly formatted email body here. Use line breaks and spaces appropriately. Do not use generic placeholders like [Your Name] or [Recipient Name], use the names provided above!)
"""

    try:
        # Step 5: Initialize the Gemini model.
        # We use the fast and highly capable "gemini-2.5-flash" model.
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Step 6: Call the API to generate the text response.
        response = model.generate_content(prompt)
        
        # Step 7: Extract and clean up the text response.
        response_text = response.text.strip()
        
        # Step 8: Parse the output to separate the Subject from the Body.
        # We look for the [SUBJECT] and [BODY] markers we asked for in the prompt.
        subject = "Generated Email"
        body = response_text
        
        if "[SUBJECT]" in response_text and "[BODY]" in response_text:
            # We split the text by the markers to extract the exact strings
            parts = response_text.split("[BODY]")
            subject_part = parts[0].replace("[SUBJECT]", "").strip()
            body_part = parts[1].strip()
            
            subject = subject_part
            body = body_part
            
        return subject, body
        
    except Exception as error:
        # If any error occurs (network issues, API errors, etc.), we pass it back.
        raise Exception(f"Failed to generate email: {str(error)}")
