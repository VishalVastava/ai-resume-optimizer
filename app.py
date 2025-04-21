import streamlit as st
from transformers import pipeline

# Page settings
st.set_page_config(page_title="AI Resume Optimizer", page_icon="🧠")

st.title("📄 AI Resume Optimizer")
st.write("Match your resume with job descriptions using GenAI")

# Input boxes
resume = st.text_area("🧑‍💼 Paste Your Resume Here", height=250)
job_desc = st.text_area("💼 Paste Job Description Here", height=250)

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

generator = load_model()

# Button to generate suggestions
if st.button("🔍 Analyze & Suggest Improvements"):
    if resume and job_desc:
        with st.spinner("Analyzing..."):
            prompt = (
                f"Compare the resume and job description. "
                f"Suggest 3 resume improvements to better match the job description.\n\n"
                f"Resume:\n{resume}\n\nJob Description:\n{job_desc}"
            )
            result = generator(prompt, max_length=300, clean_up_tokenization_spaces=True)[0]["generated_text"]
            st.success("✅ Suggestions Ready!")
            st.markdown("### 💡 Suggestions:")
            st.write(result)
    else:
        st.warning("⚠️ Please enter both resume and job description.")
