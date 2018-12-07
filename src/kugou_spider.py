# -*- coding: utf-8 -*-
# 酷狗音乐爬虫工具
from src.SingerList import SingerList

if __name__ == "__main__":
    #  获取歌手列表
    singer_list = SingerList()
    singer_list.start()
