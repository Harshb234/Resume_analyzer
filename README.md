# Resume_analyzer
# 🤖 AI Career Coach – Resume Analyzer & Interview Simulator

A next-generation AI-powered application that analyzes resumes, simulates recruiter interviews, and provides tailored feedback. This tool mimics real-world job screening, helping users prepare for technical and behavioral interviews using their own resume data.


---

## 🚀 Features

- 📄 **Resume Parser**: Upload a PDF resume and extract structured data (skills, experience, projects).
- 🧠 **AI-Powered Feedback**: Analyze resume against job-specific keywords and provide suggestions.
- 🎭 **Mock Interviews**: Simulate recruiter personas that ask role-based questions derived from the resume.
- 💬 **Real-Time Coaching**: Get intelligent feedback on your answers.
- 🌐 **Modern UI**: Sleek glassmorphism-inspired dark-mode design using Bootstrap 5+.
- 🔊 **Optional Voice Mode**: Let the bot talk back to you using text-to-speech.

---

## 📁 Project Structure


resume-coach/
├── app.py                # Flask app entry point
├── resume_parser.py      # PDF to text extractor
├── analyzer.py           # Keyword analysis logic
├── ai_interviewer.py     # Interview simulation engine
├── static/               # CSS, images, JS
├── templates/
│   └── index.html        # Main UI (Bootstrap-based)
├── uploads/              # Uploaded resumes
├── requirements.txt      # Dependencies
└── README.md             # This file



🔧 Installation & Setup
1. Clone the Repo

git clone https://github.com/yourusername/resume-coach.git

2. Install Dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm



3. Run the App

python app.py
Visit http://127.0.0.1:5000 in your browser.

🧠 Powered By
OpenAI GPT API

spaCy

Flask

Bootstrap

PyPDF2

[TTS Engines] (Optional: pyttsx3, gTTS)



🧑‍💻 Author
Your Name – @harsh_bambatkar

