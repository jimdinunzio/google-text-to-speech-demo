#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import texttospeech as tts
import time
import subprocess
from threading import Thread, Lock
import conversation as converse

lock = Lock()

class VoiceHatThread(Thread):
    def run(self):
        recognizer = aiy.cloudspeech.get_recognizer()
        recognizer.expect_hotword('robot');
        recognizer.expect_phrase('turn off the light')
        recognizer.expect_phrase('turn on the light')
        recognizer.expect_phrase('pulse the light')
        recognizer.expect_phrase('what time is it')
        recognizer.expect_phrase('repeat after me')
        recognizer.expect_phrase('goodbye')
        recognizer.expect_phrase("What's Australian for beer?")

        button = aiy.voicehat.get_button()
        led = aiy.voicehat.get_led()
        aiy.audio.get_recorder().start()

        while True:
            print('Listening...')
            text = recognizer.recognize()
            if not text:
                print('Sorry, I did not hear you.')
            else:
                lock.acquire()
                print('You said "', text, '"')
                #aiy.audio.say('I heard ' + text)
                #tts.say_text('I heard ' + text)
                if 'turn on the light' in text:
                    led.set_state(aiy.voicehat.LED.ON)
                elif 'turn off the light' in text:
                    led.set_state(aiy.voicehat.LED.OFF)
                elif 'pulse the light' in text:
                    led.set_state(aiy.voicehat.LED.BLINK)
                elif 'repeat after me' in text:
                    to_repeat = text.replace('repeat after me', '', 1)
                    #aiy.audio.say(to_repeat)	
                    tts.say_text(to_repeat)
                elif 'what time is it' in text:
                    tts.say_text('It\'s ' + time.strftime('%l:%M %p.'))
                elif 'goodbye' in text:
                    tts.say_text('good bye')
                elif "what's australian for beer" in text:
                    tts.say_text('Fosters, of course')
                
                lock.release()

class ConversationThread(Thread):
    def run(self):
        converse.start(lock)


if __name__ == '__main__':
    VoiceHatThread().start()
    ConversationThread().start()

