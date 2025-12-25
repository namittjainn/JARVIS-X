import pyttsx3

engine = pyttsx3.init()

def speak(text, emotion="neutral"):
    rate = 160
    if emotion == "happy":
        rate = 180
    elif emotion == "sad":
        rate = 140

    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
