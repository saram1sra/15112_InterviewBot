Project Details :
Interview Bot to replace human interviewers in job interviews to save capital and resources, as well as accurate and more realistic practice 
for people preparing for interviews. 
NOTE : To run interview Bot, run the python file, UI.py
No. of Jobs supported :761 jobs

Must have installed:
Python 2.7.x
Any editor(Pyzo,Sublime Text3, etc) 

APIs used :
IBM Watson Personality Insights
Google's Text to Speech and Speech to Text

Python Modules used(pip install) :
Tkinter, Pyglet, PyAudio, SpeechRecognition, json, requests, urllib, urllib2, HTMLParser, gTTS

Note : The program takes time to load as the code loads the 761 jobs in admin before running to reduce lag of actual program.
(Similarly it takes time for the best match to appear as it collects data)
If file shows HTTP error (404/502 mostly) re-run the file as this occurs if the website is unable to handle all the requests 
sent by the program, similarly when we come to the result page and we want to see the best match this error IOError: [Errno 2]
might come up due to the same reason.

Also we need to choose the job for which we are interviewing before in Admin to set comparison data.




