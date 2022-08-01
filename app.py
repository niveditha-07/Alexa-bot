import pandas as pd
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import pyttsx3

r=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
df=pd.read_csv('boto.csv')
x=df.iloc[:,:-4].values
y=df.iloc[:,1:].values
text1="hii am alexa  can you tell me your roll number"

with sr.Microphone() as source2:
    engine.say(text1)
    engine.runAndWait()
    r.adjust_for_ambient_noise(source2,duration=0.2)
    audio2=r.listen(source2)
    try:
        no=r.recognize_google(audio2,language='en-US')
        #print('your message {}'.format(mytext))
        #st.write(mytext)
    except Exception as es:
        print("err")
print(no)
num=int(no)
print("the roll no is: ",num)
for i in range(4):
    if df.roll[i]==num:
        academic=(y[i][0]+y[i][1])//2
        attendence=(y[i][2]+y[i][3])//2
        engine.say("the academic percentage is")
        engine.say(academic)
        print("the academic percentage is",academic)
        engine.say("the attendence percentage is")
        engine.say(attendence)
        print("the attendence percentage is",attendence)
        engine.runAndWait()