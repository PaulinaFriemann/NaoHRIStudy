# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:43:13 2016

@author: Gast1
"""

import positions
#from effector import Effector
from speechrecognition import SpeechRecognition

from naoqi import ALProxy


def main(IP = "10.0.1.7", PORT = 9559):
    print('main called')    
    
    try:
        speechRecProxy = ALProxy("ALSpeechRecognition", IP, PORT)
        memoryProxy = ALProxy("ALMemory", IP, PORT)
        tracker = ALProxy("ALTracker", IP, PORT)
        print('motionProxy initialized!')
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
        
    # initialize motion proxy
    #postureProxy = ALProxy("ALRobotPosture", IP, PORT)

    
    # initialize speech recognition proxy
    asr = SpeechRecognition(IP, PORT)
    asr.start_recognition()
        
    #postureProxy.goToPosture("Sit", 0.5)

    # initialize effector
    #leftArmEffector = Effector('LArm','LWristYaw', IP, PORT)
    
    testPos = [0.10129939019680023, 0.22932101786136627, 0.23544558882713318] 
    testRot = []
    
    #leftArmEffector.move_to_absolute_position(testPos, testRot)
    
  #  arm, pos, hand, rot = positions.get_position('C')
    #leftArmEffector.move_to_absolute_position(pos, rot)
    
 #   arm, pos, hand, rot = positions.get_position('D')
    #leftArmEffector.move_to_absolute_position(pos, rot)
    

if __name__ == "__main__":
    main()