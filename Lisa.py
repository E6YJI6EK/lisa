import speech_recognition as sr
import pyttsx3
from config import opts, cmds, phrases
from commands import skills


class ZaebalException(Exception):
    def __init__(self, response):
        super().__init__()
        self.response = response


# heart
engine = pyttsx3.init()
recog = sr.Recognizer()
microphone = sr.Microphone(device_index=1)

# ears
def listening():
    microphone = sr.Microphone(device_index=1)
    with microphone as source:
        return recog.recognize_google(recog.listen(source), language='ru-Ru').lower()

# eyes
def reading():
    cmd = input()
    return cmd

# cock_sucker
def say_phrase(phrase):
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()
    return phrase

# brains
def censore(phrase):
    if "*" in phrase:
        return True
    return False


def define_cmd(word, prev_word, cmds):
    return word in cmds or f"{prev_word} {word}" in cmds


def execute_cmd(cmd):
    response = ''

    for word in cmd.split():    
        if word in opts['appeals']:
            cmd = cmd.split()
            prev_word = ''

            for word in cmd:
                if censore(word):
                    say_phrase(phrases['bad_lexicon'])
                    say_phrase(skills["goodbye"]())
                    raise ZaebalException(phrases['bad_lexicon'])
                if define_cmd(word, prev_word, cmds['hello']):
                    response = skills["hello"]()
                if define_cmd(word, prev_word, cmds['joke']):
                    response = skills["joke"]()
                if define_cmd(word, prev_word, cmds['ctime']):
                    response = skills["ctime"]()
                if define_cmd(word, prev_word, cmds['news']):
                    response = skills["news"]()
                if define_cmd(word, prev_word, cmds['love_me']):
                    response = skills["no"]()
                if define_cmd(word, prev_word, cmds['shut_up']):
                    raise ZaebalException(say_phrase(skills["goodbye"]()))

                prev_word = word

            say_phrase(response)

    return response
        

