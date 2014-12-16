#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created by wzp.
"""
from shared.db_opear.configs_data.game_configs import special_stage_config, hero_config, monster_group_config, monster_config
from gfirefly.dbentrust.redis_client import redis_client
import random
from shared.utils.random_pick import random_pick_with_percent
import cPickle
from shared.utils.date_util import str_time_period_to_timestamp, get_current_timestamp
from gfirefly.server.logobj import logger

class BaseBoss(object):
    """docstring for Boss 基类"""
    def __init__(self, boss_name, rank_instance, config_name):
        self._boss_name = boss_name   # boss 名称：对应redis key
        self._lucky_high_heros = []   # 高级幸运武将
        self._lucky_middle_heros = [] # 中级幸运武将
        self._lucky_low_heros = []    # 低级幸运武将
        self._debuff_skill_no = 0     # debuff id
        self._last_shot_item = {}     # 最后击杀
        self._stage_id = 0            # 关卡id
        self._hp = 0                  # 剩余血量
        self._boss_dead_time = 0      # boss被打死的时间

        self._rank_instance = rank_instance # 排名
        self._config_name = config_name # worldboss:boss_stages, mineboss:mine_boss_stages


    def init_base_data(self, boss_data):
        """docstring for init_base_data"""
        self._lucky_high_heros = boss_data.get("lucky_high_heros")
        self._lucky_middle_heros = boss_data.get("lucky_middle_heros")
        self._lucky_low_heros = boss_data.get("lucky_low_heros")

        self._debuff_skill_no = boss_data.get("debuff_skill_no")
        self._last_shot_item = boss_data.get("last_shot_item")
        self._stage_id = boss_data.get("stage_id")
        self._boss_dead_time = boss_data.get("boss_dead_time")
        self._hp = boss_data.get("hp")

    @property
    def stage_id(self):
        return self._stage_id

    @stage_id.setter
    def stage_id(self, value):
        self._stage_id = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    def get_data_dict(self):
        return dict(hp=self._hp,
                lucky_high_heros=self._lucky_high_heros,
                lucky_middle_heros=self._lucky_middle_heros,
                lucky_low_heros=self._lucky_low_heros,
                debuff_skill_no=self._debuff_skill_no,
                last_shot_item=self._last_shot_item,
                stage_id=self._stage_id,
                boss_dead_time=self._boss_dead_time
                )

    @property
    def debuff_skill_no(self):
        return self._debuff_skill_no

    @property
    def last_shot_item(self):
        return self._last_shot_item

    @last_shot_item.setter
    def last_shot_item(self, value):
        self._last_shot_item = value

    @property
    def lucky_high_heros(self):
        return self._lucky_high_heros

    @property
    def lucky_middle_heros(self):
        return self._lucky_middle_heros

    @property
    def lucky_low_heros(self):
        return self._lucky_low_heros

    @property
    def boss_dead_time(self):
        return self._boss_dead_time

    @boss_dead_time.setter
    def boss_dead_time(self, value):
        self._boss_dead_time = value

    @property
    def open_or_not(self):
        return self.in_the_time_period()

    def start_boss(self):
        self._rank_instance.clear_rank() # 重置排行
        self._last_shot_item = {} # 重置最后击杀

    def update_base_boss(self, base_config_info):
        """
        boss被打死或者boss到期后，更新下一个boss相关信息。
        """
        # 初始化幸运武将
        lucky_hero_1_num = base_config_info.get("lucky_hero_1_num")
        lucky_hero_2_num = base_config_info.get("lucky_hero_2_num")
        lucky_hero_3_num = base_config_info.get("lucky_hero_3_num")
        all_high_heros, all_middle_heros, all_low_heros = self.get_hero_category()
        self._lucky_high_heros =  random.sample(all_high_heros, lucky_hero_1_num)

        for k in self._lucky_high_heros: # 去重
            all_middle_heros.remove(k)
        self._lucky_middle_heros =  random.sample(all_middle_heros, lucky_hero_2_num)

        for k in self._lucky_middle_heros: # 去重
            all_low_heros.remove(k)
        self._lucky_low_heros =  random.sample(all_low_heros, lucky_hero_3_num)

        # 初始化奇遇
        debuff_skill = base_config_info.get("debuff_skill")
        self._debuff_skill_no = random_pick_with_percent(debuff_skill)

        self.set_next_stage(self._hp<=0)
        self._hp = self.get_hp() # 重置血量

        #todo: 重置玩家信息

        # todo:对前十名发放奖励


    def in_the_time_period(self):
        stage_info = self.current_stage_info()
        time_start, time_end = str_time_period_to_timestamp(stage_info.timeControl)
        current = get_current_timestamp()
        if self._boss_dead_time > time_start:
            return time_start<=current and self._boss_dead_time>=current
        return time_start<=current and time_end>=current

    def get_hero_category(self):
        """docstring for get_hero_category"""
        all_high_heros = []
        all_middle_heros = []
        all_low_heros = []
        for k, v in hero_config.items():
            if v.quality in [5, 6]:
                all_high_heros.append(k)
            if v.quality in [3, 4, 5, 6]:
                all_middle_heros.append(k)
            if v.quality in [2, 3, 4, 5, 6]:
                all_low_heros.append(k)
        return all_high_heros, all_middle_heros, all_low_heros

    def set_next_stage(self, kill_or_not=False):
        """
        根据id规则确定下一个关卡
        如果boss未被击杀则不升级
        """
        logger.debug("current_stage_id1%s" % self._stage_id)
        current_stage_id = self._stage_id
        if current_stage_id == 0:
            self._stage_id_am = 800101
            self._stage_id_pm = 800102
            self._stage_id = 800101
            return
        if kill_or_not: #如果boss被击杀，则升级boss
            if current_stage_id == self._stage_id_am: # am
                self._stage_id_am = current_stage_id + 100
            else: # pm
                self._stage_id_pm = current_stage_id + 100

        if current_stage_id == self._stage_id_am:
            self._stage_id = self._stage_id_pm
        else:
            self._stage_id = self._stage_id_am


        logger.debug("current_stage_id3%s" % self._stage_id)
        logger.debug("current_stage_id_am%s" % self._stage_id_am)
        logger.debug("current_stage_id_pm%s" % self._stage_id_pm)


    def add_rank_item(self, player_info):
        """
        每次战斗结束, 添加排名
        """
        player_id = player_info.get("player_id")

        instance = self._rank_instance
        instance.incr_value(player_id, player_info.get("demage_hp"))

        # 如果玩家信息在前十名，保存玩家信息到redis
        rank_no = instance.get_rank_no(player_id)
        if rank_no > 10: return
        str_player_info = cPickle.dumps(player_info)
        redis_client.set(player_id, str_player_info)

    def get_rank_items(self):
        """
        返回伤害最大前十名
        """
        instance = self._rank_instance
        rank_items = []
        for player_id, demage_hp in instance.get(1, 10):
            player_info = cPickle.loads(redis_client.get(player_id))

            player_info["demage_hp"] = demage_hp
            rank_items.append(player_info)

        return rank_items

    def get_rank_item_by_rankno(self, no):
        """
        rank no
        """
        player_id = self._rank_instance.get(no, no)[0][0]
        player_info = cPickle.loads(redis_client.get(player_id))
        return player_info

    def get_demage_hp(self, player_id):
        demage_hp = self._rank_instance.get_value(player_id)
        return demage_hp

    def get_rank_no(self, player_id):
        rank_no = self._rank_instance.get_rank_no(player_id)
        return rank_no

    def current_stage_info(self):
        return special_stage_config.get(self._config_name).get(self._stage_id)

    def get_stage_info(self, stage_id):
        return special_stage_config.get(self._config_name).get(stage_id)

    def get_hp(self):
        stage_info = self.current_stage_info()
        logger.info("stage info %s id:%s" % (stage_info, self._stage_id))
        monster_group_info = monster_group_config.get(stage_info.round1)
        monster_info = monster_config.get(monster_group_info.pos5)
        return monster_info.hp
