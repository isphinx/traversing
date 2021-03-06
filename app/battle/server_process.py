# coding:utf8

#from lupa import LuaRuntime
from shared.utils.const import const
from app.battle.battle_unit import BattleUnit
from random import randint
from shared.utils.lua_runtime import lua

#TYPE_GUIDE = 0              --演示关卡
#TYPE_STAGE_NORMAL = 1       -- 普通关卡（剧情）， stage_config
#TYPE_STAGE_ELITE = 2        -- 精英关卡， special_stage_config
#TYPE_STAGE_ACTIVITY = 3     -- 活动关卡， special_stage_config
#TYPE_TRAVEL         = 4     --travel

#TYPE_PVP            = 6     --pvp

#TYPE_WORLD_BOSS     = 7     --世界boss

#TYPE_MINE_MONSTER           = 8       -- 攻占也怪
#TYPE_MINE_OTHERUSER         = 9       -- 攻占其他玩家

#func = lua.eval('''function() return start(); end''')
#print(func())

pvp_func = lua.eval('''function(fightData, fightType, level) setData(fightData, fightType, level); return pvp_start(); end''')
pve_func = lua.eval('''function(fightData, fightType, steps, level) setData(fightData, fightType, level); return pve_start(steps); end''')

def construct_battle_unit(unit):
    """
    python to table
    """
    # 构造战斗单元
    if not unit:
        return None
    return lua.table(
        no = unit.unit_no,
        quality = unit.quality,

        hp = unit.hp,
        hp_max = unit.hp_max,
        atk = unit.atk,
        physical_def = unit.physical_def,
        magic_def = unit.magic_def,
        hit = unit.hit,
        dodge = unit.dodge,
        cri = unit.cri,
        cri_coeff = unit.cri_coeff,
        cri_ded_coeff = unit.cri_ded_coeff,
        block = unit.block,
        ductility = unit.ductility,

        level = unit.level,
        break_level = unit.break_level,

        is_boss = unit.is_boss,
        #break_skills = unit.break_skills,
        position = unit.position,

        is_break = unit.is_break,
        is_awake = unit.is_awake,
        origin_no = unit.origin_no
    )

def from_table_to_battle_unit(unit):
    """
    table to python
    """
    info = dict(
        unit_no = unit.no,
        quality = unit.quality,

        hp = unit.hp,
        hp_max = unit.hp_max,
        atk = unit.atk,
        physical_def = unit.physical_def,
        magic_def = unit.magic_def,
        hit = unit.hit,
        dodge = unit.dodge,
        cri = unit.cri,
        cri_coeff = unit.cri_coeff,
        cri_ded_coeff = unit.cri_ded_coeff,
        block = unit.block,
        ductility = unit.ductility,

        level = unit.level,
        break_level = unit.break_level,

        is_boss = unit.is_boss,
        #break_skills = unit.break_skills,
        position = unit.pos,

        is_break = unit.is_break,
        is_awake = unit.is_awake,
        origin_no = unit.origin_no
    )
    unit = BattleUnit()
    unit.set_attrs(**info)
    print("from table================")
    print(unit)
    return unit

def pvp_start(red_units, blue_units, red_skill, red_skill_level, blue_skill, blue_skill_level, seed1, seed2, level):
    red = []
    blue = []
    for unit in red_units.values():
        red.append(construct_battle_unit(unit))
    for unit in blue_units.values():
        blue.append(construct_battle_unit(unit))

    fight_data = lua.table(
        red = lua.table_from(red),
        blue = lua.table_from(blue),
        red_skill = red_skill,
        red_skill_level = red_skill_level,
        blue_skill = blue_skill,
        blue_skill_level = blue_skill_level,
        fight_result = False,
        seed1 = seed1,
        seed2 = seed2
    )
    fight_type = const.BATTLE_PVP
    res = pvp_func(fight_data, fight_type, level)
    print("pvp_start=====:", res)
    if int(res[0]) == 1:
        return True
    return False

def pve_start(red_units, blue_groups, red_skill, red_skill_level, blue_skill, blue_skill_level, f_unit, seed1, seed2, step_infos, level):
    red = []
    blue = []
    for unit in red_units.values():
        red.append(construct_battle_unit(unit))
    for units in blue_groups:
        temp = []
        for unit in units.values():
            temp.append(construct_battle_unit(unit))
        blue.append(lua.table(group=lua.table_from(temp)))

    temp = {}
    for step in step_infos:
        temp[step.step_id] = step.step_type
    print("pve_start steps %s" % temp)
    steps = lua.table_from(temp)

    fight_data = lua.table(
        red = lua.table_from(red),
        blue = lua.table_from(blue),
        hero_unpar = red_skill,
        hero_unpar_level = red_skill_level,
        monster_unpar = blue_skill,
        #blue_skill_level = blue_skill_level,
        friend = construct_battle_unit(f_unit),
        fight_result = False,
        seed1 = seed1,
        seed2 = seed2
    )
    fight_type = const.BATTLE_PVE
    res = pve_func(fight_data, fight_type, steps, level)
    if int(res) == 1:
        return True
    return False

