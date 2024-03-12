#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """
    checking if available boxes can be opened
    """

    if not boxes:
        return False

    # Initialize a set to track the keys
    keys = set([0])

    # Initialize a set to track boxes can be accessed
    accessible_boxes = [0]
    i = 0

    # Loop until any more boxes can't be accessed
    while i < len(accessible_boxes):
        box = accessible_boxes[i]
        for key in boxes[box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                accessible_boxes.add(key)
        i += 1

    return len(keys) == len(boxes)
