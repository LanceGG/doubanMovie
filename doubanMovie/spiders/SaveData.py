# -*- coding: utf-8 -*-
from doubanMovie.spiders.MySql import  mysql

class SaveData:
    def save_media_data(self, data):
        sql = "insert into media.media (id, title, rate, url, classify) VALUES "
        for i in range(len(data)):
            sql = sql + "( '" + data[i]['id'] + "' , '" + data[i]['title'] + "' , '" + data[i]['rate'] + "' , '" + data[i]['url'] + "' , '" + data[i]['classify'] + " ' )"
            if i != len(data)-1:
                sql = sql + ","
            else:
                sql = sql + ";"
        mysql().insertOperation(sql)

    def find_media_data(self):
        sql = "select * from media.media"