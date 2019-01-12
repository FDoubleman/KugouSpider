# -*- coding: utf-8 -*-
from src.DbManager import dbManager
from src.Song_bean import Song_bean

str1 = "(2017\"\u6211\u60f3\"\u4e16\u754c\u5de1\u56de\u6f14\u5531\u4f1a\u2014\u53a6\u95e8\u7ad9)"
text = bytes(str1, "unicode_escape").decode("unicode_escape")
print(text)
songbean = Song_bean(hash="121", audio_name="哈哈")
dbManager.insert_song_table(songbean)
