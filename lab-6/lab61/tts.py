import tempfile
from gtts import gTTS
from pygame import mixer
import time

def speak(sentence, lang, loops_count):
  with tempfile.NamedTemporaryFile(delete=True) as file:
    tts = gTTS(text=sentence, lang=lang)
    tts.save('{}.mp3'.format(file.name))
    mixer.init()
    mixer.music.load('{}.mp3'.format(file.name))
    mixer.music.play(loops_count)

try:
  sentence = 'Hello World'
  speak(sentence, 'en', 1)
  time.sleep(2)
except Exception as e:
  print(e)
