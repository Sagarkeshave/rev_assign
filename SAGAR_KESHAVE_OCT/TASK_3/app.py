import os

import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_article(topic):

    # Generate the article using OpenAI API
    prompt = f"Write an informative article about {topic}."
    response = openai.Completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
    )
    article = response.choices[0].text.strip()
    return article

# Streamlit UI
st.title("Article Generator")

# User input for OpenAI API key and topic
api_key = st.text_input("Enter your OpenAI API key:")
topic = st.text_input("Enter the topic of the article:")

if api_key and topic:
    openai.api_key = api_key
    if st.button("Generate Article"):
        # Call the generate_article function and display the generated article
        article = generate_article(topic)
        st.subheader("Generated Article:")
        st.write(article)
        print(article)
else:
    st.warning("Please enter your OpenAI API key and the topic to generate the article.")
