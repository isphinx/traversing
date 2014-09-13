# -*- coding:utf-8 -*-
"""
created by server on 14-7-7下午2:25.
"""
from app.game.core.PlayersManager import PlayersManager
from app.game.core.pack.item import Item
from app.game.redis_mode import tb_character_item_package


def init_item(player):
    # 突破丹
    item1 = Item(20001, 10)
    item2 = Item(20002, 20)
    item3 = Item(20003, 30)
    item4 = Item(20004, 40)
    item5 = Item(20005, 50)

    # 经验
    item6 = Item(10003, 15)
    item9 = Item(10002, 15)

    # box
    item7 = Item(30003, 15)
    # key
    item8 = Item(30013, 15)

    player.item_package.add_item(item1)
    player.item_package.add_item(item2)
    player.item_package.add_item(item3)
    player.item_package.add_item(item4)
    player.item_package.add_item(item5)
    player.item_package.add_item(item6)
    player.item_package.add_item(item9)
    # player.item_package.add_item(item7)
    # player.item_package.add_item(item8)