# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item
class BaidustocksInfoPipeline(object):
    def open_spider(self,spider):
        self.f = open('D:/股票.csv','w+',newline='')
        stocktitle = ['企业','股票代码','今开', '成交量', '最高', '涨停', '内盘', '成交额', '委比', '流通市值', '市盈率', '每股收益', '总股本', '昨收', '换手率', '最低', '跌停', '外盘', '振幅', '量比', '总市值', '市净率', '每股净资产', '流通股本']
        self.write = csv.writer(self.f)
        self.write.writerow((stocktitle))
    def close_spider(self,spider):
        self.f.close()


    def process_item(self,item,spider):
        try:
            line = (item['信息'])
            if len(line)>10 and len(line)<25:
                self.write.writerow((line))
        except:
            pass
        return item
    
