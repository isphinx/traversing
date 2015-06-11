# -*- coding:utf-8 -*-
"""
created by server on 14-8-29上午11:39.
"""
from app.game.component.Component import Component
from app.game.redis_mode import tb_character_info
import time
from shared.db_opear.configs_data import game_configs
from shared.utils.date_util import days_to_current, get_current_timestamp
from gfirefly.server.logobj import logger


class CharacterLoginGiftComponent(Component):
    """登录活动"""

    def __init__(self, owner):
        super(CharacterLoginGiftComponent, self).__init__(owner)
        self._continuous_day = {}    # 连续登录
        self._cumulative_day = {}    # 累积登录
        self._continuous_day_num = 0 # 连续登录天数
        self.new_item()
        self._last_login = int(time.time())  # 日期

    def init_data(self, character_info):
        data = character_info.get('login_gift')
        self._continuous_day = data.get('continuous_day', {})
        self._continuous_day_num = data.get('continuous_day_num', 0)
        self._cumulative_day = data.get('cumulative_day', {})
        self._last_login= data.get('last_login')
        self.check_time()

    def new_item(self):
        """docstring for new_item"""
        activity_infos = game_configs.activity_config.get(1)
        for info in activity_infos:
            self._continuous_day[info.id] = -1

        activity_infos = game_configs.activity_config.get(2)
        for info in activity_infos:
            self._cumulative_day[info.id] = -1

        self._continuous_day[2001] = 0
        self._cumulative_day[1001] = 0

    def check_time(self):
        """docstring for check_time"""
        if days_to_current(self._last_login) > 1:
            self._continuous_day = [0] + [-1] * 6
        elif days_to_current(self._last_login) == 1:
            for k, v in enumerate(self._continuous_day):
                if v == -1 or k == 7:
                    self._continuous_day[k] = 0
                    break

        if days_to_current(self._last_login) > 0:
            self._cumulative_day.append(-1)
            for k, v in enumerate(self._cumulative_day):
                if v == -1:
                    self._cumulative_day[k] = 0
                    break

        self._last_login = get_current_timestamp()

    def save_data(self):
        sign_in_data = tb_character_info.getObj(self.owner.base_info.id)
        sign_in_data.hset('login_gift', {
            'cumulative_day': self._cumulative_day,
            'continuous_day': self._continuous_day,
            'continuous_day_num': self._continuous_day_num,
            'last_login': self._last_login})

    def new_data(self):
        return {'login_gift': {'last_login': self._last_login,
                               'continuous_day': self._continuous_day,
                               'continuous_day_num': self._continuous_day_num,
                               'cumulative_day': self._cumulative_day}}

    @property
    def continuous_day(self):
        return self._continuous_day

    @continuous_day.setter
    def continuous_day(self, value):
        self._continuous_day = value

    @property
    def cumulative_day(self):
        return self._cumulative_day

    @cumulative_day.setter
    def cumulative_day(self, value):
        self._cumulative_day = value

    @property
    def cumulative_day_num(self):
        for k, v in self._cumulative_day:
            if v == -1:
                return k
        return 8

    @property
    def continuous_day_num(self):
        return self._continuous_day_num

    @continuous_day_num.setter
    def continuous_day_num(self, value):
        self._continuous_day_num = value

    def is_open(self, activity_id):
        """
        check if it opened.
        """
        activity_info = game_configs.activity_config.get(activity_id)
        if not activity_info:
            logger.error("can not find activity_config by id %s" % activity_id)
            return False
        if activity_info.type == 1:
            res = False
            for item in self._cumulative_day:
                if not item:
                    res = True
            if not res and len(self._cumulative_day) == 7:
                return False

        if not self._owner.is_activiy_open(activity_id):
            return False
        return True

