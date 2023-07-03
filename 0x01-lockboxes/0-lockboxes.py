#!/usr/bin/python3
''' lockbox module '''


def canUnlockAll(boxes):
    '''
        CanUnockAll
        ([boxes]): a list of list
    '''

    # initialize a list of unlocked boxes
    unlocked = [False] * len(boxes)
    # set the first box oprn
    unlocked[0] = True
    # iterate over the boxes
    for index, box in enumerate(boxes):
        # check if the box is unlocked
        if unlocked[index]:
            # get the keys in the box
            for index, key in enumerate(box):
                # set the box with a found key to open
                if key < len(unlocked):
                    unlocked[key] = True
                    # get the keys at the box that has been opened
                    # set the boxes with the keys to be open
                    for i in boxes[key]:
                        if i < len(unlocked):
                            unlocked[i] = True
    return all(unlocked)
