import spacy

# Load Spacy for NLP
nlp = spacy.load("en_core_web_sm")

# Clean tag to remove generic words
def clean_tag(tag):
    return tag.lower().strip().replace("the ", "").replace("a ", "").replace("an ", "")

# Extract tags dynamically with lemmatization
def extract_tags_with_nlp(review):
    doc = nlp(review)
    tags = set()  # Use a set to avoid duplicates
    
    # Remove stop words before extracting noun chunks and other tokens
    for chunk in doc.noun_chunks:
        cleaned_tag = clean_tag(chunk.lemma_)
        if cleaned_tag not in {"it", "they", "we", "you", "ear"} and not nlp.vocab[cleaned_tag].is_stop:  # Exclude stop words and pronouns
            tags.add(cleaned_tag)
    
    for token in doc:
        # Include NOUN and exclude stop words, pronouns, and punctuation
        if token.pos_ == "NOUN" and not token.is_stop and not token.is_punct and token.pos_ not in {"PRON", "ADJ"}:
            cleaned_tag = clean_tag(token.lemma_)
            tags.add(cleaned_tag)

    return list(tags)

# Associate tags with reviews
def assign_tags(phrases, tags):
    return list(set(phrases) & set(tags))