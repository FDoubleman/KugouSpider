# -*- coding: utf-8 -*-
from src.DbManager import insert_file_rec

str1 = "(2017\"\u6211\u60f3\"\u4e16\u754c\u5de1\u56de\u6f14\u5531\u4f1a\u2014\u53a6\u95e8\u7ad9)"
text = bytes(str1, "unicode_escape").decode("unicode_escape")
print(text)
insert_file_rec("123123", "1000")
