# AI Resume Analyzer 📄🤖

An AI-powered web application that analyzes resumes against job descriptions to calculate a match score and provide actionable improvement suggestions using NLP and AI.

---

## 📌 Overview

AI Resume Analyzer helps users understand how well their resumes align with specific job roles.

By uploading a resume PDF and entering a job description, the system:

- Extracts and processes resume text  
- Compares resume content with job requirements  
- Calculates a similarity-based match percentage  
- Generates AI-powered feedback for improvement  

This tool is designed to simulate ATS-style resume screening and provide meaningful insights.

---

## 🛠️ Tech Stack

**Frontend:**  
- React  
- Vite  

**Backend:**  
- Node.js / FastAPI  

**AI & Processing:**  
- PDF Parsing (pdf-parse)  
- NLP similarity scoring  
- LLM API for feedback  

**Tools:**  
- GitHub  
- Render (optional deployment)

---

## ✨ Features

- Upload resume in PDF format  
- Enter job description text  
- Automated resume text extraction  
- Match percentage scoring  
- AI-generated feedback on missing skills  
- Clean responsive UI with light/dark mode  

---

## 🏗️ System Workflow

1. User uploads resume and enters job description  
2. Backend extracts and cleans resume text  
3. NLP similarity algorithm compares texts  
4. AI analyzes gaps and provides feedback  
5. Results displayed on frontend  

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
