import copy
from core import Conf
from ability import *

class Slot(object):
    att = 0
    ele = 'none'
    wt = 'none'
    stype = 'slot'
    onele = 0

    a = None
    mod = None
    conf = None
    def __init__(this):
        if not this.mod:
            this.mod = []
        if not this.conf:
            this.conf = Conf()
        if not this.a:
            this.a = []

    def setup(this, c):
        if c.ele == this.ele :
            this.onele = 1
        if this.wt != 'none' and c.wt != this.wt:
            raise ValueError('Wrong weapon type, expected {} but got {}'.format(this.wt, c.wt))

    def oninit(this, adv):
        adv.conf(this.conf)

        i = this.stype
        j = this.mod
        if type(j) == tuple:
            adv.Modifier(i,*j)
        elif type(j) == list:
            idx = 0
            for k in j:
                adv.Modifier(i+'_%d'%idx,*k)
                idx += 1
        elif type(j) == dict:
            idx = 0
            for k in j:
                adv.Modifier(i+k+'_%d'%idx,*j[k])
                idx += 1


class CharacterBase(Slot):
    name = 'null'
    stars = 5
    ex = {}
    def setup(this):
        return

    def oninit(this, adv):
        Slot.oninit(this, adv)
        j = this.ex
        if type(j) == tuple:
            this.a.append(j)
        elif type(j) == list:
            this.a += j
        elif type(j) == dict:
            for i in j:
                this.a.append(j[i])



class WeaponBase(Slot):
    stype = 'w'
    wt = 'none'
    s3 = Conf()
    ele = [] # or ''

    def setup(this, c):
        super(WeaponBase, this).setup(c)
        if type(this.ele) == list:
            for i in this.ele:
                if c.ele == i :
                    this.onele = 1
                    break
        
        if this.onele :
            this.att *= 1.5
            this.conf.s3 = Conf(this.s3)
        elif 'all' in this.ele :
            this.conf.s3 = Conf(this.s3)

        if this.wt == 'axe':
            this.mod.append(('crit','chance',0.04))
        else :
            this.mod.append(('crit','chance',0.02))

class DragonBase(Slot):
    stype = 'd'
    a = [('a', 0.60)]
    default_dragonform = {
        'duration': 600 / 60, # 10s dragon time
        'dracolith': 0.40, # base dragon damage
        'exhilaration': 0, # psiren aura
        'skill_use': 1, # number of skill usage
        'gauge_iv': 15, # gauge interval
        'latency': 0, # amount of delay for cancel
        'act': 'end',

        'dshift.startup': 96 / 60, # shift 102 -> 96 + 6
        'dshift.recovery': 0 / 60, # assumed cancel
        'dshift.dmg': 2.00,
        'dshift.hit': 1,

        'dx1.recovery': 0,
        'dx2.recovery': 0,
        'dx3.recovery': 0,
        'dx4.recovery': 0,
        'dx5.recovery': 0,
        'ds.startup': 0,

        'dodge.startup': 40 / 60, # dodge frames
        'dodge.recovery': 0,
        'dodge.hit': 0,

        'end.startup': 0, # amount of time needed to kys, 0 default
        'end.recovery': 0
    }
    dragonform = {}

    def setup(this, c):
        Slot.setup(this, c)
        if this.onele:
            this.att *= 1.5
        else:
            this.a = []

    def ds_proc(self):
        try:
            return self.adv.dmg_make('d_ds',self.adv.dragonform.conf.ds.dmg,'s')
        except:
            return 0

    def oninit(self, adv):
        super().oninit(adv)
        from core.dragonform import DragonForm
        self.adv = adv
        if 'dragonform' in adv.conf:
            name = type(adv).__name__
            dconf = Conf(self.default_dragonform)
            dconf += adv.conf.dragonform
            self.adv.dragonform = DragonForm(name, dconf, adv, adv.ds_proc)
        else:
            name = type(self).__name__
            dconf = Conf({**self.default_dragonform, **self.dragonform})
            self.adv.dragonform = DragonForm(name, dconf, adv, self.ds_proc)

class Amuletempty(object):
    stype = 'a2'
    def oninit(this,adv):
        return
    def setup(this, c):
        return


class AmuletBase(Slot):
    ae = Amuletempty()
    stype = 'a'
    a2 = None

    def __add__(this, another):
        if type(this) is type(another):
            raise ValueError('Cannot equip two of the same wyrmprint')
        this.a2 = another
        this.a2.stype = 'a2'
        return this

    def oninit(this, adv):
        Slot.oninit(this, adv)
        if this.a2:
            this.a2.a2 = None
            this.a2.oninit(adv)



class Slots(object):
    #w = None
    #d = None
    #a = None
    #a2 = None
    #w = WeaponBase()
    #d = DragonBase()
    #a = AmuletBase()+AmuletBase()
    #c = CharacterBase()
    #a2 = AmuletBase()
    def __str__(this):
        r = str(this.c) + '\n'
        r += str(this.d) + '\n'
        r += str(this.w) + '\n'
        r += str(this.a) + '\n'
        r += str(this.a.a2) + '\n'
        return r


    def __init__(this):
        this.c = CharacterBase()
        #this.w = WeaponBase()
        #this.d = DragonBase()
        #this.a = AmuletBase()+AmuletBase()
        this.w = None
        this.d = None
        this.a = None

    def __setup(this):
        this.c.setup()
        this.w.setup(this.c)
        this.d.setup(this.c)
        this.a.setup(this.c)


    def oninit(this, adv):
        tmp = copy.deepcopy(this)
        this.tmp = tmp
        tmp.__setup()
        tmp.c.oninit(adv)
        tmp.w.oninit(adv)
        tmp.d.oninit(adv)
        tmp.a.oninit(adv)
        a = tmp.c.a + tmp.w.a + tmp.d.a + tmp.a.a
        this.abilities = a
        #for i in a:
        #    Ability(*i).oninit(adv)
        for i in tmp.c.a:
            Ability(*i).oninit(adv,'c_')
        for i in tmp.w.a:
            Ability(*i).oninit(adv,'w_')
        for i in tmp.d.a:
            Ability(*i).oninit(adv,'d_')
        for i in tmp.a.a:
            Ability(*i).oninit(adv,'a_')


    def att(this, forte=None):
        tmp = copy.deepcopy(this)
        this.tmp = tmp
        tmp.__setup()
        if not forte:
            return tmp.c.att + tmp.d.att + tmp.w.att + tmp.a.att
        # return tmp.c.att*forte.c(tmp.c.ele,tmp.c.wt) + tmp.d.att*forte.d(tmp.d.ele) + tmp.w.att + tmp.a.att
        return (tmp.c.att+100)*forte.c(tmp.c.ele,tmp.c.wt) + tmp.d.att*forte.d(tmp.d.ele) + tmp.w.att + (tmp.a.att+200)

    def _att(this, forte=None):
        a = this.att(forte)
        dm = this.tmp.d.mod
        md = 0
        if type(dm) == list:
            for i in dm:
                if i[0] == 'att':
                    md += i[2]
        elif type(dm) == tuple:
            if dm[0] == 'att':
                md += dm[2]
        return a+a*md

import slot.d as d
import slot.w as w
import slot.a as a

def main():
    s = Slots('elisanne')
    import slot
    slot.DragonBase = DragonBase
    #slot.d.base(DragonBase)
    import slot.d.water
    import slot.d.flame
    s.d = slot.d.water.Dragon()
    s.setup()
    print(s.d.att)

if __name__ == "__main__":
    main()
