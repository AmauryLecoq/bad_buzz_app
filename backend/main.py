# Vérifier l'installation : pip install fastapi uvicorn

# 1. Import des packages
import uvicorn

from fastapi import FastAPI

import numpy as np
import pandas as pd

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
from nltk.stem.snowball import EnglishStemmer

import spacy
#import en_core_web_sm

import re

import tensorflow as tf

from Tweet import Tweet

# 2. Création de l'objet app et import model
app = FastAPI()
model_dir = "export_model"
model = tf.keras.models.load_model(model_dir)

# 3. Index route, s'ouvre automatiquement sur http://127.0.0.1:8000
@app.get('/')
def index():
    return {"Bienvenue sur l'app de prédiction"}

# 4. Préparation de la page de prédiction

@app.post('/predict')
def predict_tweet(data: Tweet):
    data = data.dict()
    tweet = data['tweet']
    prediction = model.predict([tweet])
    print(prediction)
    if (prediction[0]>0.5):
        prediction = 'Ceci est un Tweet positif!'
    else :
        prediction="Ceci est un Tweet négatif!"
    return prediction


# Lancer l'api avec unicorn
# sera lancer sur http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host ="127.0.0.1", port=8000)

# uvicorn <nom du fichier actuel>:app --reload