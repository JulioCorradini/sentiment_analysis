from nltk.classify import NaiveBayesClassifier

from Preprocezado_de_texto import preprocess_text
from Frecuencia_de_palabras import extract_features
from Datos_de_entrenamiento import training_data

# Preprocesamiento de los datos de entrenamiento
preprocessed_training_data = [(preprocess_text(text), label) for text, label in training_data]

# Extracción de características de los datos de entrenamiento
training_features = [(extract_features(text), label) for text, label in preprocessed_training_data]

# Entrenamiento del clasificador Naive Bayes
classifier = NaiveBayesClassifier.train(training_features)

########################### Clasificación de un nuevo texto ###########################

# Nuevo texto para clasificar
##new_text = "It is a error"

# Preprocesamiento del nuevo texto
##preprocessed_text = preprocess_text(new_text)

# Extracción de características del nuevo texto
##features = extract_features(preprocessed_text)

# Clasificación del nuevo texto
##sentiment = classifier.classify(features)
##print("Sentiment:", sentiment)