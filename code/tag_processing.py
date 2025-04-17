from collections import Counter

# Define common words to exclude from tags
common_words = {"product", "item", "thing", "stuff", "something"}

# Process tags and get relevant tags
def process_tags(all_tags, threshold=0.01, max_tags=7):
    tag_counts = Counter(all_tags)
    total_tags = sum(tag_counts.values())
    # Sort tags by frequency and filter out common words
    sorted_tags = sorted(
        [phrase for phrase, count in tag_counts.items() if phrase not in common_words],
        key=lambda x: tag_counts[x],
        reverse=True
    )
    # Limit to the most relevant tags
    tags = sorted_tags[:max_tags]
    return tags

# Aggregate sentiment indicators for each tag
def aggregate_sentiments(tag_reviews):
    tag_sentiments = {}
    for tag, reviews in tag_reviews.items():
        positive_count = (reviews['sentiment_indicator'] == '✔️').sum()
        negative_count = (reviews['sentiment_indicator'] == '❌').sum()
        
        if positive_count > negative_count:
            overall_sentiment = '✔️ Positive'
        else:
            overall_sentiment = '❌ Negative'
        
        tag_sentiments[tag] = overall_sentiment
    return tag_sentiments