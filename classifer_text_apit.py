# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:05:46 2024

@author: serv5cgpepe
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re, string
from langdetect import detect, detect_langs
from googletrans import Translator
import matplotlib.pyplot as plt


#Modelo de PLN 
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')

#Se importan las herramientas necesarias para el modelo de clasificación
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize

inicio = time.time()

#Lista de publicaciones de Instagram
posts = ['https://www.instagram.com/p/C7LYI_rvwrP/', 'https://www.instagram.com/p/C6jE6boN0Lc/', 'https://www.instagram.com/p/C6boyNKOqqT/', 'https://www.instagram.com/p/C7WdJEdh6La/', 'https://www.instagram.com/p/C7O8ymZR4_2/', 'https://www.instagram.com/p/C7T9hWvJ66F/', 'https://www.instagram.com/p/C5IfHx5Iyso/', 'https://www.instagram.com/p/C7R08dLJZ5e/', 'https://www.instagram.com/p/C7UbHtGpyed/', 'https://www.instagram.com/p/C7PmrJptZMC/', 'https://www.instagram.com/p/C7ZgEu7MAeF/', 'https://www.instagram.com/p/C6WTGOkuM2B/', 'https://www.instagram.com/p/C7PUU0bitwl/', 'https://www.instagram.com/p/C6248uOi3x5/', 'https://www.instagram.com/p/C6eNYohLQfA/', 'https://www.instagram.com/p/C7a3OJtCDEQ/', 'https://www.instagram.com/p/C7WoMRCo1tz/', 'https://www.instagram.com/p/C7hBNwYoKZm/', 'https://www.instagram.com/p/C7hFdXCxrD1/', 'https://www.instagram.com/p/C6nTOIxIPmb/', 'https://www.instagram.com/p/C7OeA05o8LF/', 'https://www.instagram.com/p/C6_XHb8Bz6K/', 'https://www.instagram.com/p/C5p-17QMAXR/', 'https://www.instagram.com/p/C6xd-Yhrqym/', 'https://www.instagram.com/p/C6EBzh1CtXj/', 'https://www.instagram.com/p/C7USWgtsQTE/', 'https://www.instagram.com/p/C6--UzdKtkp/', 'https://www.instagram.com/p/C7ggdbjCOp7/']
driver = webdriver.Chrome()

#Texto en los post
texto_posts = []

#Iteración de los posts
i = 0
for post in posts:
    url = post
    driver.get(url)
    time.sleep(5)
    if i == 0:     
        cerrar_ventana = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div/div/div[1]/div/button').click()
        time.sleep(5)
    texto_posts.append(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/div[1]/li/div/div/div[2]/div[1]/h1').text)
    time.sleep(5)
    print(i)
    i = i+1
    #driver.close()

analizador = SentimentIntensityAnalyzer()
listaFinalIngles = []

#Eliminamos los signos de puntuación, así como los números para no tener problemas con la traducción
def quitar_numeros(texto):
    return ''.join(caracter for caracter in texto if not caracter.isdigit())

def quitar_signos(texto):
    translator = str.maketrans('', '', string.punctuation)
    return texto.translate(translator)

def quitar_signos_de_exclamacion(text, replace):
    return re.sub('[%s]' % re.escape(string.punctuation), replace, text)

def quitar_emojis(texto):
    # Definir el patrón regex para los emojis
    patron = re.compile("["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Símbolos y pictogramas
        u"\U0001F680-\U0001F6FF"  # Transporte y símbolos de mapas
        u"\U0001F1E0-\U0001F1FF"  # Banderas
        u"\U00002500-\U00002BEF"  # Otros símbolos
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # Variación de selección
        u"\u3030"
        "]+", re.UNICODE)
    return re.sub(patron, '', texto)

frases = []
for elemento in texto_posts: #Iteramos la lista de la cual queremos obtener la nube de palabras
    elemento = quitar_numeros(elemento) #Eliminamos números
    elemento = quitar_signos(elemento) #Eliminamos signos de puntuación
    elemento = quitar_signos_de_exclamacion(elemento, '.') #Eliminamos signos de exclamación
    elemento = quitar_emojis(elemento)
    frases.append(elemento) #Se agregan las frases ya traducidas para su posterior evaluación

# i = 0
# translater = Translator()
# for comentario in frases:
#     idioma = translater.detect(comentario)
#     if idioma != 'en' and i < 5:
#         frases.remove(comentario)
#         traduccion = translater.translate(comentario, dest='en')
#         frases.append(traduccion)
#         print(traduccion)
#         i = i + 1


positivo = 0
negativo = 0
neutral = 0
for sentence in frases:
    #print(sentence)
    scores = analizador.polarity_scores(sentence)
    for key in scores:
        print(key, ': ', scores[key])

print(scores)


print(positivo, negativo, neutral)

valores = [positivo, negativo, neutral]
categorias = ['Positivo', 'Negativo', 'Neutral']

plt.bar(categorias, valores)

plt.title("Clasificación de comentarios")
plt.xlabel("Clasificación")
plt.ylabel("Número de posts")

plt.show()

fin = time.time()
tiempo_final = fin - inicio
print(f"El tiempo fue de: {tiempo_final} segundos")