def world_boss_start(red_units,  blue_units, red_skill, red_skill_level, blue_skill, blue_skill_level, debuff_skill_no, damage_rate, seed1, seed2, level):
    red = []
    blue = []
    for unit in red_units.values():
        red.append(construct_battle_unit(unit))
    for unit in blue_units.values():
        blue.append(construct_battle_unit(unit))

    fight_data = lua.table(
        red = lua.table_from(red),
        blue = lua.table_from(blue),
        red_best_skill = red_skill,
        red_best_skill_level = red_skill_level,
        blue_skill = blue_skill,
        blue_skill_level = blue_skill_level,
        seed1 = seed1,
        seed2 = seed2,
        debuff_skill_no = debuff_skill_no,
        damage_rate= damage_rate
    )
    fight_type = const.BATTLE_PVB
    res = pvp_func(fight_data, fight_type, level)
    print("world_boss_start=====:", res, level)
    if int(res[0]) == 1:
        return {"result":True, "hp_left":res[1]}
    return {"result":False, "hp_left":res[1]}

def hjqy_start(red_units,  blue_units, red_skill, red_skill_level, blue_skill, blue_skill_level, attack_type, seed1, seed2, level):
    red = []
    blue = []
    for unit in red_units.values():
        red.append(construct_battle_unit(unit))
    for unit in blue_units.values():
        blue.append(construct_battle_unit(unit))

    fight_data = lua.table(
        red = lua.table_from(red),
        blue = lua.table_from(blue),
        red_skill = red_skill,
        red_skill_level = red_skill_level,
        blue_skill = blue_skill,
        blue_skill_level = blue_skill_level,
        seed1 = seed1,
        seed2 = seed2,
        attack_type = attack_type
    )
    fight_type = const.BATTLE_HJQY
    res = pvp_func(fight_data, fight_type, level)
    print("hjqy_start=====:", res, level, blue_units.keys())
    for k, v in blue_units.items():
        if k not in res[2]:
            del blue_units[k]
        else:
            blue_units[k].hp = res[2][k].hp

    if int(res[0]) == 1:
        return True
    return False

def mine_pvp_start(red_units, blue_units, red_skill, red_skill_level, blue_skill, blue_skill_level, seed1, seed2, level):
    red = []
    blue = []
    for unit in red_units.values():
        red.append(construct_battle_unit(unit))
    for unit in blue_units.values():
        blue.append(construct_battle_unit(unit))

    fight_data = lua.table(
        red = lua.table_from(red),
        blue = lua.table_from(blue),
        red_best_skill_id = red_skill,
        red_best_skill_level = red_skill_level,
        blue_best_skill_id = blue_skill,
        blue_best_skill_level = blue_skill_level,
        seed1 = seed1,
        seed2 = seed2
    )
    fight_type = const.BATTLE_MINE_PVP
    res = pvp_func(fight_data, fight_type, level)
    print("pvp_start=====:", res)
    if int(res[0]) == 1:
        return True
    return False

def mine_start(red_units, blue_units, red_skill, red_skill_level, blue_skill, blue_skill_level, seed1, seed2, step_infos, level):
    red = []
    blue = []
    for unit in red_units.values():
        red.append(construct_battle_unit(unit))
    for unit in blue_units.values():
        blue.append(construct_battle_unit(unit))
    temp = {}
    for step in step_infos:
        temp[step.step_id] = step.step_type
    print("pve_start steps %s" % temp)
    steps = lua.table_from(temp)

    fight_data = lua.table(
        red = lua.table_from(red),
        blue = lua.table_from(blue),
        red_best_skill_id = red_skill,
        red_best_skill_level = red_skill_level,
        blue_best_skill_id = blue_skill,
        blue_best_skill_level = blue_skill_level,
        seed1 = seed1,
        seed2 = seed2
    )
    fight_type = const.BATTLE_MINE_PVE
    res = pvp_func(fight_data, fight_type)
    print("pvp_start=====:", res)
    res = pve_func(fight_data, fight_type, steps, level)
    if int(res) == 1:
        return True
    return False

def get_seeds():
    seed1 = randint(1, 100)
    seed2 = randint(1, 100)
    return seed1, seed2

