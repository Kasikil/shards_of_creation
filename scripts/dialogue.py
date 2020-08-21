####################################################################
#
#
# Shards of Creation -- scripts.dialogue --
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
DIALOGUE[1] = {'speaker': '[name]', 'dialogue': '\n1. Where am I?\n2. Know any stories you\'d be willing to share?', 'audio': '', 'color': WHITE, 'next': [2, 99], 'read': False}
DIALOGUE[2] = {'speaker': 'Zuan', 'dialogue': 'You are currently in the woodland monestary. My name is Zuan. Do you know how you got here?', 'audio': '', 'color': WHITE, 'next': [3], 'read': False}
DIALOGUE[3] = {'speaker': '[name]', 'dialogue': 'No...', 'audio': '', 'color': WHITE, 'next': [4], 'read': False}
DIALOGUE[4] = {'speaker': 'Zuan', 'dialogue': 'We found you with a large bump on your head in the forest four days ago.', 'audio': '', 'color': WHITE, 'next': [5], 'read': False}
DIALOGUE[5] = {'speaker': '[name]', 'dialogue': 'Four days. Wow. I... I can\'t remember anything.', 'audio': '', 'color': WHITE, 'next': [6], 'read': False}
DIALOGUE[6] = {'speaker': 'Zuan', 'dialogue': 'Oh my, it must have been quite a bump.', 'audio': '', 'color': WHITE, 'next': [7], 'read': False}
DIALOGUE[7] = {'speaker': '[name]', 'dialogue': 'Can you tell me anything about myself?', 'audio': '', 'color': WHITE, 'next': [8], 'read': False}
DIALOGUE[8] = {'speaker': 'Zuan', 'dialogue': 'We found you with this unique musical \'instrument\' and a note.', 'audio': '', 'color': WHITE, 'next': [9], 'read': False}
DIALOGUE[9] = {'speaker': 'Zuan', 'dialogue': 'Maybe your \'instrument\' can help you remember more? I know music helps me.', 'audio': '', 'color': WHITE, 'next': [10], 'read': False}
DIALOGUE[10] = {'speaker': '[name]', 'dialogue': 'Thanks, I\'ll give it a try perhaps.', 'audio': '', 'color': WHITE, 'next': [11], 'read': False}
DIALOGUE[11] = {'speaker': 'Zuan', 'dialogue': 'What should we call you?', 'audio': '', 'color': WHITE, 'next': [12], 'read': False}
DIALOGUE[12] = {'speaker': '[name]', 'dialogue': '\n1. The Traveler\n2. The Wanderer\n3. The Musician', 'audio': '', 'color': WHITE, 'next': [13, 13, 13], 'read': False, 'update': {'update_field': 'name', 'options': ['The Traveler', 'The Wanderer', 'The Musician']}}
DIALOGUE[13] = {'speaker': 'Zuan', 'dialogue': 'Okay, we\'ll call you [name]. You are welcome to stay at the monestary as long or short as you\'d like.', 'audio': '', 'color': WHITE, 'next': [1], 'read': False}

DIALOGUE[99] = {'speaker': 'Zuan', 'dialogue': 'Perhaps once Kasikil gets around to implementing this task.', 'audio': '', 'color': WHITE, 'next': [1], 'read': False}

# Corris
DIALOGUE[100] = {'speaker': 'Corris', 'dialogue': 'Hello, my name is Corris. This is my home.', 'audio': '', 'color': WHITE, 'next': [101], 'read': False}
DIALOGUE[101] = {'speaker': '[name]', 'dialogue': '\n1. How long have you lived here?\n2. Know any stories you\'d be willing to share?', 'audio': '', 'color': WHITE, 'next': [102, 199], 'read': False}
DIALOGUE[102] = {'speaker': 'Corris', 'dialogue': 'I moved here nearly 50 years ago, 45 of which I spent with my partner.', 'audio': '', 'color': WHITE, 'next': [103], 'read': False}
DIALOGUE[103] = {'speaker': '[name]', 'dialogue': 'Those sound like many beautiful years you spent together.', 'audio': '', 'color': WHITE, 'next': [104], 'read': False}
DIALOGUE[104] = {'speaker': 'Corris', 'dialogue': 'They were, I truly miss him.', 'audio': '', 'color': WHITE, 'next': [105], 'read': False}
DIALOGUE[105] = {'speaker': '[name]', 'dialogue': 'What was his name?', 'audio': '', 'color': WHITE, 'next': [106], 'read': False}
DIALOGUE[106] = {'speaker': 'Corris', 'dialogue': 'His name was Dalin. He had kind eyes and a gentle soul...', 'audio': '', 'color': WHITE, 'next': [107], 'read': False}
DIALOGUE[107] = {'speaker': 'Corris', 'dialogue': '...could you do me a favor?', 'audio': '', 'color': WHITE, 'next': [108], 'read': False}
DIALOGUE[108] = {'speaker': '[name]', 'dialogue': 'It would be my priveldge.', 'audio': '', 'color': WHITE, 'next': [109], 'read': False}
DIALOGUE[109] = {'speaker': 'Corris', 'dialogue': 'Dalin\'s favorite flower was a lily...', 'audio': '', 'color': WHITE, 'next': [110], 'read': False}
DIALOGUE[110] = {'speaker': 'Corris', 'dialogue': '...next time you next find one, could you offer a blessing in his memory?', 'audio': '', 'color': WHITE, 'next': [111], 'read': False}
DIALOGUE[111] = {'speaker': '[name]', 'dialogue': 'Consider it done. Ubuntu.', 'audio': '', 'color': WHITE, 'next': [112], 'read': False}
DIALOGUE[112] = {'speaker': 'Corris', 'dialogue': 'Ubuntu.', 'audio': '', 'color': WHITE, 'next': [101], 'read': False}

DIALOGUE[199] = {'speaker': 'Zuan', 'dialogue': 'Perhaps once Kasikil gets around to implementing this task.', 'audio': '', 'color': WHITE, 'next': [101], 'read': False}

# Elsk
DIALOGUE[200] = {'speaker': 'Elsk', 'dialogue': 'Greetings soon-to-be friend. Kindess and love to you!', 'audio': '', 'color': WHITE, 'next': [200], 'read': False}

# Morad
DIALOGUE[300] = {'speaker': 'Morad', 'dialogue': 'Ah, a guest! My home is your home! Join me for some bread and honey.', 'audio': '', 'color': WHITE, 'next': [300], 'read': False}

# Sovik
DIALOGUE[400] = {'speaker': 'Sovik', 'dialogue': '*nods*', 'audio': '', 'color': WHITE, 'next': [400], 'read': False}

# Tinterbeck
DIALOGUE[500] = {'speaker': 'Tinterbeck', 'dialogue': 'You must join us for tea!', 'audio': '', 'color': WHITE, 'next': [500], 'read': False}

# Sivas
DIALOGUE[600] = {'speaker': 'Sivas', 'dialogue': 'Wow! You seem really cool! I am almost 7!', 'audio': '', 'color': WHITE, 'next': [600], 'read': False}

# Goat
DIALOGUE[700] = {'speaker': 'Goat', 'dialogue': 'Baaa? Make me better pixel art. Baaaa.', 'audio': '', 'color': WHITE, 'next': [700], 'read': False}

