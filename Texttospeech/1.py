from gtts import gTTS
import os
f=open('1.txt')
x=f.read()
langauge ='en'
audio=gTTS(text=x,lang=langauge,slow=True)
audio.save("1.wav")
os.system("1.wav")
