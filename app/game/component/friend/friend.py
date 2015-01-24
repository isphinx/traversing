# -*- coding:utf-8 -*-
"""
created by server on 14-7-17下午5:21.
"""

import datetime
import time

from app.game.action.root import netforwarding
from app.game.component.Component import Component
from app.game.redis_mode import tb_character_info
from gfirefly.server.logobj import logger
from shared.db_opear.configs_data.game_configs import mail_config
from app.proto_file.db_pb2 import Mail_PB


class FriendComponent(Component):
    def __init__(self, owner):
        super(FriendComponent, self).__init__(owner)
        self._friends = {}
        self._blacklist = []
        self._applicants_list = {}

    def init_data(self, character_info):
        self._friends = character_info.get('friends')
        self._blacklist = character_info.get('blacklist')
        self._applicants_list = character_info.get('applicants_list')

    def save_data(self):
        friend_obj = tb_character_info.getObj(self.owner.base_info.id)
        data = dict(friends=self._friends,
                    blacklist=self._blacklist,
                    applicants_list=self._applicants_list)
        friend_obj.hmset(data)

    def new_data(self):
        data = dict(friends=self._friends,
                    blacklist=self._blacklist,
                    applicants_list=self._applicants_list)
        return data

    @property
    def friends(self):
        date_now = datetime.datetime.now().date()
        for k in self._friends.keys():
            self._friends[k] = filter(lambda t: t.date() == date_now,
                                      self._friends[k])

        return self._friends.keys()

    @property
    def blacklist(self):
        return self._blacklist

    @property
    def applicant_list(self):
        for k, v in self._applicants_list.items():
            period = datetime.datetime.now() - v
            if period.days > 2:
                del (self._applicants_list[k])

        return self._applicants_list.keys()

    def is_friend(self, friend_id):
        if friend_id in self._friends.keys():
            return True
        return False

    def is_in_blacklist(self, target_id):
        if target_id in self._blacklist:
            return True
        return False

    def is_in_applicants_list(self, target_id):
        if target_id in self.applicant_list:
            return True
        return False

    def add_friend(self, friend_id, is_active=True):
        if friend_id in self._friends.keys():
            if friend_id in self._applicants_list:
                del(self._applicants_list[friend_id])
            return False

        if friend_id in self._blacklist:
            if friend_id in self._applicants_list:
                del(self._applicants_list[friend_id])
            return False

        if is_active:
            if friend_id not in self._applicants_list:
                return False

        if friend_id in self._applicants_list:
            del(self._applicants_list[friend_id])

        self._friends[friend_id] = []
        return True

    def del_friend(self, friend_id):
        if friend_id not in self._friends.keys():
            return False

        del self._friends[friend_id]
        return True

    def add_blacklist(self, target_id):
        if target_id in self._blacklist:
            return False

        if target_id in self._friends.keys():
            return False

        self._blacklist.append(target_id)
        return True

    def del_blacklist(self, target_id):
        if target_id not in self._blacklist:
            return False

        self._blacklist.remove(target_id)
        return True

    def add_applicant(self, target_id):
        if target_id in self._applicants_list.keys():
            return False

        if target_id in self._friends.keys():
            return False

        if target_id in self._blacklist:
            return False

        self._applicants_list[target_id] = datetime.datetime.now()
        return True

    def del_applicant(self, target_id):
        if target_id not in self._applicants_list:
            return False

        del (self._applicants_list[target_id])
        return True

    def last_present_times(self, target_id):
        given_time_list = self._friends.get(target_id)
        if given_time_list is None:
            return 0
        given_times = len(given_time_list)
        return max(1 - given_times, 0)

    def given_stamina(self, target_id, if_present=True):
        if target_id not in self._friends.keys():
            return False

        given_time_list = self._friends[target_id]
        given_times = len(given_time_list)
        if given_times >= 1:
            return False

        given_time_list.append(datetime.datetime.now())
        if not if_present:
            return True

        stamina_mail = mail_config.get(1)
        if stamina_mail:
            mail = Mail_PB()
            mail.sender_id = self.owner.base_info.id
            mail.sender_name = self.owner.base_info.base_name
            mail.sender_icon = self.owner.line_up_component.lead_hero_no
            mail.receive_id = target_id
            mail.title = stamina_mail.get('title')
            mail.content = stamina_mail.get('content')
            mail.mail_type = stamina_mail.get('type')
            mail.send_time = int(time.time())
            mail.prize = str(stamina_mail.get('rewards'))

            # command:id 为收邮件的命令ID
            mail_data = mail.SerializePartialToString()
            if netforwarding.push_message('receive_mail_remote', target_id, mail_data):
                return True
            else:
                logger.error('stamina mail push message fail')
        else:
            logger.error('can not find stamina mail!!!')

        return False
