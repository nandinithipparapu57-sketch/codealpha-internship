import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is AI?",
    "What is Machine Learning?",
    "What is Python?",
    "What is Deep Learning?",
    "What is Data Science?",
    "What is NLP?",
    "What is ChatGPT?",
    "What is Computer Vision?"
]

answers = [
    "AI stands for Artificial Intelligence. It enables machines to mimic human intelligence.",
    "Machine Learning is a subset of AI that allows systems to learn from data.",
    "Python is a popular programming language used in AI, web development, and data science.",
    "Deep Learning is a branch of Machine Learning that uses neural networks.",
    "Data Science is the process of extracting insights from data.",
    "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "ChatGPT is an AI chatbot developed by OpenAI.",
    "Computer Vision enables computers to understand and analyze images and videos."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

st.title("🤖 FAQ Chatbot")

user_question = st.text_input("Ask a Question")

if user_question:
    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vector, X)
    best_match = similarity.argmax()
    best_score = similarity[0][best_match]

    if best_score < 0.2:
        st.warning("Sorry, I don't have an answer for that. Try asking about AI, ML, Python, etc.")
    else:
        st.success("Bot Response:")
        st.write(answers[best_match])