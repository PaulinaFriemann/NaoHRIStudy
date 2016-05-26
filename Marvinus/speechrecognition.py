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
        
    def stop_recognition(self):
        self.speechRecProxy.unsubscribe("ASR")