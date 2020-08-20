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
READABLE['monestary_floor_etching'] = {'title': 'Floor Plaque', 'text': 'Peace only\nhas meaning\nin community', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0000'] = {'title': 'Grave', 'text': 'RIP Brother Albard\nMaster of Bees\n2507-2573', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0001'] = {'title': 'Grave', 'text': 'RIP Brother Donaldson\nFriend of Nature\n2499-2581', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0002'] = {'title': 'Grave', 'text': 'RIP Brother Antilles\nLover of Poetry\n2481-2576', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0003'] = {'title': 'Grave', 'text': 'RIP Sister Sensara\nBrewer of Ales\n2505-2589', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0004'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0005'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0006'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0007'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0008'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0009'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0010'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0011'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0012'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0013'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0014'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0015'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0016'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0017'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0018'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0019'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0020'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0021'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0022'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0023'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0024'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0025'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0026'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0027'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0028'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0029'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0030'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0031'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0032'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0033'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0034'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0035'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0036'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0037'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0038'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0039'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0040'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0041'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0042'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0043'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0044'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0045'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0046'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0047'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0048'] = {'title': 'Grave', 'text': 'RIP ', 'audio': '', 'color': WHITE, 'read': False}
