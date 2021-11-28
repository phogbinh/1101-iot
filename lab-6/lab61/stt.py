from importlib import reload
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source, duration=1)
  print("Say something: ")
  audio = r.listen(source)

try:
  print("Google Speech Recognition thinks you said: ")
  sent = r.recognize_google(audio, language="zh-TW")
  print("{}".format(sent))
except sr.UnknownValueError:
  print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
  print("No response from Google Speech Recognition serve: {0}".format(e))
