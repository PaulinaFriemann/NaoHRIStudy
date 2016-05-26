# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:43:13 2016

@author: Gast1
"""

import positions
import effector
import time
from speech_recognition import Speech_recognition

from naoqi import ALProxy

def main(IP = "10.0.1.4", PORT = 9559):
    
    

    print('main called')    
    
    try:
        motionProxy = ALProxy("ALMotion", IP, PORT)
        speechRecProxy = ALProxy("ALSpeechRecognition", IP, PORT)
        memoryProxy = ALProxy("ALMemory", IP, PORT)
        tracker = ALProxy("ALTracker", IP, PORT)
        print('motionProxy initialized!')
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
        
    # initialize motion proxy
    #postureProxy = ALProxy("ALRobotPosture", IP, PORT)
        
    motionProxy.setStiffnesses("Body", 0)
    
    #motionProxy.wakeUp()
    #motionProxy.closeHand('LHand')
    #motionProxy.stiffnessInterpolation('LHand',1,0.01)
    
    # initialize speech recognition proxy
    asr = Speech_recognition(IP, PORT)
    asr.start_recognition()
    
        
    #postureProxy.goToPosture("Sit", 0.5)
    
    #leftArmEffector = effector.Effector('LArm','LWristYaw',motionProxy)
    
    testPos = [0.10129939019680023, 0.22932101786136627, 0.23544558882713318] 
    testRot = []
    
    #leftArmEffector.moveToAbsolutePosition(testPos, testRot)
    
    arm, pos, hand, rot = positions.getPosition('C')
    #leftArmEffector.moveToAbsolutePosition(pos, rot)
    
    arm, pos, hand, rot = positions.getPosition('D')
    #leftArmEffector.moveToAbsolutePosition(pos, rot)
    

if __name__ == "__main__":
    main()