# -*- coding:utf-8 -*-
"""
created by server on 15-5-29下午5:21.
"""
import time
import random
from shared.utils.const import const
from gfirefly.server.logobj import logger
from app.game.component.Component import Component
from app.game.redis_mode import tb_character_info
from shared.db_opear.configs_data import game_configs
from app.game.redis_mode import tb_pvp_rank
from app.game.core import rank_helper
from gfirefly.dbentrust.redis_mode import RedisObject
tb_rank = RedisObject('tb_rank')

tb_robot2 = tb_character_info.getObj('robot2')
robot2_rank = {}
for robot_id in tb_robot2.hkeys():
    robot_data = tb_robot2.hget(robot_id)
    robot2_rank[int(robot_id)] = robot_data.get('attackPoint')

robot2_rank = sorted(robot2_rank.items(), key=lambda _: _[1])
# for _ in robot2_rank:
#     print _


class CharacterPvpComponent(Component):
    def __init__(self, owner):
        """
        Constructor
        """
        Component.__init__(self, owner)
        self._pvp_overcome = []
        self._pvp_overcome_current = 1
        self._pvp_overcome_refresh_time = time.time()
        self._pvp_overcome_refresh_count = 0

        self._pvp_times = 0  # pvp次数
        self._pvp_refresh_time = 0
        self._pvp_refresh_count = 0
        self._pvp_current_rank = 0
        self._pvp_high_rank = 999999  # 玩家pvp最高排名
        self._pvp_high_rank_award = []  # 已经领取的玩家pvp排名奖励
        self._pvp_arena_players = []

    def init_data(self, character_info):
        self._pvp_overcome = character_info['pvp_overcome']
        self._pvp_overcome_current = character_info['pvp_overcome_current']
        self._pvp_overcome_refresh_time = character_info['pvp_overcome_refresh_time']
        self._pvp_overcome_refresh_count = character_info['pvp_overcome_refresh_count']

        self._pvp_times = character_info['pvp_times']
        self._pvp_refresh_time = character_info['pvp_refresh_time']
        self._pvp_refresh_count = character_info['pvp_refresh_count']

        self._pvp_high_rank = character_info['pvp_high_rank']
        self._pvp_current_rank = character_info['pvp_current_rank']
        self._pvp_high_rank_award = character_info['pvp_high_rank_award']

        self._pvp_arena_players = character_info.get('pvp_arena_players', [])

        self.check_time()

        self.save_data()

    def save_data(self):
        character_info = tb_character_info.getObj(self.owner.base_info.id)

        data = dict(pvp_overcome=self._pvp_overcome,
                    pvp_overcome_current=self._pvp_overcome_current,
                    pvp_overcome_refresh_time=self._pvp_overcome_refresh_time,
                    pvp_overcome_refresh_count=self._pvp_overcome_refresh_count,
                    pvp_high_rank=self._pvp_high_rank,
                    pvp_current_rank=self._pvp_current_rank,
                    pvp_high_rank_award=self._pvp_high_rank_award,
                    pvp_times=self._pvp_times,
                    pvp_refresh_time=self._pvp_refresh_time,
                    pvp_refresh_count=self._pvp_refresh_count,
                    pvp_arena_players=self._pvp_arena_players)
        character_info.hmset(data)

    def new_data(self):
        data = dict(pvp_overcome=self._pvp_overcome,
                    pvp_overcome_current=self._pvp_overcome_current,
                    pvp_overcome_refresh_time=self.pvp_overcome_refresh_time,
                    pvp_overcome_refresh_count=self.pvp_overcome_refresh_count,
                    pvp_high_rank=self._pvp_high_rank,
                    pvp_current_rank=self._pvp_current_rank,
                    pvp_high_rank_award=self._pvp_high_rank_award,
                    pvp_times=self._pvp_times,
                    pvp_refresh_time=self._pvp_refresh_time,
                    pvp_refresh_count=self._pvp_refresh_count,
                    pvp_arena_players=self._pvp_arena_players)
        return data

    def check_time(self):
        tm = time.localtime(self._pvp_refresh_time)
        local_tm = time.localtime()
        if local_tm.tm_year != tm.tm_year or local_tm.tm_yday != tm.tm_yday:
            self._pvp_times = game_configs.base_config.get('arena_free_times')
            self._pvp_refresh_count = 0
            self._pvp_refresh_time = time.time()
            self.save_data()

        tm = time.localtime(self._pvp_overcome_refresh_time)
        if local_tm.tm_year != tm.tm_year or local_tm.tm_yday != tm.tm_yday:
            if not self._pvp_overcome:
                self.reset_overcome()
            self._pvp_overcome_refresh_time = time.time()
            self._pvp_overcome_refresh_count = 0
            # self._pvp_overcome_current = 1
            self.save_data()

    def reset_overcome(self):
        _times = self.pvp_overcome_refresh_count + 1
        if _times > self.owner.base_info.buyGgzj_times:
            logger.error('overcome reset times error:%s-%s',
                         self.pvp_overcome_refresh_count,
                         self.owner.base_info.buyGgzj_times)
            return False

        character_info = tb_character_info.getObj(self.owner.base_info.id)
        ids = get_overcomes(self.owner.base_info.id,
                            int(character_info.hget('attackPoint')))
        if not ids:
            return False
        logger.debug('reset overcome:%s', ids)
        self._pvp_overcome = ids
        self._pvp_overcome_refresh_time = time.time()
        self._pvp_overcome_refresh_count += 1
        self._pvp_overcome_current = 1
        self.save_data()
        return True

    def get_overcome_id(self, index):
        if index > len(self._pvp_overcome):
            return 0

        return self._pvp_overcome[index]

    def pvp_player_rank_refresh(self):
        rank = tb_pvp_rank.zscore(self.owner.base_info.id)
        rank_max = int(tb_pvp_rank.ztotal())
        if not rank or rank_max == rank:
            rank = rank_max
            self._pvp_arena_players = range(rank-9, rank + 1)
            return

        if self._pvp_current_rank == rank:
            return
        self._pvp_current_rank = rank

        if rank < 9:
            self._pvp_arena_players = range(1, 11)
            return

        self._pvp_arena_players = [rank]
        for v in game_configs.arena_fight_config.values():
            if v.get('type') != 1:
                continue
            play_rank = v.get('play_rank')
            if rank in range(play_rank[0], play_rank[1] + 1):
                para = dict(k=rank)
                choose_fields = eval(v.get('choose'), para)
                logger.info('cur:%s choose:%s', rank, choose_fields)
                for x, y, c in choose_fields:
                    _min = int(x)
                    _max = min(int(y), rank_max)
                    range_nums = range(_min, _max+1)
                    if not range_nums:
                        logger.error('pvp rank range error:min:%s max:%s, rank_max:%s',
                                     _min, _max, rank_max)
                        continue
                    for _ in range(c):
                        r = random.choice(range_nums)
                        range_nums.remove(r)
                        self._pvp_arena_players.append(r)
                break
                logger.info('pvp rank refresh:%s', self._pvp_arena_players)

    @property
    def pvp_overcome(self):
        return self._pvp_overcome

    @pvp_overcome.setter
    def pvp_overcome(self, value):
        self._pvp_overcome = value

    @property
    def pvp_overcome_current(self):
        return self._pvp_overcome_current

    @pvp_overcome_current.setter
    def pvp_overcome_current(self, value):
        self._pvp_overcome_current = value

    @property
    def pvp_times(self):
        return self._pvp_times

    @pvp_times.setter
    def pvp_times(self, value):
        self._pvp_times = value

    @property
    def pvp_refresh_time(self):
        return self._pvp_refresh_time

    @pvp_refresh_time.setter
    def pvp_refresh_time(self, value):
        self._pvp_refresh_time = value

    @property
    def pvp_refresh_count(self):
        return self._pvp_refresh_count

    @pvp_refresh_count.setter
    def pvp_refresh_count(self, value):
        self._pvp_refresh_count = value

    @property
    def pvp_high_rank(self):
        return self._pvp_high_rank

    @pvp_high_rank.setter
    def pvp_high_rank(self, value):
        self._pvp_high_rank = value

    @property
    def pvp_high_rank_award(self):
        return self._pvp_high_rank_award

    @pvp_high_rank_award.setter
    def pvp_high_rank_award(self, value):
        self._pvp_high_rank_award = value

    @property
    def pvp_overcome_refresh_time(self):
        return self._pvp_overcome_refresh_time

    # @pvp_overcome_refresh_time.setter
    # def pvp_overcome_refresh_time(self, value):
    #     self._pvp_overcome_refresh_time = value

    @property
    def pvp_overcome_refresh_count(self):
        return self._pvp_overcome_refresh_count

    # @pvp_overcome_refresh_count.setter
    # def pvp_overcome_refresh_count(self, value):
    #     self._pvp_overcome_refresh_count = value

    @property
    def pvp_arena_players(self):
        self.pvp_player_rank_refresh()
        self.save_data()
        return self._pvp_arena_players


