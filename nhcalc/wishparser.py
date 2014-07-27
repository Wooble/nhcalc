class NethackItem(object):
    pass


def parsewish(wish):
    if wish in ('nothing', 'nil', 'none'):
        return None

    obj = NethackItem()
    bp = 0
    blessed = cursed = uncursed = 0

    while bp < len(wish):

        if wish[bp:].startswith("blessed ") or wish[bp:].startswith("holy "):
            blessed = 1
            bp += wish[bp:].index(" ")
        elif (wish[bp:].startswith("cursed ")
              or wish[bp:].startswith("unholy ")):
            cursed = 1
            bp += wish[bp:].index(" ")
        elif wish[bp:].startswith("uncursed "):
            uncursed = 1
            bp += wish[bp:].index(" ")
        else:
            bp += 1

    obj.buc = "uncursed"
    if cursed:
        obj.buc = "cursed"
    elif uncursed:
        obj.buc = "uncursed"
    elif blessed:
        obj.buc = "blessed"

    return obj
