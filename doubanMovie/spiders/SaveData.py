# -*- coding: utf-8 -*-
from doubanMovie.spiders.MySql import  mysql

class SaveData:
    # 插入简略的剧集数据
    def save_media_data(self, data):
        sql = "insert into mediadb.media_simple (id, title, rate, url, classify) VALUES "
        for i in range(len(data)):
            sql = sql + "( '" + data[i]['id'].replace("'", "''") + "', '" + data[i]['title'].replace("'", "''") + "', '" \
                  + data[i]['rate'].replace("'", "''") + "', '" + data[i]['url'].replace("'", "''") + "', '" + data[i]['classify'].replace("'", "''") + "')"
            if i != len(data)-1:
                sql = sql + ","
            else:
                sql = sql + ";"
        mysql().insertOperation(sql)

    # 插入详细的剧集数据
    def save_media_detail(self, data):
        sql = "INSERT INTO `mediadb`.`media_detail` (`id`,`title`,`title_long`,`m_year`,`classify`," \
              "`m_type`,`country`,`m_language`,`release_date`,`runtime`,`season`,`episodes`,`along_run_time`,`alias`," \
              "`imdb_id`,`score`,`stars5`,`stars4`,`stars3`,`stars2`,`stars1`,`people_num`,`tags`,`report`)VALUES"
        sql = sql + "('" + data['id'].replace("'", "''") + "', '" + data['title'].replace("'", "''") + "', '" + data['titleLong'].replace("'", "''") + "', '" + data['year'].replace("'", "''") \
              + "', '" + data['classify'].replace("'", "''") + "', '" + data['type'].replace("'", "''") + "', '" + data['country'].replace("'", "''") + "', '" + data['language'].replace("'", "''") \
              + "', '" + data['releaseDate'].replace("'", "''") + "', '" + data['runtime'].replace("'", "''") + "', '" + data['season'].replace("'", "''") + "', '" + data['episodes'].replace("'", "''") \
              + "', '" + data['alongRuntime'].replace("'", "''") + "', '" + data['alias'].replace("'", "''") + "', '" + data['imdbId'].replace("'", "''") + "', '" + data['score'].replace("'", "''") \
              + "', '" + data['rating']['stars5'].replace("'", "''") + "', '" + data['rating']['stars4'].replace("'", "''") + "', '" + data['rating']['stars3'].replace("'", "''") + "', '" + data['rating']['stars2'].replace("'", "''") \
              + "', '" + data['rating']['stars1'].replace("'", "''") + "', '" + data['rating']['peopleNum'].replace("'", "''") + "', '" + data['tags'].replace("'", "''") + "', '" + data['report'].replace("'", "''") + "');"
        mysql().insertOperation(sql)

    # 插入剧集推荐
    def save_media_recommend(self, recommendList, id, title):
        sql = "insert into mediadb.media_recommend (id, title, recommend_id, recommend_title) values "
        for i in range(len(recommendList)):
            sql = sql + "('" + id.replace("'", "''") + "', '" + title.replace("'", "''") + "', '" + recommendList[i]['id'].replace("'", "''") + "', '" + recommendList[i]['name'].replace("'", "''") + "')"
            if i != len(recommendList)-1:
                sql = sql + ","
            else:
                sql = sql + ";"
        mysql().insertOperation(sql)

    # 插入人员数据
    def save_media_attr(self, dataList, id, title, type):
        sql = "insert into mediadb.media_attender (id, title, attender_id, attender_name, attender_type) values "
        for i in range(len(dataList)):
            sql = sql + "('" + id.replace("'", "''") + "', '" + title.replace("'", "''") + "', '" + dataList[i]['id'].replace("'", "''") + "', '" + dataList[i]['name'].replace("'", "''") + "', '" + type.replace("'", "''") + "')"
            if i != len(dataList)-1:
                sql = sql + ","
            else:
                sql = sql + ";"
        mysql().insertOperation(sql)

    # 存储简略剧集数据爬取进度
    def save_history_data(self, targetNum, num):
        sql = "update mediadb.history_data set target_num = " + str(targetNum) + ", num = " + str(num) + " where id = 1;"
        mysql().updateOperation(sql)

    # 查找简略剧集爬取进度
    def query_history_data(self):
        sql = "select target_num, num from mediadb.history_data where id = 1;"
        return mysql().queryOperation(sql)

    # 查找简略的剧集数据
    def query_media_data(self, start, size):
        sql = "select * from mediadb.media_simple order by media_id limit " + str(start) + ", " + str(size) + ";"
        return mysql().queryOperation(sql)

    # 查找演员的数据
    def query_actor_id(self):
        pass

    # 查找剧集详情, 人员, 图片, 获奖情况爬取进度
    def query_media_history(self, type):
        sql = "select * from mediadb.query_history_data where type = '" + str(type) + "';"
        return mysql().queryOperation(sql)

    # 存储剧集详情, 人员, 图片, 获奖情况爬取进度
    def update_media_history(self, type):
        sql = "update mediadb.query_history_data set num = num + 1 where type = '" + type + "' ;"
        mysql().updateOperation(sql)

    # 存储剧集获奖数据
    def save_media_award(self, dataList):
        sql = "insert into mediadb.media_award (id, title, award_name, award_year, award_type, award_user_id, award_user_name) values "
        for i in range(len(dataList)):
            sql = sql + "('" + dataList[i]['id'].replace("'", "''") + "', '" + dataList[i]['title'].replace("'", "''") + "', '" + dataList[i]['awardName'].replace("'", "''") + "', '" + dataList[i]['awardYear'].replace("'", "''") + "', '" + dataList[i]['awardType'].replace("'", "''") + "', '" + dataList[i]['awardUserId'].replace("'", "''") + "', '" + dataList[i]['awardUserName'].replace("'", "''") + "')"
            if i != len(dataList) - 1:
                sql = sql + ","
            else:
                sql = sql + ";"
        mysql().insertOperation(sql)

    # 存储图片id
    def save_media_pic_id(self, dataList):
        sql = "insert into mediadb.media_pic (id, title, pic_id) values "
        for i in range(len(dataList)):
            sql = sql + "('" + dataList[i]['id'].replace("'", "''") + "', '" + dataList[i]['title'].replace("'", "''") + "', '" + dataList[i]['picId'].replace("'", "''") + "')"
            if i != len(dataList) - 1:
                sql = sql + ","
            else:
                sql = sql + ";"
        mysql().insertOperation(sql)

    # 存储人员详情
    def save_perform_detail(self):
        pass

    def query_media_pic_id(self, movieId):
        sql = "select * from mediadb.media_pic where id = " + movieId + ";"
        return mysql().queryOperation(sql)