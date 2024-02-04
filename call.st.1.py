import time
import pyttsx3
import requests

def get_warning_message_from_server():
    
    try:
        response = requests.get("http:/localhost:5050/get_warning_message")
        if response.status_code == 200:
            return response.json().get("warning_message")
        else:
            print("Failed to fetch warning message from server.")
    except Exception as e:
        print("Error occurred while fetching warning message:", e)
    return None

def play_warning_message(message):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(message)
    engine.runAndWait()

def main():
    while True:
        # Get warning message from server
        warning_message = get_warning_message_from_server()
        if warning_message:
            print("Received warning message:", warning_message)
            play_warning_message(warning_message)
        
        # Delay for 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    main()
