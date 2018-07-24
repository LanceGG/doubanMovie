# -*- coding: utf-8 -*-
import requests
import sys
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        detailURL = item['detailURL']
        path = item['path']
        fileName = item['fileName']

        image = requests.get(detailURL)
        f = open(path, 'wb')
        f.write(image.content)
        f.close()
        print ('正在保存图片：', detailURL)
        print ('图片路径：', path)
        print ('文件：', fileName)
        return item
