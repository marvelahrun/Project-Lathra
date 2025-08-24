from wakeword_listener import listen_for_wakeword
from speech.recognizer import recognize_command
from speech.tts_engine import speak
import subprocess
import webbrowser
from modules import browser, media
from config.permissions import is_allowed


def handle_command(command):
    if "open browser" in command and is_allowed("browser"):
        browser.open_browser()
    elif "play music" in command and is_allowed("media"):
        webbrowser.open('https://music.youtube.com/')
    elif "say hi" in command and is_allowed("say hi"):
        speak("Hi, I'm Lathra. Your personal AI Assistant")
    elif "ping youtube" in command and is_allowed("youtubeping"):
        subprocess.run('ping youtube.com')
    elif "you may sleep" in command and is_allowed("sleep"):
        speak("See you again")
        exit()
    else:
        speak("Sorry, I can't do that or it is not permitted.")


if __name__ == "__main__":
    while True:
        print("[Listening for wake word...]")
        listen_for_wakeword()
        speak("Hello! how can I help you?")
        command = recognize_command()
        handle_command(command)