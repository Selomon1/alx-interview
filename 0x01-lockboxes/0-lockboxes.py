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
    accessible_boxes = set([0])

    # Loop until any more boxes can't be accessed
    while accessible_boxes:
        box = accessible_boxes.pop()
        for key in boxes[box]:
            if key not in keys:
                keys.add(key)
                if key < len(boxes):
                    accessible_boxes.add(key)

    return len(keys) == len(boxes)
