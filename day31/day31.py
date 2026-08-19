"""
day31

Author:ignorant-fool
Version:0.1
Date:2026/8/19
"""

# project122 - 用元类实现单例模式

import threading

class SingletonMeta(type):
    """自定义元类"""

    def __init__(cls, *args, **kwargs):
        