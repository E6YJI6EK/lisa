import speech_recognition as sr
from config import recog, engine

# input/output
def listening():
    microphone = sr.Microphone(device_index=1)
    with microphone as source:
        return recog.recognize_google(recog.listen(source), language='ru-Ru')


def reading():
    cmd = input()
    return cmd


def say_phrase(phrase):
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()
    return phrase