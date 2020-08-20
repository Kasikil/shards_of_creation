####################################################################
#
#
# Shards of Creation -- scripts.readable --
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


READABLE = {}
# READABLE[] = {'title': '', 'text': '', 'audio': '', 'color': '', 'read': False}
READABLE['monestary_floor_etching'] = {'title': 'Floor Plaque', 'text': 'Peace only has meaning in community', 'audio': '', 'color': WHITE, 'read': False}
