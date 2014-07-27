class NethackItem(object):
    pass


def parsewish(wish):
    lcwish = ' ' + wish.lower()
    if lcwish in (' nothing', ' nil', ' none'):
        return None

    obj = NethackItem()

    obj.buc = 'uncursed'
    if ' cursed ' in lcwish or ' unholy ' in lcwish:
        obj.buc = 'cursed'
    elif ' uncursed ' in lcwish:
        obj.buc = 'uncursed'
    elif ' blessed ' in lcwish or ' holy' in lcwish:
        obj.buc = 'blessed'

    return obj
