####################################################################
#
#
# Shards of Creation -- assets.dialogue_scripts.dialogue --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import pygame

    # Non-Standard Imports
    from settings.settings import *
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

# DIALOGUE[] = {'speaker': '', 'dialogue': '', 'audio': '', 'color': '', 'next': [], 'read': False}
DIALOGUE = {}

# Zuan
DIALOGUE[0] = {'speaker': 'Zuan', 'dialogue': 'Good day my friend.', 'audio': '', 'color': WHITE, 'next': [1], 'read': False}
DIALOGUE[1] = {'speaker': 'Player', 'dialogue': 'Where am I?\nKnow any stories you\'d be willing to share?', 'audio': '', 'color': WHITE, 'next': [2, 14], 'read': False}
DIALOGUE[2] = {'speaker': 'Zuan', 'dialogue': 'You are currently in the woodland monestary. My name is Zuan. Do you know how you got here?', 'audio': '', 'color': WHITE, 'next': [3], 'read': False}
DIALOGUE[3] = {'speaker': 'Player', 'dialogue': 'No...', 'audio': '', 'color': WHITE, 'next': [4], 'read': False}
DIALOGUE[4] = {'speaker': 'Zuan', 'dialogue': 'We found you with a large bump on your head in the forest four days ago.', 'audio': '', 'color': WHITE, 'next': [5], 'read': False}
DIALOGUE[5] = {'speaker': 'Player', 'dialogue': 'Four days. Wow. I... I can\'t remember anything.', 'audio': '', 'color': WHITE, 'next': [6], 'read': False}
DIALOGUE[6] = {'speaker': 'Zuan', 'dialogue': 'Oh my, it must have been quite a bump.', 'audio': '', 'color': WHITE, 'next': [7], 'read': False}
DIALOGUE[7] = {'speaker': 'Player', 'dialogue': 'Can you tell me anything about myself?', 'audio': '', 'color': WHITE, 'next': [8], 'read': False}
DIALOGUE[8] = {'speaker': 'Zuan', 'dialogue': 'We found you with this unique musical \'instrument\' and a note.', 'audio': '', 'color': WHITE, 'next': [9], 'read': False}
DIALOGUE[9] = {'speaker': 'Zuan', 'dialogue': 'Maybe your \'instrument\' can help you remember more? I know music helps me.', 'audio': '', 'color': WHITE, 'next': [10], 'read': False}
DIALOGUE[10] = {'speaker': 'Player', 'dialogue': 'Thanks, I\'ll give it a try perhaps.', 'audio': '', 'color': WHITE, 'next': [11], 'read': False}
DIALOGUE[11] = {'speaker': 'Zuan', 'dialogue': 'What should we call you?', 'audio': '', 'color': WHITE, 'next': [12], 'read': False}
DIALOGUE[12] = {'speaker': 'Player', 'dialogue': 'The Traveler\nThe Wanderer\nThe Musician', 'audio': '', 'color': WHITE, 'next': [13, 13, 13], 'read': False, 'update': {'update_field': 'name', 'options': ['The Traveler', 'The Wanderer', 'The Musician']}}
DIALOGUE[13] = {'speaker': 'Zuan', 'dialogue': 'Okay, we\'ll call you [name]. You are welcome to stay at the monestary as long or short as you\'d like.', 'audio': '', 'color': WHITE, 'next': [1], 'read': False}
DIALOGUE[14] = {'speaker': 'Zuan', 'dialogue': 'Perhaps once Kasikil gets around to implementing this task.', 'audio': '', 'color': WHITE, 'next': [1], 'read': False}