# -*- coding:utf-8 -*-
"""
created by server on 14-7-4上午10:30.
"""
from shared.utils.const import const


def init_player(player):
    player.finance[const.COIN] = 10000000
    player.finance[const.HERO_SOUL] = 10000000
    player.finance[const.EQUIPMENT_ELITE] = 10000000
    player.finance[const.PVP] = 10000000
    player.finance.save_data()

    player.level.level = 60
    player.level.exp = 0
    player.vip_component.vip_level = 10
    player.line_up_component.update_slot_activation()
    player.last_pick_time.fine_hero = 0
    player.last_pick_time.excellent_hero = 0
    player.last_pick_time.fine_equipment = 0
    player.last_pick_time.excellent_equipment = 0
    player.last_pick_time.save_data()
    player.save_data()
