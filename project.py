import os
import webbrowser
import subprocess
from twython import Twython
import pyttsx3
import wikipedia
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from geopy.geocoders import Nominatim

def open_notepad():
    subprocess.run(['notepad.exe'])

def open_chrome():
    webbrowser.open("http://www.google.com")

def open_whatsapp():
    # 
    pass

def send_email():
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    recipient_email = 'recipient_email@example.com'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Subject of the email'

    body = 'Hello, this is the body of the email!'
    message.attach(MIMEText(body, 'plain'))


    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Email sent successfully!")
    pass

def send_sms():
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'
    recipient_phone_number = 'recipient_phone_number'


    client = Client(account_sid, auth_token)

    message_body = 'Hello, this is a test SMS from your Python script!'

    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"SMS SID: {message.sid}")
    pass

def chat_with_gpt():
    user_input = input("Enter your message: ")
    # Implement code to interact with GPT-3 or any other chatbot
    pass

def get_geolocation(address):
    geolocator = Nominatim(user_agent="geolocation_example")
    location = geolocator.geocode(address)

    if location:
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude
    else:
        return None

    # Example usage:
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    coordinates = get_geolocation(address)

    if coordinates:
        print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
    else:
        print("Geolocation not found for the given address.")
    pass

def get_twitter_trends():
    # 
    pass

def get_hashtag_posts():
    hashtag = input("Enter the hashtag: ")
    query = f"site:instagram.com/p/ #{hashtag}"
    results = search(query, num=10, stop=10, pause=2)  # Get up to 10 search results
    for result in results:
        print(result)
    get_hashtag_posts(hashtag)
    pass

def get_wikipedia_data():
    # Ask the user for the topic of the Wikipedia page
    topic = input("Enter the topic of the Wikipedia page: ")

    wiki_url = f"https://en.wikipedia.org/wiki/{topic}"

    response = requests.get(wiki_url)

    soup = BeautifulSoup(response.content, "html.parser")

    paragraphs = soup.find("div", {"class": "mw-parser-output"}).find_all("p")

    for paragraph in paragraphs:
        print(paragraph.text)


def play_audio():
    import pyttsx3
    speaker = pyttsx3.init()
    speaker.say("Hello Goverdhan")
    speaker.runAndWait()
    pass

def play_video():
    # 
    pass

def control_speaker_volume():
    text_to_speak = input("Enter the text to speak: ")
    engine = pyttsx3.init()
    engine.say(text_to_speak)
    engine.runAndWait()

while True:
    print("\n===== Menu =====")
    print("1. Notepad")
    print("2. Chrome")
    print("3. WhatsApp")
    print("4. Email")
    print("5. SMS")
    print("6. Chat with GPT")
    print("7. Geolocation")
    print("8. Twitter Trends")
    print("9. Hashtag Posts")
    print("10. Wikipedia Data")
    print("11. Audio Player")
    print("12. Video Player")
    print("13. Speaker Volume Control")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        open_notepad()
    elif choice == '2':
        open_chrome()
    elif choice == '3':
        open_whatsapp()
    elif choice == '4':
        send_email()
    elif choice == '5':
        send_sms()
    elif choice == '6':
        chat_with_gpt()
    elif choice == '7':
        get_geolocation()
    elif choice == '8':
        get_twitter_trends()
    elif choice == '9':
        get_hashtag_posts()
    elif choice == '10':
        get_wikipedia_data()
    elif choice == '11':
        play_audio()
    elif choice == '12':
        play_video()
    elif choice == '13':
        control_speaker_volume()
    elif choice == '0':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
