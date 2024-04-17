import os
import requests
from dotenv import load_dotenv
from fpdf import FPDF
from flask import Flask, render_template, request, send_file

#Carga las variables de entorno desde un archivo .env
load_dotenv()

#Configuración de la clave de API y el endpoint de la API de OpenAI para usar el modelo gpt-3.5-turbo
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Obtiene la clave de API de OpenAI desde las variables de entorno
OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions'  # URL para solicitar respuestas del modelo de chat "gpt-3.5-turbo"

#Configuración de encabezados:
headers = {
    'Content-Type': 'application/json',   #Indica que el cuerpo de la solicitud es un JSON
    'Authorization': f'Bearer {OPENAI_API_KEY}'  #Usa la clave de API para la autorización
}

prompt = "¿CUAL ES LA CAPITAL DE PERÚ?"

#Datos que se enviarán en la solicitud POST:
data = {
    'model': 'gpt-3.5-turbo', 
    'messages': [{'role': 'user', 'content': prompt}],  
    'max_tokens': 10,  
    'temperature': 0.7  
}


try:
    #Realizamos una solicitud POST a la API de OpenAI
    respuesta = requests.post(OPENAI_API_URL, headers=headers, json=data)
    #Verificamos si la solicitud fue exitosa (código HTTP 200)
    if respuesta.status_code == 200:
        #Extrae el contenido de la respuesta y lo muestra
        respuesta_texto = respuesta.json()['choices'][0]['message']['content'].strip()
        print(respuesta_texto)
    else:
        print(f"Error de la Api: {respuesta.status_code} - {respuesta.text}")
except Exception as e:
    print(f"Error haciendo la llamada a la Api: {e}")