import speech_recognition as sr
import webbrowser
import pyttsx3
import tkinter as tk

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
        return ""

def search_on_amazon():
    engine.say("¿Qué quieres buscar en Amazon?")
    engine.runAndWait()
    text = talk()
    webbrowser.open(f"https://www.amazon.es/s?k={text}")

def open_github():
    webbrowser.open("https://github.com/EnmanuelReynoso23")

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_twitter():
    webbrowser.open("https://twitter.com/Enmanue15414610")

def open_instagram():
    webbrowser.open("https://www.instagram.com/enmanuel_reynoso2/")

def open_youtube():
    webbrowser.open("https://www.youtube.com/@Enmanueldev")

def create_interface():
    window = tk.Tk()
    window.title("Asistente de Compra en Amazon")
    window.geometry("400x200")

    button_amazon = tk.Button(window, text="Comprar", command=search_on_amazon, bg="blue", fg="white", font=("Arial", 14), width=15, height=2)
    button_amazon.pack(pady=20)

    button_github = tk.Button(window, text="GitHub", command=open_github, bg="black", fg="white", font=("Arial", 14), width=10, height=2)
    button_github.pack(side=tk.LEFT, padx=10)

    button_chrome = tk.Button(window, text="Chrome", command=open_chrome, bg="green", fg="white", font=("Arial", 14), width=10, height=2)
    button_chrome.pack(side=tk.LEFT, padx=10)

    button_twitter = tk.Button(window, text="Twitter", command=open_twitter, bg="blue", fg="white", font=("Arial", 14), width=10, height=2)
    button_twitter.pack(side=tk.LEFT, padx=10)

    button_instagram = tk.Button(window, text="Instagram", command=open_instagram, bg="purple", fg="white", font=("Arial", 14), width=10, height=2)
    button_instagram.pack(side=tk.LEFT, padx=10)

    button_youtube = tk.Button(window, text="YouTube", command=open_youtube, bg="red", fg="white", font=("Arial", 14), width=10, height=2)
    button_youtube.pack(side=tk.LEFT, padx=10)

    label = tk.Label(window, text="Creado por Enmanuel Reynoso", font=("Arial", 12))
    label.pack(side=tk.BOTTOM)

    window.mainloop()

if __name__ == "__main__":
    create_interface()
