# -*- coding: utf-8 -*-
import urllib2

from urllib2 import Request
from lxml import etree

from src.SongList import SongList


class SingerList:

    def __init__(self):
        self.head = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.baseUrl = "https://www.kugou.com/yy/singer/index/1-all-1.html"
        self.start_page = int(raw_input("请输入起始页："))
        self.end_page = int(raw_input("请输入终止页："))
        self.song_list = SongList()

    def start(self):
        self.song_list.reqJson("")
        # self.join_url()

    def join_url(self):
        for page in range(self.start_page, self.end_page):
            real_url = self.baseUrl + "{pg}-all-1.html".format(pg=page)
            self.reqSingerPage(real_url)

    def reqSingerPage(self, url):
        request = Request(url, headers=self.head)
        html = urllib2.urlopen(request).read()

        singer_head_url = etree.HTML(html).xpath('//*[@id="list_head"]/li[*]/a/@href')
        # singer_title = etree.HTML(html).xpath('//*[@id="list_head"]/li[*]/a/@title')
        singer_content_url = etree.HTML(html).xpath('//*[@id="list1"]/ul[*]/li[*]/a/@href')

        singer_head_url.extend(singer_content_url)

        print("请求明星主页总数:%d" % len(singer_head_url))

        for p in singer_content_url:
            print("请求明星主页:" + p + "\n")
            self.song_list.reqSongHash(p)
