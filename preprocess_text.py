import string

def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split into words (simple tokenizer)
    tokens = text.split()

    # Remove common English stopwords manually (no nltk)
    stopwords = set([
        "the", "and", "is", "in", "to", "a", "of", "for", "on", "with",
        "that", "as", "are", "it", "by", "from", "at", "an", "be", "or"
    ])
    tokens = [word for word in tokens if word not in stopwords]

    return tokens
