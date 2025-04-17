# Review-Insight: A Customer Review Analysis Tool

## Overview

Review-Insight is a powerful tool designed to analyze customer reviews and extract meaningful insights through natural language processing and sentiment analysis. This application helps businesses understand customer feedback at scale by automatically identifying key topics (tags) mentioned in reviews and analyzing the sentiment associated with each topic.

Using Review-Insight, you can:

* Automatically extract common themes and topics from large volumes of customer reviews
* Analyze sentiment around specific product features or aspects
* Identify areas of strength and opportunities for improvement
* Track customer sentiment trends over time

In the provided dataset example, Review-Insight analyzes reviews for headphones, identifying key aspects like sound quality, comfort, battery life, design, and more - along with whether customers feel positively or negatively about each aspect.

## Key Features

* **Automated Tag Extraction**: Identifies the most relevant topics and features mentioned in reviews
* **Sentiment Analysis**: Determines whether reviews express positive or negative sentiments about specific features
* **Interactive Visualization**: Displays tag frequency and associated sentiment in an easy-to-understand format
* **Scalable Processing**: Handles large datasets with thousands of reviews
* **Customizable Analysis**: Allows adjustment of tag extraction parameters and sentiment thresholds

## Sample Output

After processing reviews, Review-Insight provides:

* A list of the most commonly mentioned product features/aspects
* The sentiment distribution for each feature (positive vs. negative)
* Representative review excerpts for each feature
* Overall sentiment metrics across all reviews

## Steps to Run

``` python
streamlit run code/app.py
```

It will take around 2 to 3 minutes to run completely (depending on data size).

## Approach to Generate Tags

The application processes customer reviews to extract and analyze tags, and then performs sentiment analysis on these tags. Below is a detailed explanation of the approach used:

1. **Extract Tags**:
    * The `extract_tags_with_nlp` function in `extract_tags.py` uses the Spacy NLP library to extract tags from reviews. It identifies noun chunks and individual nouns, cleans them, and removes generic words and stop words.
    * The `assign_tags` function associates the extracted tags with the corresponding reviews.
2. **Process Tags**:
    * The `process_tags` function in `tag_processing.py` processes all extracted tags to filter out common words and sorts them by frequency. It then limits the tags to the most relevant ones based on a specified threshold and maximum number of tags.
3. **Sentiment Analysis**:
    * The `get_sentiment_indicator` function in `sentiment_analysis.py` uses the TextBlob library to perform sentiment analysis on each review. It assigns a sentiment indicator ('✔️' for positive and '❌' for negative) based on the polarity of the review.
4. **Aggregate Sentiments**:
    * The `aggregate_sentiments` function in `tag_processing.py` aggregates sentiment indicators for each tag to determine the overall sentiment (positive or negative) for that tag.
5. **Streamlit Application**:
    * The `app.py` file integrates all the above functionalities into a Streamlit application. It loads and processes the data, extracts and processes tags, performs sentiment analysis, and displays the results in an interactive web interface.

## File Descriptions

* <b>`code/extract_tags.py`</b>: Contains functions to extract and clean tags from reviews using Spacy.
* <b>`code/tag_processing.py`</b>: Contains functions to process tags and aggregate sentiments.
* <b>`code/sentiment_analysis.py`</b>: Contains functions to perform sentiment analysis using TextBlob.
* <b>`code/app.py`</b>: The main Streamlit application file that integrates all functionalities and provides an interactive interface.

## Data

The application expects a CSV file (`data/data.csv`) with customer reviews and ratings. The file should have the following columns:

* `review`: The text of the customer review.(This is a mandatory column)
* `rating`: The rating given by the customer.(not a mandatory column)