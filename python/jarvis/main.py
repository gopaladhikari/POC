import speech_recognition as sr
import webbrowser
import pyttsx3
import requests


from playlist import musicPlaylist as music


url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="


recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processText(text: str):
    if "open google" in text:
        print("-> Action: Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in text:
        print("-> Action: Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in text:
        print("-> Action: Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif text.startswith("play"):
        print("-> Action: Playing music")
        songName = text.split(" ")[1]
        songUrl = music[songName]
        webbrowser.open(songUrl)

    elif "news" in text:
        print("-> Action: Fetching news")
        response = requests.get(url)
        data = response.json()
        print(data)
        articles = data.get("articles", [])

        for article in articles:
            speak(article.get("title"))

    else:
        print(f"-> No action defined for command: '{text}'")


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        try:
            text: str = ""
            with sr.Microphone() as source:
                print("\n[ Listening for wake word... ]")
                # Calibrate to background noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                word = recognizer.listen(source)

                print("[ Recognizing wake word... ]")
                text = recognizer.recognize_google(word).lower()
            print(f"You said: '{text}'")

            if "jarvis" in text:
                speak("Ya")
                print("Ya")

                with sr.Microphone() as source:
                    print("\n[ Listening for command... ]")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                    print("[ Recognizing command... ]")
                    command = recognizer.recognize_google(audio).lower()

                print(f"Command recognized: '{command}'")
                processText(command)

        except Exception as e:
            print(f"Error: {e}")
