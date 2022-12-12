import speech_recognition as sr 
from googletrans import Translator


r = sr.Recognizer()
translator = Translator()


filename = 'D:/JMM/11 twilio for call/RE8dc7f6318b81596e65a53f8fb890ba86.wav'
with sr.AudioFile(filename) as source:
    print('Recording Start.....')
    audio_data = r.record(source)
    print("Recognizing...")
    # convert speech to text
    # text = r.recognize_google(audio_data,language='ur-in')
    text = r.recognize_google(audio_data)
    
    print('Speech To Text : ',text)
    
    # translation = translator.translate(text)
    # print ('Translated To English : ',translation)