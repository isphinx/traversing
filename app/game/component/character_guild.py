# -*- coding:utf-8 -*-
"""
created by server on 14-7-24下午6:32.
"""
from app.game.component.Component import Component
from app.game.redis_mode import tb_guild_info
from shared.db_opear.configs_data import game_configs
from app.game.redis_mode import tb_character_info
from app.game.core.guild import Guild


class CharacterGuildComponent(Component):
    """
    公会组件类
    """

    def __init__(self, owner):
        super(CharacterGuildComponent, self).__init__(owner)
        self._g_id = 0  # 公会id
        self._position = 5  # 职务
        self._contribution = 0  # 贡献
        self._all_contribution = 0  # 总贡献
        # self._k_num = 0  # 杀人数
        # self._worship = 0  # 膜拜次数
        # self._worship_time = 1  # 最后膜拜时间
        self._exit_time = 1  # 上次退出公会时间
        self._praise = [0, 1]  # 点赞状态（0没点，1点），时间
        self._bless = [0, 1]  # 祈福人数,时间
        self._apply_guilds = []  # 已经申请过的军团

    def init_data(self, character_info):
        """
        初始化公会组件
        """
        self._g_id = character_info.get("guild_id")
        self._position = character_info.get("position")
        self._contribution = character_info.get("contribution")
        self._all_contribution = character_info.get("all_contribution")
        # self._k_num = character_info.get("k_num")
        # self._worship = character_info.get("worship")
        # self._worship_time = character_info.get("worship_time")
        self._bless = character_info.get('bless')
        self._praise = character_info.get('praise')
        self._exit_time = character_info.get("exit_time")

    def save_data(self):
        data_obj = tb_character_info.getObj(self.owner.base_info.id)
        data_obj.hmset({'guild_id': self._g_id,
                        'position': self._position,
                        'contribution': self._contribution,
                        'all_contribution': self._all_contribution,
                        'bless': self._bless,
                        'praise': self._praise,
                        # 'k_num': self._k_num,
                        # 'worship': self._worship,
                        # 'worship_time': self._worship_time,
                        'exit_time': self._exit_time})

    def new_data(self):
        data = {'guild_id': self._g_id,
                'position': self._position,
                'contribution': self._contribution,
                'all_contribution': self._all_contribution,
                'bless': self._bless,
                'praise': self._praise,
                # 'k_num': self._k_num,
                # 'worship': self._worship,
                # 'worship_time': self._worship_time,
                'exit_time': self._exit_time}
        return data

    def get_guild_level(self):
        if self._g_id == "no":
            return 0
        data = tb_guild_info.getObj(self._g_id).hgetall()
        if not data:
            return 0
        guild_obj = Guild()
        guild_obj.init_data(data)
        return guild_obj.level

    @property
    def praise(self):
        return self._praise

    @praise.setter
    def praise(self, value):
        self._praise = value

    @property
    def bless(self):
        return self._bless

    @bless.setter
    def bless(self, value):
        self._bless = value

    @property
    def g_id(self):
        return self._g_id

    @g_id.setter
    def g_id(self, g_id):
        self._g_id = g_id

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def exit_time(self):
        return self._exit_time

    @exit_time.setter
    def exit_time(self, exit_time):
        self._exit_time = exit_time

    # @property
    # def worship(self):
    #     return self._worship

    # @worship.setter
    # def worship(self, worship):
    #     self._worship = worship

    # @property
    # def worship_time(self):
    #     return self._worship_time

    # @worship_time.setter
    # def worship_time(self, worship_time):
    #     self._worship_time = worship_time

    @property
    def contribution(self):
        return self._contribution

    @contribution.setter
    def contribution(self, contribution):
        self._contribution = contribution

    @property
    def all_contribution(self):
        return self._all_contribution

    @all_contribution.setter
    def all_contribution(self, all_contribution):
        self._all_contribution = all_contribution

    def guild_attr(self):
        guild_level = self.get_guild_level()
        guild_info = game_configs.guild_config.get(guild_level)
        if not guild_info:
            return {}

        return dict(hp=guild_info.profit_hp,
                    atk=guild_info.profit_atk,
                    physical_def=guild_info.profit_pdef,
                    magic_def=guild_info.profit_mdef)

    @property
    def contribution(self):
        return self._contribution

    @contribution.setter
    def contribution(self, contribution):
        self._contribution = contribution
