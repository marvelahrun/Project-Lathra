import speech_recognition as sr

def listen_for_wakeword():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                phrase = recognizer.recognize_google(audio).lower()
                if "hello" in phrase:
                    return
                elif "hello lathra" in phrase:
                    return
                elif "hello luhtra" in phrase:
                    return
                elif "lathra" in phrase:
                    return
                elif "luhtra" in phrase:
                    return
            except sr.UnknownValueError:
                continue