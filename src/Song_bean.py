# -*- coding: utf-8 -*-
from typing import Any


class Song_bean:
    def __init__(self, hash, timelength="", filesize="", audio_name="", img="",
                 author_name="", song_name="", play_url="", bitrate=""):
        self.hash = hash
        self.timelength = timelength
        self.filesize = filesize
        self.audio_name = audio_name
        self.img = img
        self.author_name = author_name
        self.song_name = song_name
        self.play_url = play_url
        self.bitrate = bitrate
