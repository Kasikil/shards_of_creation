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
# Monestary and Graveyard
# Row 1
READABLE['monestary_floor_etching'] = {'title': 'Floor Plaque', 'text': 'Peace only\nhas meaning\nin community', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0000'] = {'title': 'Grave', 'text': 'RIP Brother Adriel\nMaster of Bees\n2507-2573', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0001'] = {'title': 'Grave', 'text': 'RIP Brother Dan\nFriend of Nature\n2499-2581', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0002'] = {'title': 'Grave', 'text': 'RIP Brother Andrew\nLover of Poetry\n2481-2576', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0003'] = {'title': 'Grave', 'text': 'RIP Sister Sapphira\nBrewer of Ales\n2505-2589', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0004'] = {'title': 'Grave', 'text': 'RIP Sister Martha\nTickler of Ivories\n2508-2557', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0005'] = {'title': 'Grave', 'text': 'RIP Sister Ada\nKeeper of Lore\n2501-2576', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0006'] = {'title': 'Grave', 'text': 'RIP Sister Delilah\nForest Friend\n2493-2577', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0007'] = {'title': 'Grave', 'text': 'RIP Brother Elon\nHerb Gardner Extraordinaire\n2507-2588', 'audio': '', 'color': WHITE, 'read': False}
# Row 2
READABLE['grave_0008'] = {'title': 'Grave', 'text': 'RIP Sister Asher\nWalker of Wind\n2482-2570', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0009'] = {'title': 'Grave', 'text': 'RIP Brother Gideon\nJoyful Cook\n2477-2567', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0010'] = {'title': 'Grave', 'text': 'RIP Sister Eve\nMaster Carptener\n2460-2559', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0011'] = {'title': 'Grave', 'text': 'RIP Brother Philip\nSwept With A Smile\n2468-2570', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0012'] = {'title': 'Grave', 'text': 'RIP Brother Joel\nHealer of Hearts\n2481-2532', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0013'] = {'title': 'Grave', 'text': 'RIP Sister Dinah\nSeed Sower\n2472-2576', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0014'] = {'title': 'Grave', 'text': 'RIP Sister Salome\nWriter of Our History\n2488-2578', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0015'] = {'title': 'Grave', 'text': 'RIP Brother Solomon\nOrator of Life\n2498-2571', 'audio': '', 'color': WHITE, 'read': False}
# Row 3
READABLE['grave_0016'] = {'title': 'Grave', 'text': 'RIP Sister Tamar\nCheerfully Washed Linens\n2509-2595', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0017'] = {'title': 'Grave', 'text': 'RIP Sister Tabitha\nTable Cleaner and Listening Ear\n2467-2433', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0018'] = {'title': 'Grave', 'text': 'RIP Sister Miriam\nKeeper of the Grounds\n2468-2546', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0019'] = {'title': 'Grave', 'text': 'RIP Brother Seth\nPriest to Priests\n2490-2559', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0020'] = {'title': 'Grave', 'text': 'RIP Brother Thaddeus\nHarpist of Great Caliber\n2481-2573', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0021'] = {'title': 'Grave', 'text': 'RIP Sister Opah\nConductor of the Chant\n2474-2566', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0022'] = {'title': 'Grave', 'text': 'RIP Brother Silas\nPrayed with Entire Being\n2499-2545', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0023'] = {'title': 'Grave', 'text': 'RIP Sister Abigail\nMaster of Meditation\n2508-2578', 'audio': '', 'color': WHITE, 'read': False}
# Row 4
READABLE['grave_0024'] = {'title': 'Grave', 'text': 'RIP Brother Hezekiah\nMaster of Mending\n2488-2592', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0025'] = {'title': 'Grave', 'text': 'RIP Brother John\nPoet of Pottery\n2495-2525', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0026'] = {'title': 'Grave', 'text': 'RIP Brother John\nKnitter of Hats\n2460-2547', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0027'] = {'title': 'Grave', 'text': 'RIP Sister Hagar\nLived as Christ\n2488-2553', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0028'] = {'title': 'Grave', 'text': 'RIP Brother Hiram\nTraveler of Mercy\n2520-2577', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0029'] = {'title': 'Grave', 'text': 'RIP Sister Jezebel\nSongs of Gold\n2509-2576', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0030'] = {'title': 'Grave', 'text': 'RIP Sister Judith\nPainter of Canvas\n2532-2596', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0031'] = {'title': 'Grave', 'text': 'RIP Brother James\nDancer of Souls\n2487-2583', 'audio': '', 'color': WHITE, 'read': False}
# Row 5
READABLE['grave_0032'] = {'title': 'Grave', 'text': 'RIP Sister Lois\nWeaver of Tapestries\n2521-2578', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0033'] = {'title': 'Grave', 'text': 'RIP Brother Luke\nPond of Reflection\n2511-2580', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0034'] = {'title': 'Grave', 'text': 'RIP Sister Vashti\nKeeper of Lore\n2466-2512', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0035'] = {'title': 'Grave', 'text': 'RIP Brother Joe\nArchivist of Experience\n2510-2587', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0036'] = {'title': 'Grave', 'text': 'RIP Sister Zilpah\nFriend of Wildlife\n2469-2544', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0037'] = {'title': 'Grave', 'text': 'RIP Brother Simon\nMaster of Chess\n2478-2555', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0038'] = {'title': 'Grave', 'text': 'RIP Sister Sarai\nCultivator of Soil\n2490-2562', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0039'] = {'title': 'Grave', 'text': 'RIP Brother Benjamin\nPurveyor of Paper\n2475-2558', 'audio': '', 'color': WHITE, 'read': False}
# Row 6
READABLE['grave_0040'] = {'title': 'Grave', 'text': 'RIP Sister Mary\nKnitter of Branches\n2435-2524', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0041'] = {'title': 'Grave', 'text': 'RIP Sister Lydia\nWanderer of the Woods\n2444-2537', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0042'] = {'title': 'Grave', 'text': 'RIP Sister Joanna\nSlinger of Sourdough\n2453-2511', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0043'] = {'title': 'Grave', 'text': 'RIP Sister Elizabeth\nBrewmaster of Ales\n2439-2538', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0044'] = {'title': 'Grave', 'text': 'RIP Sister Damaris\nTiller of Gardens\n2447-2535', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0045'] = {'title': 'Grave', 'text': 'RIP Sister Bathsheba\nCollector of Texts\n2452-2541', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0046'] = {'title': 'Grave', 'text': 'RIP Sister Anna\nWelcomer of Strangers\n2432-2520', 'audio': '', 'color': WHITE, 'read': False}
READABLE['grave_0047'] = {'title': 'Grave', 'text': 'RIP Sister Claudia\nFriend of Wild Things\n2446-2531', 'audio': '', 'color': WHITE, 'read': False}
# Head
READABLE['grave_0048'] = {'title': 'Grave', 'text': 'RIP Sister Eve\n Layer of the Foundation\n2432-2512', 'audio': '', 'color': WHITE, 'read': False}

# Taize Village
READABLE['taize_welcome'] = {'title': 'Welcome Sign', 'text': 'Welcome to Taize Village!', 'audio': '', 'color': WHITE, 'read': False}
READABLE['corris_sign'] = {'title': 'House Sign', 'text': 'Corris and Dalin\nLove is a Lily', 'audio': '', 'color': WHITE, 'read': False}
READABLE['elsk_sign'] = {'title': 'House Sign', 'text': 'Elsk Home\nKindness And Love', 'audio': '', 'color': WHITE, 'read': False}
READABLE['morad_sign'] = {'title': 'House Sign', 'text': 'Morad\'s Dwelling\nSimple Pleasures', 'audio': '', 'color': WHITE, 'read': False}
READABLE['sovik_sign'] = {'title': 'House Sign', 'text': 'Sovik\nThe Way of Silence', 'audio': '', 'color': WHITE, 'read': False}
READABLE['tinterbeck_sign'] = {'title': 'House Sign', 'text': 'Tinterbeck Home\nCome Share Some Tea', 'audio': '', 'color': WHITE, 'read': False}
