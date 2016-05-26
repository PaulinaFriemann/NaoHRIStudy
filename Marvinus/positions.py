# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:03:07 2016

@author: Gast1
"""

default_positions = {
    'LArm': [0.10129939019680023, 0.22932101786136627, 0.23544558882713318],
    'RArm': []
}

default_rotations = {
    'LArm': [],
    'RArm': []
}

defaults = {
    'position': default_positions,
    'rotation': default_rotations
}

positions_left = {}
positions_right = {}

positions_left['C'] = [0.12560521066188812, 0.2638903856277466, 0.17710906267166138]
positions_left['D'] = [0.05927547812461853, 0.24047115445137024, 0.18063606321811676]
positions_left['E'] = []
positions_left['F'] = []

positions_right['G'] = []
positions_right['A'] = []
positions_right['B'] = []
positions_right['Ch'] = []

positions = {
    'LArm': positions_left,
    'RArm': positions_right
}

rotations_left = {}
rotations_right = {}

rotations_left['C'] = [0.39879798889160156]
rotations_left['D'] = []
rotations_left['E'] = []
rotations_left['F'] = []

rotations_right['G'] = []
rotations_right['A'] = []
rotations_right['B'] = []
rotations_right['Ch'] = []

rotations = {
    'LArm': rotations_left,
    'RArm': rotations_right
}

keys = {
    'position': positions,
    'rotation': rotations
}


def get_default_position(key):
    arm = key #'LArm' if key in positions_left else 'RArm'
    hand = 'LWristYaw' if arm == 'LArm' else 'RWristYaw'
    return arm, defaults['position'][arm], hand, defaults['rotation'][arm]


def get_position(key):
    arm = 'LArm' if key in positions_left else 'RArm'
    hand = 'LWristYaw' if arm == 'LArm' else 'RWristYaw'
    return arm, keys['position'][arm][key], hand, keys['rotation'][arm][key]
