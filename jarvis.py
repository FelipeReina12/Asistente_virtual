"""
Se necesita descargar varias liberias:
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
pip install pywhatkit
pip install wikipedia
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = "jarvis"  #Le damos un nombre a nuestro asistente
key = "AIzaSyAuJL8Uc69nwB-NP498-hBakf1vOhAjmVw"

listener = sr.Recognizer()  #Reconocer la voz
engine = pyttsx3.init()  #Es para escuchar la voz

voices = engine.getProperty('voices')  #Obtener todas las voces
engine.setProperty("voice", voices[0].id)  #Establecer la voz por defecto

def talk(text):
    engine.say(text)  #Aqui lo que hacemos es pasarle un mensaje a la voz
    engine.runAndWait()  #Aqui lo que hacemos es esperar a que termine de hablar

def listen():
    try:  #El try es para evitar errores
        with sr.Microphone() as source:  #Abrir el micrófono
            print("Escuchando...")
            voice = listener.listen(source)  #Aqui lo que hacemos es escuchar
            rec = listener.recognize_google(voice, language="es-ES")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, " ")
                print(rec)

    except Exception as e:
        print(f"Error: {e}")
    return rec
def run():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce", "")
        talk(f"Reproduciendo: {music}")
        pywhatkit.playonyt(music)
    # if "Cuntos suscriptores tiene" in rec:
    #     name_subs = rec.replace("cuantos suscriptores tiene", " ")
    #     data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name_subs.strip() + "&key=" + key).read()
    #     subs = json.loads(data).get("items")[0].get("statistics").get("subscriberCount")
    #     talk(name_subs + "Tiene {:d}".format(int(subs)) + " suscriptores")
    if "hora" in rec:
        hora = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"Hora actual: {hora}")
    elif "busca" in rec:
        order = rec.replace("busca", "")
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk("Vuelve a intentarlo")
while True:
    run()








