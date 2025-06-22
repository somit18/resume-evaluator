import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation and digits
    text = ''.join([char for char in text if char not in string.punctuation and not char.isdigit()])

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [word for word in tokens if word not in stop_words]

    return cleaned_tokens

# Example usage:
if __name__ == "__main__":
    sample_text = "This is a sample resume text mentioning Python, teamwork, and data analysis."
    cleaned = preprocess_text(sample_text)
    print(cleaned)
