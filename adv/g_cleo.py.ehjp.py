import adv.adv_test
from core.advbase import *
import adv.g_cleo
from slot.a import Amulet

class King_of_the_Skies(Amulet):
    att = 39

class Candy_Couriers(Amulet):
    att = 65
    a = [('s',0.40)]

def module():
    return Gala_Cleo

class Gala_Cleo(adv.g_cleo.Gala_Cleo):
    comment = '4 Gleo vs EHJP; simulated break & no team dps; s2 s1 c5 fs s3 c5 s1 c5 c5 c5 fs s2 s1 dragon end'
    conf = adv.g_cleo.Gala_Cleo.conf.copy()
    conf['slot.a'] = Candy_Couriers()+King_of_the_Skies()
    conf['slot.d'] = slot.d.Shinobi()
    conf['acl'] = "`rotation"
    conf['rotation'] = """
        s2 s1 c5 fs s3 c5 s1 c5 c5 c5 fs s2 s1 dragon end
    """

    def prerun(this):
        super().prerun()
        this.dragonform.dragon_gauge = 100
        this.dragonform.conf.act = 'c3 s c3 end'
        this.odbk = 991202+792960
        this.ehjp = 4488479
        this.dmgsum = 0
        adv.adv_test.team_dps = 0
        this.broken_punisher = Selfbuff(name='candy_couriers', value=0.25, duration=-1, mtype='att', morder='bk')

    def dmg_proc(this, name, amount):
        this.dmgsum += int(amount) * 4
        if this.dmgsum > this.odbk and this.dmgsum-(int(amount)*4) < this.odbk:
            log('debug', 'odbk', 'BREAK start')
            this.broken_punisher.on()
            Timer(this.break_end).on(10)
        log('debug', 'ehjp', '{}/{} ({:.0%})'.format(this.dmgsum, this.ehjp, this.dmgsum/this.ehjp))
        if this.dmgsum > this.ehjp:
            log('debug', 'ehjp is kill')

    def break_end(this, t):
        log('debug', 'odbk', 'BREAK end')
        this.broken_punisher.off()

    def dmg_make(this, name, dmg_coef, dtype=None, fixed=False):
        if this.broken_punisher.get():
            generic_name = name.split('_')[0]
            if generic_name[0] == 'x':
                generic_name = 'attack'
            if generic_name[0] == 'd':
                generic_name = name.split('_')[1][0:2]
            name = 'o_'+generic_name+'_on_bk'
        if dtype == None:
            dtype = name
        count = this.dmg_formula(dtype, dmg_coef) if not fixed else dmg_coef
        log('dmg', name, count)
        this.dmg_proc(name, count)
        return count

    def dmg_formula(this, name, dmg_coef):
        att = 1.0 * this.att_mod() * this.base_att
        if this.broken_punisher.get():
            armor = 10.0 * this.def_mod() * 0.6
        else:
            armor = 10.0 * this.def_mod()
        return 5.0/3 * dmg_coef * this.dmg_mod(name) * att/armor * 1.5   # true formula

    def s2_proc(this, e):
        super().s2_proc(e)
        Debuff('s2',0.10,20).on()
        Debuff('s2',0.10,20).on()
        Debuff('s2',0.10,20).on()

    def fs_proc(this, e):
        if this.fsa_charge and this.a1_buffed:
            Debuff('a1_str',-0.25,10,1,'att','buff').on()
            Debuff('a1_str',-0.25,10,1,'att','buff').on()
            Debuff('a1_str',-0.25,10,1,'att','buff').on()
        super().fs_proc(e)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0)

