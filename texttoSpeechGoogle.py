#citation : learnt modules from : 
#http://pythonhosted.org/pyglet/programming_guide/simple_audio_playback.html

import pyaudio
from gtts import gTTS
import pyglet

def texttospeech(text,savename):
    #msg = open("C:/Users/saram/Dropbox/Classes/Sem1/15112/TermProject/Test code/testingFile.txt","r+")
    #MyText =msg.read()
    MySpeech = gTTS(text=text, lang = "en")
    #MySpeech = gTTS(text=MyText, lang = "en")
    #MySpeech.save("textSpeech.mp3")
    MySpeech.save('C:/Users/saram/Dropbox/Classes/Sem1/15112/TermProject/Test code/'+savename)
    music = pyglet.media.load('C:/Users/saram/Dropbox/Classes/Sem1/15112/TermProject/Test code/'+savename, streaming=False)
    music.play()


####
###Testfile :#texttospeech("hell", "testinterview")
####        

    
