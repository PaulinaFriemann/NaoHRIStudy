# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:46:36 2016

@author: Gast1
"""

import motion
import almath
import positions
from naoqi import ALProxy


class Effector:
    def __init__(self, bodypart, rotator, IP, PORT, frame = motion.FRAME_ROBOT, axisMask = almath.AXIS_MASK_ALL, isAbsolute = False, useSensorValues = False):
        self.bodypart = bodypart
        self.rotator = rotator
        
        self.frame           = frame
        self.axisMask        = axisMask
        self.isAbsolute      = isAbsolute
        self.useSensorValues = useSensorValues

        try:
            self.proxy = ALProxy("ALMotion", IP, PORT)
        except Exception, e:
            print "could not create motion proxy"
            print "problem was: ", e

        self.proxy.wakeUp()
        self.proxy.closeHand('LHand')
        self.proxy.stiffnessInterpolation('LHand', 1, 0.01)

        # self.proxy.setStiffnesses("Body", 0)

    def move_to_absolute_position(self, position, rotation):
        
        path = []
        currentTf = self.proxy.getTransform(str(self.bodypart), int(self.frame), bool(self.useSensorValues))
        targetTf  = almath.Transform(currentTf)
        backTf = almath.Transform(currentTf)
        
        targetTf.r1_c4 = position[0] # x
        targetTf.r2_c4 = position[1] # y
        targetTf.r3_c4 = position[2] # z
        
        arm, default, hand, rot = positions.get_default_position(self.bodypart)
        backTf.r1_c4 = default[0] # x
        backTf.r2_c4 = default[1] # y
        backTf.r3_c4 = default[2] # z
        
        path.append(list(targetTf.toVector()))
        path.append(list(backTf.toVector()))
        
        #print(path)
    
        # Go to the target and back again
        times      = [2.0, 4.0] # seconds
    
        self.proxy.transformInterpolations(self.bodypart, self.frame, path, self.axisMask, times)
        
        names = list()
        times = list()
        keys = list()
    
        names.append(self.rotator)
        times.append([1, 3])
        keys.append([0,0.4])
        
        isAbsoluteWrist = True
        self.proxy.angleInterpolation(names, keys, times, isAbsoluteWrist)
    
    def get_absolute_position(self):
        currentTf = self.proxy.getTransform(str(self.bodypart), int(self.frame), bool(self.useSensorValues))
        currentTf = almath.Transform(currentTf)
        return [currentTf.r1_c4,currentTf.r2_c4,currentTf.r3_c4]
        
    def get_wrist_angle(self):
        self.proxy.getAngles(self.rotator, True)