from textblob import TextBlob

# Perform sentiment analysis and add 'sentiment_indicator' column
def get_sentiment_indicator(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity >= 0:
        return '✔️'
    else:
        return '❌'
