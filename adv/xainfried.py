import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Xainfried

class Xainfried(Adv):
    comment = 'use s1 only to cancel c5 or fs'
    a1 = ('dc', 3)
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """

    def d_slots(this):
        if 'wand' not in this.ex:
            this.conf.slot.d = Siren()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

