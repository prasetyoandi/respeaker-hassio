import speech_recognition as sr
import config
from subprocess import call
from intent_recognition import getIntent
import hass
import time
import snowboy.snowboydecoder as snowboydecoder

def detected_callback():
    r = sr.Recognizer()
    mic = sr.Microphone()
    voice = ''
    with mic as source :
        call(['aplay', '-q', 'snowboy/resources/ding.wav'])
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try :
            voice = r.recognize_google(audio, language='id-ID')
        except : {}
        voice = voice.lower()
    print('command : ' + voice)
    intent = getIntent(voice)
    call(['aplay', '-q', 'snowboy/resources/dong.wav'])
    if intent is not None :
        print('intent  : ' + intent)
        res = hass.call(intent)
        print('hassio  : ' + res)

detector = snowboydecoder.HotwordDetector("nilaya.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)

print('ready')