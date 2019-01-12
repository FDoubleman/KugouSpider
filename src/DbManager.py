# -*- coding: utf-8 -*-
import pymysql

from src.Song_bean import Song_bean


class DbManager(object):

    def __init__(self) -> None:
        super().__init__()
        self.con = self.initDB()

    def initDB(self):
        return pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='1234',
                               database='sp_kugou')

    def insert_song_table(self, songbean):
        cur = self.con.cursor()
        try:
            sql = "insert into song_table(hash, timelength, filesize, audio_name, img, author_name, song_name, play_url, bitrate) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                  % (songbean.hash, songbean.timelength, songbean.filesize, songbean.audio_name, songbean.img,
                     songbean.author_name, songbean.song_name, songbean.play_url, songbean.bitrate)
            cur.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()
            print('Insert operation error')
            raise
        finally:
            cur.close()
            self.con.close()


dbManager = DbManager()
