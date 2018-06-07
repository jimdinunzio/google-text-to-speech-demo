#!/usr/bin/env python3

import argparse
import synthesize_text as st
import os

def say_text(text, lang='en-US', name='en-US-Standard-C'):
    #print(text + ' ' + lang + ' ' + name)
    st.synthesize_text(text, lang, name)
    os.system("mpg123-pulse -q output.mp3")

def say_ssml(ssml, lang='en-US', name='en-US-Standard-C'):
    st.synthesize_ssml(ssml, lang, name)
    os.system("mpg123-pulse -q output.mp3")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('text', type=str,
            help='The text play as synthesized speech.')
    parser.add_argument('-lang', type=str, default='en-US',
            help='The language to speak.')
    parser.add_argument('-name', type=str, default='en-US-Standard-C',
            help='The voice name.')

    args = parser.parse_args()

    say_text(args.text, args.lang, args.name)
