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

The application expects a CSV file (`data/d.csv`) with customer reviews and ratings. The file should have the following columns:

* `review`: The text of the customer review.(This is a mandatory column)
* `rating`: The rating given by the customer.(not a mandatory column)