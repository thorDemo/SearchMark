from peewee import *

db = MySQLDatabase("alizhizhuchi", host='23.110.211.170', port=3339, user='alizhizhuchi', passwd='3b86aba28d1ffc65', charset='utf8')


class SearchURL(Model):
    id = AutoField()
    title = TextField()

    class Meta:
        table_name = 'waiurl'
        database = db

    def get_all(self):
        pass