# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request

from lxml import etree
import requests
import json

from src.SongDownload import SongDownload


class SongList:

    def __init__(self):
        self.head = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.base_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash="
        self.s_download = SongDownload()
        pass

    # 过滤 url
    def filter_url(self, url):
        self.reqSongHash(url)

    # 请求歌曲的hash
    def reqSongHash(self, url):
        request = Request(url, headers=self.head)
        html = urllib.request.urlopen(request).read()
        song_value = etree.HTML(html).xpath('//*[@id="song_container"]/li[*]/a/input/@value')
        for value in song_value:
            # print(value)
            self.disposeValue(value)

    # 处理value
    def disposeValue(self, value):
        result = value.split("|")
        if len(result) >= 2:
            hash = result[1]
            self.reqJson(hash)
            print("hash :{}".format(hash))

    def reqJson(self, hash):
        # hash = "E72A27BAB2E41E13E94422A068B33459"
        real_url = self.base_url + hash
        response = requests.get(real_url)
        text = response.content.decode("unicode_escape")
        s_text = text.replace("\r\n", "")
        s_text = s_text.replace(" \"", " ")
        s_text = s_text.replace("\" ", " ")
        s_text = s_text.replace("\t", "")

        # 处理json 含有""的情况
        # s_text = self.shuangyinhao(s_text)

        print(s_text)
        obj = json.loads(s_text, encoding="utf-8")
        song_name = obj['data']['audio_name']
        song_url = obj["data"]["play_url"]
        print(obj["data"]["audio_name"])
        print(obj["data"]["play_url"])
        self.s_download.download(song_name, song_url)