def get_overcomes(player_id, player_ap):
    rank_name, _ = rank_helper.get_power_rank_name()
    rank = tb_rank.getObj(rank_name)
    rank_toal = rank.ztotal()
    if rank_toal < 20:
        if len(robot2_rank) < 20:
            logger.error('not robot2 exist')
            return []
        robot_ids = set([(0, 0)])
        index = 0
        for i in range(len(robot2_rank)):
            rid, rap = robot2_rank[i]
            if rap > player_ap:
                index = i
                break
        else:
            index = len(robot2_rank)

        _min = max(index - 20, 0)
        _max = min(index + 20, len(robot2_rank) - 1)
        while len(robot_ids) != 16:
            _id = random.randint(_min, _max)
            robot_ids.add(robot2_rank[_id])
        robot_ids = sorted(list(robot_ids), key=lambda x: x[1])
        robot_ids = dict(robot_ids).keys()
        logger.error('reset overcome not enough player:%s(%s)',
                     robot_ids, index)
        return robot_ids
    types = [20001, 20002, 20003]
    count = 0
    ids = set()
    for _id in types:
        item = game_configs.arena_fight_config.get(_id)
        if not item:
            logger.error('arena_fight_config:%d', _id)
        scope = eval(item.choose, dict(k=player_ap))[0]
        count += scope[2]
        _min, _max = scope[0], scope[1]
        _min *= const.power_rank_xs
        _max *= const.power_rank_xs
        increment = player_ap * 20 / 100 * const.power_rank_xs
        index = 1
        while len(ids) < count:
            res = rank.zrangebyscore(_min - increment * (index - 1),
                                     _max + increment * (index - 1),
                                     withscores=True)
            index += index
            random.shuffle(res)
            if len(res) > count:
                res = filter(lambda x: int(x[0]) != player_id, res)
                ids_index = 0
                while len(ids) < count:
                    ids.add(res[ids_index])
                    ids_index += 1

    overcome_ids = [0]
    ids = sorted(ids, key=lambda x: x[1])
    for _id, _ in ids:
        overcome_ids.append(int(_id))
    logger.debug('get overcome %s-%s', overcome_ids, len(overcome_ids))
    return overcome_ids


