# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/config/tieba_config.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1
#

# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

# Tieba platform configuration

# Specify Tieba ID list
TIEBA_SPECIFIED_ID_LIST = []

# Specify a list of Tieba names
# 填贴吧名称（不含"吧"字），与 tieba.baidu.com/f?kw=xxx 中的 kw 一致
TIEBA_NAME_LIST = [
    "外卖",      # 外卖吧
    "美团骑手",  # 美团骑手吧
    "饿了么骑手",  # 饿了么骑手吧
    "美团众包",  # 美团众包吧
    "美团",      # 美团吧
]

# Specify Tieba user URL list
TIEBA_CREATOR_URL_LIST = [
    "https://tieba.baidu.com/home/main/?id=tb.1.7f139e2e.6CyEwxu3VJruH_-QqpCi6g&fr=frs",
    # ........................
]
