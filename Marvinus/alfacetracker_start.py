# -*- encoding: UTF-8 -*-

"""
This example shows how to use ALTracker with face.
"""

import time
import argparse
from naoqi import ALProxy

class FaceTracker:
    def __init__(self, IP, PORT):
        
        try:
            self.motion = ALProxy("ALMotion", IP, PORT)
            self.faceProxy = ALProxy("ALTracker", IP, PORT)
            self.faceDetection = ALProxy("ALFaceDetection", IP, PORT)
        except Exception, e:
            print "could not create motion proxy"
            print "problem was: ", e

        # First, wake up.
      #  motion.wakeUp()
      #  motion.setStiffnesses("Body", 1)
      #  
        # Add target to track.
        self.targetName = "Face"
        self.faceWidth = 0.1

    def start(self):
        self.motion.setStiffnesses("Head", 1)
        self.faceDetection.subscribe("Test_Face", 500, 0.0 )
        self.faceDetection.enableTracking(True)
        self.faceProxy.registerTarget(self.targetName, self.faceWidth)

        # Then, start tracker.
        self.faceProxy.track(self.targetName)

        print "ALTracker successfully started, now show your face to robot!"
        print "Use Ctrl+c to stop this script."


    def stop(self):
        # HEEEEEERE
        # TODO please
        # wait til the faceDetection has a valid value (but I dont know what it gives back when there is no face detected...)
        # and maybe even put that in the facedetection class
        # no Ill put it there
        while self.memoryProxy.getData(memValue, 0) == :
            pass

        # Stop tracker.
        self.faceProxy.stopTracker()
        self.faceProxy.unregisterAllTargets()

        print "ALTracker stopped."


