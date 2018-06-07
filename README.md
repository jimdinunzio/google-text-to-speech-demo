# google-text-to-speech-demo
This code makes up a demonstration of google's text-to-speech cloud service and google's cloud speech recognition service and runs on on the AIY Voice Hat google device with a button, speaker, and microphone with its AIY modules installed.  The voice hat talks to itself and gets a response just as you would speaking to it yourself.

It runs two threads, one using TTS to play a conversation and another thread running cloud speech to listen for speech commands from the TTS output.  The cloud speech listener answers to the hot word "robot." When dialog from the converstaion says a command starting with "robot," the listener picks it up and makes a response.  A single lock is used to prevent both from speaking at the same time.  

It really needs a signal/wait construct so the conversation thread would sleep until the assistant thread signals it that it is done speaking, but apparently python signals cannot be used to communicate between threads.

synthesize_text.py is verbatim google code.  my_assistant.py is code I modified from google's AIY voice-hat code and I wrote files texttospeech.py and conversation.py.

Have fun!
jim@dinunzio.com