# -*- coding:utf-8 -*-
"""
created by server on 14-8-14下午3:48.
"""
from shared.db_opear.configs_data.game_configs import base_config
from app.game.component.Component import Component
from app.game.redis_mode import tb_character_info
from gfirefly.server.logobj import logger
from app.proto_file.db_pb2 import Mail_PB
from shared.utils.pyuuid import get_uuid


class CharacterMailComponent(Component):
    """角色邮件列表组件"""

    def __init__(self, owner):
        """
        @param owner: 当前玩家
        """
        super(CharacterMailComponent, self).__init__(owner)
        self._mails = {}

    def init_data(self, c):
        pid = self.owner.base_info.id
        char_obj = tb_character_info.getObj(pid).getObj('mails')
        mails = char_obj.hgetall()
        for mid, mail_data in mails.items():
            mail = Mail_PB()
            mail.ParseFromString(mail_data)
            self._mails[mail.mail_id] = mail

    def new_data(self):
        return {}

    def save_data(self):
        return

    def _new_mail_data(self, mail):
        character_id = self.owner.base_info.id

        char_obj = tb_character_info.getObj(character_id).getObj('mails')
        result = char_obj.hsetnx(mail.mail_id, mail.SerializePartialToString())
        if not result:
            logger.error('add mail error!:%s', mail.mail_id)

    def add_exist_mail(self, mail):
        self._mails[mail.mail_id] = mail
        self._new_mail_data(mail)
        self.save_data()

    def add_mail(self, mail):
        """添加邮件"""
        if mail.mail_type == 1:  # 领取体力邮件不能超过15个
            mails = self.get_mails_by_type(1)
            if len(mails) >= base_config['times_save_vigor']:
                return

        mail.mail_id = get_uuid()
        mail.receive_id = self.owner.base_info.id

        self._mails[mail.mail_id] = mail
        self._new_mail_data(mail)

    def get_mails(self):
        """获取角色邮件列表
        """
        return self._mails.values()

    def get_mails_by_type(self, mail_type):
        """根据邮件类型获取邮件"""
        return [mail for mail in self._mails.values() if mail.mail_type == mail_type]

    def get_mail(self, mail_id):
        return self._mails.get(mail_id)

    def delete_mail(self, mail_id):
        if mail_id not in self._mails:
            return
        mail = self._mails[mail_id]
        mail.delete()
        del self._mails[mail_id]

    def delete_mails(self, mail_ids):
        """批量删除"""
        for mail_id in mail_ids:
            self.delete_mail(mail_id)
