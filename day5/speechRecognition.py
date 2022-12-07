import speech_recognition as sr

# Create a speech recognition object
r = sr.Recognizer()

# Set the language of the speech recognition
r.language = "it-IT"

# Start recording from the microphone
with sr.Microphone() as source:
  print("Dì qualcosa...")
  audio = r.listen(source)

# Recognize the voice in the audio
try:
  print("Hai detto: " + r.recognize_google(audio, language="it-IT"))
except sr.UnknownValueError:
  print("Spiacente, non ho capito quello che hai detto.")
except sr.RequestError as e:
  print("Errore durante la richiesta: " + str(e))
