from slot import *

class HDT1_Crimson_Fang(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 728
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Savage Crimson
    a = [('k', 0.3, 'vs HMS')]

class HDT2_Flamerulers_Maw(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 1455
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Savage Flameruler
    a = []

class HDT1_Tidal_Fang(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 728
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Vicious Tides
    a = [('k', 0.3, 'vs HBH')]

class HDT2_Tiderulers_Maw(WeaponBase):
    ele = ['water']
    wt = 'dagger'
    att = 1455
    s3 = {
        "dmg"      : 1.15*8   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 3.37     ,
        "hit"      : 8        ,
    } # Vicious Tideruler
    a = []

class HDT1_Galestorm_Fang(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 691
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Merciless Galestorm
    a = [('k', 0.3, 'vs HMC')]

class HDT2_Windrulers_Maw(WeaponBase):
    ele = ['wind']
    wt = 'dagger'
    att = 1383
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Merciless Windruler
    a = []

class HDT1_Lightning_Fang(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 706
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Ferocious Lightning
    a = [('k', 0.3, 'vs HZD')]

class HDT2_Fulminators_Maw(WeaponBase):
    ele = ['light']
    wt = 'dagger'
    att = 1412
    s3 = {
        "dmg"      : 1.64*5   ,
        "sp"       : 6145     ,
        "startup"  : 0.1      ,
        "recovery" : 2.45     ,
        "hit"      : 5        ,
    } # Ferocious Fulminator
    a = []

class HDT1_Darkened_Fang(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 706
    s3 = {
        "dmg"      : 1.73*5   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 2.3      ,
        "hit"      : 5        ,
    } # Bloodstarved Darkness
    a = [('k', 0.3, 'vs HJP')]

class HDT2_Shaderulers_Maw(WeaponBase):
    ele = ['shadow']
    wt = 'dagger'
    att = 1412
    s3 = {
        "dmg"      : 1.73*5   ,
        "sp"       : 6590     ,
        "startup"  : 0.1      ,
        "recovery" : 2.3      ,
        "hit"      : 5        ,
    } # Bloodstarved Shadowruler
    a = []

class Chimeratech_Elite(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 981
    s3 = {} #
    a = [('uo', 0.04)]

class Agito_Hrotti(WeaponBase):
    ele = ['flame']
    wt = 'dagger'
    att = 1513
    s3 = {
        "buff"     : ('self',0.20,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð
    a = []

class Agito0UB_Hrotti(Agito_Hrotti):
    att = 981
    s3 = {
        "buff"     : ('self',0.10,-1,'att','buff',True),
        "sp"       : 3000       ,
        "startup"  : 0.10+0.15  ,
        "recovery" : 1.05-0.15  ,
    } # Megingjörð

class UnreleasedAgito_WaterDagger(Agito_Hrotti):
    ele = ['water']

class UnreleasedAgito_WindDagger(Agito_Hrotti):
    ele = ['wind']

class UnreleasedAgito_LightDagger(Agito_Hrotti):
    ele = ['light']

class UnreleasedAgito_ShadowDagger(Agito_Hrotti):
    ele = ['shadow']

flame = Agito_Hrotti
water = HDT2_Tiderulers_Maw
wind = HDT2_Windrulers_Maw
light = HDT2_Fulminators_Maw
shadow = HDT2_Shaderulers_Maw