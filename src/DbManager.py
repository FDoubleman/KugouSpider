# -*- coding: utf-8 -*-
import pymysql


def connect_mysql_db():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='1234',
                           database='sp_kugou')


def insert_file_rec(hash1, timelength2):
    con = connect_mysql_db()
    cur = con.cursor()
    try:
        sql = """INSERT INTO song_table(hash,
                 timelength)
                 VALUES ('23121', '1000')"""
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
        print('Insert operation error')
        raise
    finally:
        cur.close()
        con.close()
