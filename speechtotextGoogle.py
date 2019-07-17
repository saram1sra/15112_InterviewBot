#citation : 
#https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
#https://pypi.python.org/pypi/SpeechRecognition/
import speech_recognition as MySp
import pyaudio

 

def speechtotext(time) :
    inputspeech = MySp.Recognizer()
    inputspeech.energy_threshold = 300
    with MySp.Microphone() as source:
            print("Please Start Speaking")
            audio1 = inputspeech.listen(source)
    print("Recording over")
    google_audio1 = inputspeech.recognize_google(audio1)
    print(google_audio1)
    return(google_audio1)

#speechtotext(3)
###Test
########################################3
'''inputspeech = MySp.Recognizer()
inputspeech.energy_threshold = 4000
inputspeech.operation_timeout = 240

with MySp.Microphone() as source:
#    print("Please Start Speaking in microphone")
#   audio1 = inputspeech.listen(source, timeout=120)
#  print("Second Statement")
# audio2 = inputspeech.listen(source, timeout=120)


    MyRecord = MySp.Recognizer()
    print("Please start speaking \n ")
    audio1 = inputspeech.listen(source, timeout = 120)
    print(1)
    user1 = inputspeech.recognize_google(audio1, language="en-US", show_all=False)
    print("Speaker input 1 \n \n" + user1)
   # audio2 = MyRecord.listen(source)
    #user2 = MyRecord.recognize_google(audio2, language="en-US", show_all=False)
    #print("\n Speaker input 2 \n \n" + user2)
    #print("\n The concatenated value is \n \n" + user1 + user2)





print("Recording Over")
print("Converting audio to text using google audio to text - Started")
google_audio1 = inputspeech.recognize_google(audio1, language="en-US", show_all=False)
#google_audio2 = inputspeech.recognize_google(audio2, language="en-US", show_all=False)
#print("Converting audio to text using google audio to text - Over")
print("1st Statement, I captured - ", google_audio1)
#print("2nd Statement, I captured - ", google_audio2)'''