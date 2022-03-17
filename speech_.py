
from queue import Queue
import pyttsx3
import speech_recognition as sr
import time
from colorama import init,Fore

init()
queue = Queue()
countries = ['Afghanistan','Pakistan','India']
correct = 0
incorrect = 0
for c in countries:
    queue.put(c)

# create recognizer instance
recognizer = sr.Recognizer()
# creating engine for text to speech
engine = pyttsx3.init()

# read the mic and store tha audio in a variable
while not queue.empty():
    word = queue.get()
    input("Press Enter To Continue")
    print("Listen To The Word Carefully")
    time.sleep(1)
    # give it text
    engine.say(word)
    engine.runAndWait()
    time.sleep(1)
    with sr.Microphone() as source:
        print("Now Repeat That Word")
        audio_text = recognizer.listen(source)
        print("Time Over, Thank You")
        try:
            # using google speech recognition (API)
            text = recognizer.recognize_google(audio_text)
            print(f"Text: {text}")
            if text in countries:
                print("{}Correct{}\n".format(Fore.GREEN,Fore.RESET))
                correct+=1
            else:
                incorrect+=1
                print("{}Incorrect{}\n".format(Fore.RED,Fore.RESET))
                continue
        except:
            print("Sorry I did not get it")
print(f'\nCorrect Answers >> {correct}')
print(f'\nIncorrect Answers >> {incorrect}')
