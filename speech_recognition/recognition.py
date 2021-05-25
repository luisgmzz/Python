import speech_recognition as sr
import time

PATH = "./audios/pues_entonces_no_me_jodas.wav"

r = sr.Recognizer()

with sr.AudioFile(PATH) as source:
    audio = r.listen(source)

    try:
        print("Reading audio file. Please, wait a moment...")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print(text)
    except:
        print("I am sorry! I can not understand!")