from voice.wake_word import wake_up
from voice.listen import listen
from voice.speak import speak
from core.brain import process_command
from vision.emotion import detect_emotion

print("JARVIS X INITIALIZED")

while True:
    if wake_up():
        emotion = detect_emotion()
        speak("Hello, how can I help you?", emotion)

        command = listen()
        if "exit" in command or "stop" in command:
            speak("Shutting down. Goodbye.")
            break

        response = process_command(command)

        if "write" in command:
            print("JARVIS:", response)
        else:
            speak(response, emotion)
