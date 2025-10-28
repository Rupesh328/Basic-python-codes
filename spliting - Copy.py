# Example input
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone for input
with sr.Microphone() as source:
    print("Please say something...")
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)

        input_statement = text(" ")

        # List of common stopwords (you can extend this)
        stopwords = ["the", "is", "in", "over", "a", "an", "of"]

        # Split the input statement into words
        words = input_statement.lower().split()

        # Filter out stopwords
        keywords = [word for word in words if word in stopwords]

        print("Keywords:", keywords)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if text = stopwords:
    print("Stop words")
else :
    print("it don't work")