#!/usr/bin/env python3

import aiy.voicehat
import argparse
import texttospeech as tts
import subprocess
import time

class SpokenLine():
        def __init__(self, text, lang, voice, isSsml=False, expectResponse=False):
            self.text = text
            self.lang = lang 
            self.voice = voice 
            self.isSsml = isSsml
            self.expectResponse = expectResponse

lines = [
        SpokenLine("whatcha got there?", 'en-US', 'en-US-Wavenet-A'),
        SpokenLine("Sorry, Sprechen sie deutch?", 'de-DE', 'de-DE-Standard-A'),
        SpokenLine("Bonjour, monsieur. I speak a little German. Should I translate for you?", 'fr-FR', 'fr-CA-Standard-A'),
        SpokenLine("Yes, that would be great", 'en-US', 'en-US-Wavenet-A'),
        SpokenLine("ok. Pardon Fräulein, was hast du da?", 'fr-FR', 'fr-CA-Standard-A'),
        SpokenLine("Es ist der Aussie.", 'de-DE', 'de-DE-Standard-A'),
         SpokenLine("<speak>Crikey, mate! it’s just my talking box. Have a listen. <break time=\"1s\" /> Robot <break time=\"100ms\" /> what time is it? </speak>", 'en-AU', 'en-AU-Standard-B', True, True),
         SpokenLine("<speak>awwwww, cooool. Can I try? <break time=\"1s\" /> Robot <break time=\"500ms\" /> turn on the light.</speak>", 'en-US', 'en-US-Wavenet-A', True, True),
         SpokenLine("<speak>ooohhhh ahhhhh</speak>", 'de-DE', 'de-DE-Standard-A', True),
         SpokenLine("<speak>One more trick.<break time=\"1s\" /> You do the honors, mate. It responds best to an American accent.</speak>", 'en-AU', 'en-AU-Standard-B', True),
         SpokenLine("<speak>Robot <break time=\"500ms\" />What's Australian for beer?</speak>", 'en-US', 'en-US-Wavenet-A', True, True),
         SpokenLine("Incroyable!", 'fr-FR', 'fr-CA-Standard-A', False)
        ]

def start(lock):
    button = aiy.voicehat.get_button()
    tts.say_text("I'm ready to start.")
    button.wait_for_press()
#    subprocess.run(["sudo", "service", "my_assistant", "start"])
#    choice = randint(0,5)
    for line in lines:
        print(line.text + ' ' + line.lang + ' ' + line.voice)
        lock.acquire()
        if line.isSsml:
            tts.say_ssml(line.text, line.lang, line.voice)
        else:
            tts.say_text(line.text, line.lang, line.voice)
        lock.release()
        if line.expectResponse:
            time.sleep(4)
        else:
            time.sleep(1)
#    button.wait_for_press()
#    subprocess.run(["sudo", "service", "my_assistant", "stop"])

if __name__ == '__main__':
    start()
    
