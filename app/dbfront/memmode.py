# -*-coding:utf8-*-

from gfirefly.dbentrust.mmode import MAdmin

tb_account = MAdmin('tb_account', 'id')  # 甯���疯〃
tb_account.insert()

# ��ㄦ�蜂俊���琛�
tb_character_info = MAdmin('tb_character_info', 'id')
tb_character_info.insert()

# ��ㄦ�烽����疯�����
tb_character_item_package = MAdmin('tb_character_item_package', 'id')
tb_character_item_package.insert()

# ��ㄦ�烽�靛�逛俊���
tb_character_line_up = MAdmin('tb_character_line_up', 'id')
tb_character_line_up.insert()

# ���浼�淇℃��琛�
tb_guild_info = MAdmin('tb_guild_info', 'id')
tb_guild_info.insert()

# ���浼����琛�
tb_guild_name = MAdmin('tb_guild_name', 'id')
tb_guild_name.insert()

# ��冲�′俊���琛�
tb_character_stages = MAdmin('tb_character_stages', 'id')
tb_character_stages.insert()

# 活跃度
tb_character_tasks = MAdmin('tb_character_lively', 'id')
tb_character_tasks.insert()
