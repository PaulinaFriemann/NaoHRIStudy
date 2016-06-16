# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:19:36 2016

@author: Gast1
"""
from naoqi import ALProxy
from random import randint
import time


class SpeechRecognition:
    
    def __init__(self, IP, PORT):
        try:
            self.speechRecProxy = ALProxy("ALSpeechRecognition", IP, PORT)
            self.memoryProxy = ALProxy("ALMemory", IP, PORT)
            self.speakProxy = ALProxy("ALTextToSpeech", IP, PORT)
            print('Speech Recognition initialized')
        except Exception, e:
            print "Could not create proxy to ALSpeechRecognition"
            print "Error was: ", e
            
        try:
            self.speechRecProxy.unsubscribe("ASR")
        except:
            pass
           
        self.speechRecProxy.setLanguage("English")
        self.vocabulary = ["zero", "one", "two", "three", "four", "five", "six", "seven", 
                      "eight", "nine", "ten", "yes", "no"]
        self.speechRecProxy.setVocabulary(self.vocabulary, True)
        
        self.eventName = "ALSpeechRecognition/WordRecognized"
        self.wordSpotted = "ALSpeechRecognition/SpeechDetected"
         
    def start_recognition(self):
        self.speechRecProxy.subscribe("ASR")
        try:
            while True:
                time.sleep(0.5)
                recognized_word = self.memoryProxy.getData("WordRecognized")
                recognized_word = recognized_word[0].replace("<...>", "")
                print recognized_word
                
        except KeyboardInterrupt:
            self.speechRecProxy.unsubscribe("ASR")
            print "Interrupted by user"
            print "Stopping..."
        
    def react(self, word, condition):
        lottery = randint(1,3)      
if condition == 'neutral':    
    
            if word == "zero":        
                self.speakProxy.say("You are making a joke, right? Please tell me that was a joke.")
                self.speakProxy.say("Are you trying to make me sad? ")
                self.speakProxy.say("Well, you try to play a xylophone without proper hands.")
            elif word == "one" or word =="two" or word == "three" :
                if lottery = 1:
                    self.speakProxy.say("Was it that bad?")
                elif lottery = 2:
                    self.speakProxy.say("Maybe I should stop playing.")
                elif lottery = 3:
                    self.speakProxy.say("I am sorry I wasted your time.")
            elif word == "four" or word == "five":
                if lottery = 1:
                    self.speakProxy.say("I will try better next time")
                elif lottery = 2:
                    self.speakProxy.say("Something must have gone wrong")
                elif lottery = 3:
                    self.speakProxy.say("Sorry, I am still learning.")            
            elif word == "six":
                if lottery = 1:
                self.speakProxy.say("The piece is difficult, but I am glad I am pulled it off.")
                elif lottery = 2:
                self.speakProxy.say("You gave me a six!")
                elif lottery = 3:    
                self.speakProxy.say("Thanks! I am getting better!")
            elif word == "seven":
                if lottery = 1:
                    self.speakProxy.say("I am glad you sort of liked it!")
                elif lottery = 2:
                    self.speakProxy.say("I will be a professional one day!")
                elif lottery = 3:
                    self.speakProxy.say("You gave me a seven!")
                
            elif word == "eight" or word == "nine":
                if lottery = 1:
                 self.speakProxy.say("You like that? Wait until you hear this one!")
                elif lottery = 2:
                 self.speakProxy.say("This is my favourite piece as well!")
                elif lottery = 3:
                 self.speakProxy.say("I am so happy my efforts payed off and that you liked it!")
            elif word == "ten":
                if lottery = 1:
                 self.speakProxy.say("I am so glad you liked it, I worked on this for several months. I am actually thinking of performing next month in theatre, would you come visit me?")
                elif lottery = 2:
                 self.speakProxy.say("You are too kind!")
                elif lottery = 3:
                 self.speakProxy.say("Was it that good? Maybe I will start composing my own songs!")
            else:
                self.speakProxy.say("I do not understand you. Could you repeat what you just said?")
                self.speakProxy.say("I am sorry, I did not hear what you just said.")
                self.speakProxy.say("Would you mind to repeat what you just said?")
        else:
                if lottery = 1:
                 self.speakProxy.say("Would you like to hear another song?")
                elif lottery = 2:
                 self.speakProxy.say("Thank you for your support.")
                elif lottery = 3:
                 self.speakProxy.say("Thank you for rating me.")
            
    def stop_recognition(self):
        self.speechRecProxy.unsubscribe("ASR")