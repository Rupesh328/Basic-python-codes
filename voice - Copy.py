import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set speech rate
engine.setProperty('rate', 120)

# Set volume level
engine.setProperty('volume', 1.0)

# Select voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Female voice

# Text to be spoken
text = "This is an example of text-to-speech control in Python."

# Speak the text
engine.say(text)

# Run the speech engine
engine.runAndWait()
