import nltk
nltk.download("all")
import streamlit as st
from textblob import TextBlob

# Config
st.set_page_config(
     page_title="Sentiment Analysis",
     page_icon="😀",
    #  layout="wide",
     initial_sidebar_state="expanded"
 )

def get_sentiment(value):
    if value > 0:
        return("😃 Positive")
    elif value < 0:
        return("😏 Negative")
    else:
        return("😐 Neutral")

st.title("Sentiment Analysis")

text = st.text_input("Masukkan Teks", "Saya pergi ke Paris tahun lalu. Saya membeli parfum baru.")

blob = TextBlob(text)
indo = blob.translate(from_lang="id", to="en")
sentiment = indo.sentiment
st.write(sentiment)

st.subheader("Sentiment:")

st.write(get_sentiment(indo.sentiment.polarity))

if blob.sentiment.subjectivity > 0.5:
    st.write("Personal opinion: ✅")
else:
    st.write("Personal opinion: ❌")

st.write(indo.sentiment)

st.subheader(f"Sentences: {len(indo.sentences)}")
st.write(indo.sentences)

st.subheader(f"Noun Phrase: {len(indo.noun_phrases)}")
st.write(indo.noun_phrases)

st.subheader(f"Words: {len(indo.words)}")
st.write(indo.words)

st.subheader(f"Lemmatize: {len(indo.words)}")
for item in indo.tags:
    if item[1] == "NN":
        st.write(item[0], "-->", item[1], "-->", item[0].pluralize())
    elif item[1] == "NNS":
        st.write(item[0], "-->", item[1], "-->", item[0].singularize())
    else:
        st.write(item[0], "-->", item[1], "-->1", item[0].lemmatize("v"))

st.subheader(f"Tags:")
st.write(indo.tags)

st.subheader("Sentiment by sentences:")
for sentence in indo.sentences:
    st.write(get_sentiment(sentence.sentiment.polarity), sentence)