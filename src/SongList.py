# -*- coding: utf-8 -*-
import urllib2

from urllib2 import Request
from lxml import etree
import requests


class SongList:

    def __init__(self):
        self.head = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.base_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=5FCE4CBCB96D6025033BCE2025FC3943"
        pass

    # 过滤 url
    def filter_url(self, url):
        self.reqSongHash(url)

    # 请求歌曲的hash
    def reqSongHash(self, url):
        request = Request(url, headers=self.head)
        html = urllib2.urlopen(request).read()
        song_value = etree.HTML(html).xpath('//*[@id="song_container"]/li[*]/a/input/@value')
        for value in song_value:
            print(value)
            self.disposeValue(value)

    # 处理value
    def disposeValue(self, value):
        result = value.split("|")
        if len(result) >= 2:
            hash = result[1]
            print("hash :{}".format(hash))

    def reqJson(self, hash):
        json_ = requests.get(self.base_url)
        print(json_.text)
