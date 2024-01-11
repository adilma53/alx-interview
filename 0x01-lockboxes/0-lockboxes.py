#!/usr/bin/python3
""" lockboxes problem"""


def canUnlockAll(boxes):
    """ lockboxes problem"""
    for i in range(1, len(boxes)):
        track = False
        for box in range(len(boxes)):
            if i in boxes[box] and box != i:
                track = True
                break
        if not track:
            return False
    return True
