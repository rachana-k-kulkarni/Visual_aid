import RPi.GPIO as GPIO
import time
from twilio.rest import Client
import signal
import sys

# Setup for GPIO
button_pin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Twilio setup
sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_number = '+xxxxxxxxxxxxxxxxxx'
emergency_contact = '+91xxxxxxxxxx'

client = Client(sid, authToken)

# Signal handler for graceful exit
def signal_handler(sig, frame):
    print('Exiting gracefully')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

print("Press the button...")

try:
    while True:
        if GPIO.input(button_pin) == GPIO.LOW:
            print("Button pressed")
            try:
                message = client.messages.create(
                    to=emergency_contact,
                    from_=twilio_number,
                    body="SOS worked!!"
                )
                print("Message sent")
            except Exception as e:
                print(f"Failed to send message: {e}")
            
            # Debounce
            time.sleep(0.5)
        else:
            print("Button not pressed")
        
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

