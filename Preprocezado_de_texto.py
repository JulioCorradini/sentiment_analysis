import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Procesado de texto
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

def preprocess_text(text):
    # Tokenización
    tokens = word_tokenize(text)

    # Eliminación de signos de puntuación
    tokens = [token for token in tokens if token not in string.punctuation]

    # Conversión a minúsculas
    tokens = [token.lower() for token in tokens]

    # Eliminación de stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lematización
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Reconstrucción del texto preprocesado
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text