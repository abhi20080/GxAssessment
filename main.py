# import gensim
from gensim.models import KeyedVectors
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Load Word2Vec model
# Need to download the `GoogleNews-vectors-negative300.bin.gz` and copy at the below path
wv = KeyedVectors.load_word2vec_format('Word2Vec/GoogleNews-vectors-negative300.bin.gz', binary=True, limit=1000000)
wv.save_word2vec_format('results/vectors.csv')
# wv = KeyedVectors.load_word2vec_format('vectors.csv')



# Load phrases
df = pd.read_csv('data/phrases.csv', encoding="ISO-8859-1")
phrases = df['Phrases'].tolist()

# Preprocess phrases
def preprocess(phrase):
    return word_tokenize(phrase.lower())

tokenized_phrases = [preprocess(phrase) for phrase in phrases]

# Compute phrase embeddings
def get_phrase_embedding(tokens):
    embeddings = [wv[word] for word in tokens if word in wv]
    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
        return np.zeros(wv.vector_size)

phrase_embeddings = [get_phrase_embedding(tokens) for tokens in tokenized_phrases]
# print(phrase_embeddings)


from sklearn.metrics.pairwise import cosine_similarity

# Calculate cosine similarity between each pair of phrase embeddings
similarity_matrix = cosine_similarity(phrase_embeddings)

# Create a DataFrame to store the similarity results
similarity_df = pd.DataFrame(similarity_matrix, index=phrases, columns=phrases)

# Save to CSV
similarity_df.to_csv('results/phrase_similarity.csv')

def find_closest_match(input_phrase):
    input_tokens = preprocess(input_phrase)
    input_embedding = get_phrase_embedding(input_tokens)
    similarities = cosine_similarity([input_embedding], phrase_embeddings)
    closest_index = np.argmax(similarities)
    result = {}
    result["closest_match"] = phrases[closest_index]
    result["distance"] = similarities[0][closest_index]
    return result

print(find_closest_match("What is the complete profile of the top oil rigs?"))