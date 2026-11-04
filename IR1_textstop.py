text = "The quick brown foxes  are jumping over the lazy dogs while running fast"

# 1. Stop words set
stop_words = {"the", "a", "an", "is", "are", "while", "over", "in", "on", "at", "to"}

# 2. Tokenization & Lowercasing
tokens = text.lower().split()

# 3. Stop Word Removal
filtered_tokens = [word for word in tokens if word not in stop_words]

# 4. Pure Python Suffix-Based Stemmer (Replaces NLTK PorterStemmer)
def simple_stemmer(word):
    suffixes = ['ing', 'es', 's', 'ed', 'ly', 'er']
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    return word

stemmed_tokens = [simple_stemmer(word) for word in filtered_tokens]

print("Original Tokens :", tokens)
print("After StopWords :", filtered_tokens)
print("After Stemming  :", stemmed_tokens)