def arraged_ids(ids_set):
    overcome_ids = [0]
    ids = sorted(ids_set, key=lambda x: x[1])
    for _id, _ in ids:
        overcome_ids.append(int(_id))
    logger.debug('get overcome %s-%s', overcome_ids, len(overcome_ids))
    return overcome_ids


def get_overcomes_by_score(rank, player_id, player_ap):
    ids = set()
    for item in game_configs.arena_fight_config.values():
        if item.type != 2:
            continue
        scope = eval(item.choose, dict(k=player_ap))[0]
        _min, _max, count = scope
        _min *= const.power_rank_xs
        _max *= const.power_rank_xs
        res = rank.zrangebyscore(_min, _max, withscores=True)
        if len(res) < count:
            break
        random.shuffle(res)
        res = filter(lambda x: int(x[0]) != player_id, res)
        ids.add(res[_] for _ in range(count))
        print _min, _max, ids

    return arraged_ids(ids)


def get_overcomes_by_rank(rank, player_id, player_ap):
    ids = set()
    player_rank = rank.zrank(player_id)
    if not player_rank:
        logger.error('player no rank from pvpovercom:%s', player_id)
        return []
    for item in game_configs.arena_fight_config.values():
        if item.type != 3:
            continue
        if player_rank not in range(item.choose[0], item.choose[0] + 1):
            continue
        scope = eval(item.choose, dict(k=player_rank))[0]
        _min, _max, count = scope
        res = rank.zrangebyscore(_min, _max, withscores=True)
        if len(res) < count:
            break
        random.shuffle(res)
        res = filter(lambda x: int(x[0]) != player_id, res)
        ids.add(res[_] for _ in range(count))
        print _min, _max, ids

    return arraged_ids(ids)


# get_overcomes(10008, 256)
