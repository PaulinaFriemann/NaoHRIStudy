# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:46:36 2016

@author: Gast1
"""
import time
import motion
import almath
import positions
from naoqi import ALProxy


class Effector:
    def __init__(self, IP, PORT):

        try:
            self.proxy = ALProxy("ALMotion", IP, PORT)
        except Exception, e:
            print "could not create motion proxy"
            print "problem was: ", e

        self.proxy.setStiffnesses("Body", 0)
        self.proxy.stiffnessInterpolation('LArm', 1, 0.01)
        self.proxy.stiffnessInterpolation('RArm', 1, 0.01)

    def hit_key(self,key, sleep_time=0.5):
        arm,position,default = positions.get_position(key)
        self.move_to_absolute_position(position,default,arm)
        time.sleep(sleep_time)

    def move_to_absolute_position(self, position, default, arm):      
        self.proxy.setAngles(arm,position[1],0.2)
        time.sleep(0.3)
        self.proxy.setAngles(arm,position[0],0.1)
        time.sleep(0.3)
        self.proxy.setAngles(arm,position[1],0.1)
        time.sleep(0.4)
        self.proxy.setAngles(arm,default,0.2)            
    
    def get_absolute_position(self,arm):
        keys = self.proxy.getAngles(arm, True)
        return keys          
        
    def set_stiff(self, true, hand):
        self.proxy.stiffnessInterpolation(hand, int(true), 0.01)