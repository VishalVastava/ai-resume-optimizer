# 🧠 AI Resume Optimizer

An intelligent resume analyzer powered by Generative AI. This Streamlit web app compares your resume with a job description and provides personalized suggestions to improve your resume, helping you stand out in job applications.

---

## 🚀 Features

- 📄 Paste your resume and job description
- 🤖 Get AI-generated suggestions to better match the job
- 💡 Uses Google's FLAN-T5 GenAI model (lightweight and fast)
- 🌐 Runs locally or deploys to Streamlit Cloud in 1 click
- 🧪 Fully customizable for other resume/job use-cases

---

## ✨ Demo

![App Demo](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/assets/demo.gif)  
_(Replace with your actual demo if you upload a GIF)_

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) – Web app framework for Python
- [Transformers (Hugging Face)](https://huggingface.co/transformers/) – Pre-trained NLP models
- Model: [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small)

---

## 📦 Installation

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-optimizer.git
cd ai-resume-optimizer
```

### 2. Create & activate virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, use:

```bash
pip install streamlit transformers
```

---

## 🧪 Run the App Locally

```bash
streamlit run app.py
```

Then open the browser: [http://localhost:8501](http://localhost:8501)

---

## 🛰️ Deploy to Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and click "Deploy"

---

## 📁 File Structure

```
📦 ai-resume-optimizer/
├── app.py                # Main Streamlit app
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
```

---

## 📌 Example Prompt Sent to AI

```
Compare the resume and job description.
Suggest 3 resume improvements to better match the job description.

Resume:
[...Your Resume...]

Job Description:
[...Job Description...]
```

---

## 🙌 Contribution

Want to add more AI models, features, or UX improvements?  
Feel free to fork and contribute!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by [Your Name](https://github.com/YOUR_USERNAME)
