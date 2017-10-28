#encoding:utf-8
import os
import configparser


f=open("conf.txt",'r')
cmd=f.readline()
#os.system(cmd)

#encoding:utf-8
#name:mod_config.py


#获取config配置文件
def getConfig(section, key):
    config = configparser.ConfigParser()
    print("当前目录:",os.path.split(os.path.realpath(__file__))[0])
    path = os.path.split(os.path.realpath(__file__))[0] + '/db.conf'
    config.read(path,encoding='utf-8')
    return config.get(section, key)

#其中 os.path.split(os.path.realpath(__file__))[0] 得到的是当前文件模块的目录

dbname = getConfig("database", "dbname")

print(dbname)