# ✉️ Smart Email Generator with Python, Streamlit, and Google Gemini API

Welcome to the **Smart Email Generator**! This project is designed specifically for beginners in Python and Generative AI development. It shows you how to build a fully functional, beautiful web application that uses Google's state-of-the-art Gemini 2.5 Flash model to draft custom emails.

---

## 🚀 Easy Setup Instructions (For Windows & VS Code)

Follow these simple steps to run the application on your computer:

### Step 1: Install Python
If you don't have Python installed, download and install it from the official website:
- [Download Python for Windows](https://www.python.org/downloads/)
- *Important:* During installation, make sure to check the box that says **"Add Python to PATH"**.

### Step 2: Open the Project in VS Code
1. Open **Visual Studio Code**.
2. Click **File -> Open Folder** and select this project directory.

### Step 3: Open the Terminal in VS Code
1. Open a new terminal in VS Code by going to the top menu and clicking **Terminal -> New Terminal** (or press ``Ctrl + ` ``).

### Step 4: Install Dependencies
Type the following command in your terminal and press **Enter** to install Streamlit and the Google Generative AI SDK:
```bash
pip install -r requirements.txt
```

### Step 5: Get Your Google Gemini API Key
To use the Gemini API, you need a free API Key:
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Click **Create API Key**.
3. Copy your key (it will look like `AIzaSy...`).

### Step 6: Set Your API Key (Environment Variable)
To keep your API key secure, we set it as an environment variable in the terminal:

**In PowerShell (Default in VS Code):**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**In Command Prompt (cmd):**
```cmd
set GEMINI_API_KEY=your_api_key_here
```

*(Replace `your_api_key_here` with the actual API Key you copied from Google).*

### Step 7: Run the Application!
Start your Streamlit web server by running this command in your terminal:
```bash
streamlit run app.py
```

Streamlit will automatically open a new tab in your web browser at `http://localhost:8501` showing your fully interactive Smart Email Generator!

---

## 📁 File Structure

- **`app.py`**: The main user interface of our app. It uses Streamlit components (like `st.text_input` and `st.button`) to collect user inputs, and displays the generated emails.
- **`email_generator.py`**: The logic file. It imports the Gemini API SDK, configures your API key, formats your prompt, sends it to Google, and returns the response.
- **`requirements.txt`**: A list of libraries needed to run the app.
