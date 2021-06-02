import speech_recognition as sr
recognizer = sr.Recognizer()
mic = sr.Microphone()
while 1 :
    with mic as source :
        recognizer.adjust_for_ambient_noise(source)
        print('siap')
        audio = recognizer.listen(source)
        response = recognizer.recognize_google(audio, language='id-ID')
        print(response)