# -*- coding: utf-8 -*-
import requests


class SongDownload:
    def __init__(self):
        self.save_path = "D:\\python_kugou"
        pass

    def download(self, song_name, song_url):
        if len(song_name) == 0 or len(song_url) == 0:
            pass
        self.filter(song_name, song_url)

    def filter(self, song_name, song_url):
        with open(self.save_path + "\\%s.mp3" % song_name, "wb") as f:
            response = requests.get(song_url)
            f.write(response.content)
            print("已下载%s " % song_name)
