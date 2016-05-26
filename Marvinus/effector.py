# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:46:36 2016

@author: Gast1
"""

import motion
import almath
import positions

class Effector():
    def __init__(self, bodypart, rotator, proxy, frame = motion.FRAME_ROBOT, axisMask = almath.AXIS_MASK_ALL, isAbsolute = False, useSensorValues = False):
        self.bodypart = bodypart
        self.rotator = rotator
        self.proxy = proxy
        
        self.frame           = frame
        self.axisMask        = axisMask
        self.isAbsolute      = isAbsolute
        self.useSensorValues = useSensorValues
        
    def moveToAbsolutePosition(self, position, rotation):
        
        path = []
        currentTf = self.proxy.getTransform(str(self.bodypart), int(self.frame), bool(self.useSensorValues))
        targetTf  = almath.Transform(currentTf)
        backTf = almath.Transform(currentTf)
        
        targetTf.r1_c4 = position[0] # x
        targetTf.r2_c4 = position[1] # y
        targetTf.r3_c4 = position[2] # z
        
        arm, default, hand, rot = positions.getDefaultPosition(self.bodypart)
        backTf.r1_c4 = default[0] # x
        backTf.r2_c4 = default[1] # y
        backTf.r3_c4 = default[2] # z
        
        path.append(list(targetTf.toVector()))
        path.append(list(backTf.toVector()))
        
        #print(path)
    
        # Go to the target and back again
        times      = [2.0,4.0] # seconds
    
        self.proxy.transformInterpolations(self.bodypart, self.frame, path, self.axisMask, times)
        
        names = list()
        times = list()
        keys = list()
    
        names.append(self.rotator)
        times.append([1, 3])
        keys.append([0,0.4])
        
        isAbsoluteWrist = True
        self.proxy.angleInterpolation(names, keys, times, isAbsoluteWrist)
    
    def getAbsolutePosition(self):
        currentTf = self.proxy.getTransform(str(self.bodypart), int(self.frame), bool(self.useSensorValues))
        currentTf = almath.Transform(currentTf)
        return [currentTf.r1_c4,currentTf.r2_c4,currentTf.r3_c4]
        
    def getWristAngle(self):
        self.proxy.getAngles(self.rotator, True)
    