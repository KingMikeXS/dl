import adv.adv_test
from core.advbase import *

def module():
    return Vice

class Vice(Adv):
    a1 = ('bk',0.2)
    #comment = 'reach 100 resist with Silke Lends a Hand'
    #import slot
    #conf = {}
    #conf['slots.a'] = slot.a.Silke_Lends_a_Hand()+slot.a.RR()
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)

