import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the T5 model and tokenizer
@st.cache_resource
def load_model():
    st.write("Loading model...")
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    st.write("Model loaded.")
    return tokenizer, model

tokenizer, model = load_model()

def summarize_text(article_text):
    # Preprocess the input text
    inputs = tokenizer.encode("summarize: " + article_text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate the summary
    summary_ids = model.generate(inputs, max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
    
    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Streamlit app
st.title("PubMed Article Summarizer")

# Text input for PubMed article
article = st.text_area("Enter PubMed Article", height=300)

# Placeholder for the summary
summary_placeholder = st.empty()

# Summarize button
if st.button("Summarize"):
    if article.strip() == "":
        st.warning("Please enter a PubMed article to summarize.")
    else:
        summary = summarize_text(article)
        summary_placeholder.text_area("Summarized Article", summary, height=200)
