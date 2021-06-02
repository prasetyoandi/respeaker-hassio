import speech_recognition as sr
import time
from subprocess import call

def listen(recognizer, microphone):
    response = ''
    while response == '' :
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
            call(['aplay', '-q', 'snowboy/resources/ding.wav'])
            audio = recognizer.listen(source)
        try :
            response = recognizer.recognize_google(audio, language='id-ID')
        except : 
            print('gaga;')
    return response.lower()