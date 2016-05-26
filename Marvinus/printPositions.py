# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:39:26 2016

@author: Gast1
"""

timerSeconds = 15
arm = 'LArm'
hand = 'LHand'

import effector
import datetime
from naoqi import ALProxy
IP = "10.0.1.10"
PORT = 9559

try:
    motionProxy = ALProxy("ALMotion", IP, PORT)
    print('motionProxy initialized!')
except Exception, e:
    print "Could not create proxy to ALMotion"
    print "Error was: ", e

e = effector.Effector(arm, 'LWristYaw', motionProxy)

print('STIFFness is OF')

e.proxy.setStiffnesses("Body",1)
motionProxy.closeHand(hand)
#motionProxy.stiffnessInterpolation(hand,1,0.01)

#timer = datetime.datetime.now()
#endtimer = timer + datetime.timedelta(seconds = timerSeconds)

#while datetime.datetime.now() < endtimer:
#    print(e.getAbsolutePosition())

print('STIFFness is ON')

e.proxy.stiffnessInterpolation(arm,0,1)

#motionProxy.closeHand(hand)
#motionProxy.stiffnessInterpolation(hand,1,0.01)
# motionProxy.getAngles("LWristYaw", True)