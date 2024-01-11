#!/usr/bin/python3
""" lockboxes problem"""


def canUnlockAll(boxes):
    """ lockboxes problem"""
    for i in range(1, len(boxes)):
        f = False
        for box in range(len(boxes)):
            if k in boxes[box] and box != i:
                f = True
                break
        if not f:
            return False
    return True
