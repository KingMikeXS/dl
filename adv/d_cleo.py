import adv.adv_test
from core.advbase import *
from slot.d import *
from module import energy

def module():
    return Dragonyule_Cleo

class Dragonyule_Cleo(Adv):
    a1 = ('a',0.13,'hp70')
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel or fsc
        `s3, fsc
        `fs, seq=5
        """

    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun
        if this.condition('always connect hits'):
            this.dmg_proc = this.c_dmg_proc

    def c_prerun(this):
        this.stance = 0
        this.ehit = 0
        this.energy = energy.Energy(this,
                self={'s1':1,'hit':1},
                team={'s1':1}
                )
    def prerun(this):
        this.stance = 0
        this.ehit = 0
        this.energy = energy.Energy(this,
                self={},
                team={}
                )


    def c_dmg_proc(this, name, amount):
        if this.hits // 30 > this.ehit:
            this.energy.add_energy('hit')
            this.ehit = this.hits // 30

    def s1_proc(this, e): # buggy lvl3 s1
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
            Teambuff('s1s',0.1,10).on()
        elif this.stance == 2:
            this.stance = 0
            Teambuff('s1s',0.1,10).on()
            Teambuff('s1c',0.08,10,'crit','chance').on()




if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)
    # conf['s1_sp'] = 2400
    # conf['s1_dmg'] = 0.63*11
    # conf['str_adv'] = 474-17
    # module().comment = 'use s1 in lvl2'
    # adv_test.test(module(), conf, verbose=0)
