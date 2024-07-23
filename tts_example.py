import pyttsx3

def say_message(message):
    # Initialize TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 125)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    
    # Say the message
    engine.say(message)
    
    # Wait for the speech to finish
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    message = "Hello! This is an example message."
    say_message(message)

