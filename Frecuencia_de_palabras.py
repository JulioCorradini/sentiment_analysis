from Preprocezado_de_texto import preprocess_text
from nltk.tokenize import word_tokenize
from nltk import FreqDist

def extract_features(preprocess_text):
    features = {}
    words = word_tokenize(preprocess_text)
    word_freq = FreqDist(words)

    for word, freq in word_freq.items():
        features[word] = freq

    return features