import adv.adv_test
from core.advbase import *
from module import energy
from slot.a import *

def module():
    return Annelie


class Annelie(Adv):
    comment = '1121'
    a1 = ('s',0.35,'hp70')
    conf['acl'] = """
        `s1, s2.charged<=10000
        `s1, s=2
        `s2
        `s3
        `fs, seq=5 
        """

    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = RR()+JotS()
        else:
            this.conf.slot.a = RR()+BN()

    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

    def c_prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={'1':1,'2':2,'s2':2},
                team={'s2':2}
                )
        Event('energized').listener(this.energy_doublebuff)

    def prerun(this):
        this.stance = 0
        this.energy = energy.Energy(this, 
                self={},
                team={}
                )

  #  def debug(this):
  #      print this.slots.a.__class__.__name__
  #      print this.slots.a.a2.__class__.__name__


    def energy_doublebuff(this, e):
        Selfbuff("double_buff", 0.2, 15).on()

    def s1_proc(this, e):
        if this.stance == 0:
            this.dmg_make('s1_p1',0.1+8.14)
            this.energy.add_energy('1')
            this.stance = 1
        elif this.stance == 1:
            this.dmg_make('s1_p2',2*(0.1+4.07))
            this.energy.add_energy('2')
            this.stance = 2
        elif this.stance == 2:
            this.dmg_make('s1_p3',3*(0.1+3.54))
            this.stance = 0



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

