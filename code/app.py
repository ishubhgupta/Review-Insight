import streamlit as st
import pandas as pd
from extract_tags import extract_tags_with_nlp, assign_tags
from sentiment_analysis import get_sentiment_indicator
from tag_processing import process_tags, aggregate_sentiments

# Streamlit app title
st.title("Tag and Sentiment Analysis")

# Text input for CSV file path
file_path = st.text_input("Enter the path to the CSV file", "data/data.csv")

@st.cache_data
def load_and_process_data(file_path):
    # Load data from CSV file
    data = pd.read_csv(file_path)

    # Extract tags from all reviews
    all_tags = []
    for review in data['review']:
        all_tags.extend(extract_tags_with_nlp(review))

    # Process tags and get relevant tags
    tags = process_tags(all_tags)[:7]

    # Associate tags with reviews
    data['tags'] = data['review'].apply(lambda review: assign_tags(extract_tags_with_nlp(review), tags))

    # Perform sentiment analysis and add 'sentiment_indicator' column
    data['sentiment_indicator'] = data['review'].apply(get_sentiment_indicator)

    # Create a tag to reviews mapping
    tag_reviews = {tag: data[data['tags'].apply(lambda x: tag in x)] for tag in tags}

    # Aggregate sentiment indicators for each tag
    tag_sentiments = aggregate_sentiments(tag_reviews)

    return data, tags, tag_reviews, tag_sentiments

# Process data only when file path is submitted or changed
if "processed_data" not in st.session_state and file_path:
    with st.spinner('Processing data...'):
        st.session_state.data, st.session_state.tags, st.session_state.tag_reviews, st.session_state.tag_sentiments = load_and_process_data(file_path)
        st.session_state.processed_data = True

# Display results if data has been processed
if "processed_data" in st.session_state:
    # Display tags and their sentiments
    st.header("Tags and Sentiments")
    for tag, sentiment in st.session_state.tag_sentiments.items():
        st.write(f"**{tag}**: {sentiment}")

    # Select a tag to view reviews
    selected_tag = st.selectbox("Select a tag to view reviews", st.session_state.tags)

    if selected_tag:
        st.header(f"Reviews for tag: {selected_tag}")
        filtered_reviews = st.session_state.tag_reviews.get(selected_tag, pd.DataFrame())
        for review in filtered_reviews['review'].tolist():
            st.write(review)