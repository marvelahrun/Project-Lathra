import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.id}")
engine.setProperty('voice', voices[1].id)  # Voice ID may need to be adjusted depending on OS
engine.setProperty('rate', 160)

def speak(text):
    print("Lathra:", text)
    engine.say(text)
    engine.runAndWait()