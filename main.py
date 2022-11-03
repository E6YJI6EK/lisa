from speech_recognition import UnknownValueError 
from Lisa import execute_cmd, say_phrase, listening, reading, ZaebalException
from config import phrases
from helpers import log


def main():
    say_phrase(phrases["begin"])
    while True:
        try:
            request = listening()
            response = execute_cmd(request)
            log(request, response)
        except UnknownValueError as e:
            log(request, e)
            say_phrase(phrases["misunderstanding"])
        except ZaebalException as e:
            log(request, e.response)
            break
            
        


def test():
    say_phrase(phrases["begin"])
    query = reading()
    execute_cmd(query)
    say_phrase(phrases["end"])


if __name__ == "__main__":
    main()