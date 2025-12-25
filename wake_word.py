import speech_recognition as sr

def wake_up():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for wake word...")
        audio = r.listen(source)
    try:
        return "hey jarvis" in r.recognize_google(audio).lower()
    except:
        return False
