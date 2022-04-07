"""
smtplib: Simple Mail Transfer Protocol
server: gmail.com
tls: Transport Layer Security{To ensure,I'm secure}
pyttsx3: Text to speech

#Listening from the source
voice=listener.listen(source)
#using google api to convert voice to text
info=listener.rocognize_google(voice)

pyttsx3: To speak out/text to speech.
speechRecognition: Robot to listen to our voice/speech.
pywhatkit: Advance control on browser
wikipedia: To get Wikipedia data
pyjokes: To get funny jokes
"""

import smtplib
import speech_recognition as sr
import pyttsx3
#To get the email structure
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            listener.adjust_for_ambient_noise(source, duration=2)

            voice=listener.listen(source)
            #Google to recognize the voice
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print('Not clear')
        pass


def send_email(receiver,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('18csa49@karpagamtech.ac.in','Password')
    email=EmailMessage()
    email['From']='18csa49@karpagamtech.ac.in'
    email['To']=receiver
    email['Subject']=subject
    email.set_content(message)
    server.send_message(email)

email_list={'one':'username1@gmail.com','two':'username2@gmail.com'}

def get_email_info():
    talk('To Whom you want to send email')
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver,subject,message)
    talk('Hey. Your email have sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()

