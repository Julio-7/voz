#parte 1 - importar bibliotecas
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

#parte 2 -configuracao geral
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def cuprimento ():
    hora = int(datetime.datetime.now().hour)
    if hora>5 and hora<12:
        speak("Bom dia")
    elif hora>=12 and hora<18:
        speak("Boa tarde")
    else:
        speak("Boa noite")
    
    speak("Eu me chamo jarvis, como posso lhe ajudar?")

cuprimento()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-in')
        print(f"voce disse: {query}\n")

    except Exception as e:
        print("Repita novamente, por favor...")
        return "None"

    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
    
        if 'abrir google' in query:
            #webbrowser.open("google.com") 
            url = "google.com"
            webbrowser.register('opera',
            None,
            webbrowser.BackgroundBrowser("C://Users\julio\AppData\Local\Programs\Opera GX\launcher.exe"))
            webbrowser.get('opera').open_new(url)

        elif 'fechar o programa' in query:
            speak("Ok! Finalizando o programa...")
            break
        
        elif 'horas por favor' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Senhor, a hora e {strTime}")

        elif 'abrir documento' in query:
            diretorio_documento = "C://Users\julio\OneDrive\Área de Trabalho"
            os.startfile(diretorio_documento)
        
        elif 'abrir mapa' in query:
            speak("Que local você deseja olhar no mapa?")
            query = takeCommand().lower()
            location = query
            speak("Aguarde um instante, estou abrindo o google maps com a localização de"+location)
            webbrowser.open("https://www.google.com.br/maps/place/"+location)