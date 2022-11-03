from datetime import datetime
import speech_recognition as sr

# check microphones list
def print_devices():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        string = f"device_index = {index} - {name}"
        print(string.encode('cp1251').decode('utf-8'))


def log(input_value, output_value):
    now = datetime.now()
    print(f"[LOG][{str(now.hour)}:{str(now.minute)}][request]: {input_value}")
    now = datetime.now()
    print(f"[LOG][{str(now.hour)}:{str(now.minute)}][response]: {output_value}")