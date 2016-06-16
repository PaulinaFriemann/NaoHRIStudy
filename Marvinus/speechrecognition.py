# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:19:36 2016

@author: Gast1
"""
from naoqi import ALProxy
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
        
    def react(self, word):
        if word == "zero" or word == "one" or word =="two" or word == "three" :
            self.speakProxy.say("Was it that bad?")
        elif word == "four" or word == "five" or word == "six" or word == "seven":
          self.speakProxy.say("I will try better next time")
        elif word == "eight" or word == "nine":
             self.speakProxy.say("You like that? Wait until you hear this one!")
        elif word == "ten":
             self.speakProxy.say("I am so glad you liked it, I worked on this for several months. I am actually thinking of performing next month in theatre, would you come visit me?")
        else:
            self.speakProxy.say("I do not understand you. Could you repeat what you just said?")
            
            
    def stop_recognition(self):
        self.speechRecProxy.unsubscribe("ASR")